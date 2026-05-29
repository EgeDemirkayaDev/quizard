import json
from collections import defaultdict

from fastapi import FastAPI, Depends, HTTPException
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, selectinload

import models
from database import Taban, motor, OturumYerel
from schemas import SubmitTestRequest, RegisterRequest, LoginRequest


Taban.metadata.create_all(bind=motor)

app = FastAPI(title="Quizard API")
# Şifreleri düz metin olarak saklamıyoruz.
# Kullanıcının şifresi veritabanına hashlenmiş şekilde kaydedilir.
sifreleme = CryptContext(schemes=["bcrypt"], deprecated="auto")


def sifreyi_hashle(sifre: str):
    return sifreleme.hash(sifre)


def sifre_dogru_mu(girilen_sifre: str, kayitli_hash: str):
    return sifreleme.verify(girilen_sifre, kayitli_hash)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = OturumYerel()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Quizard API çalışıyor."}
@app.post("/api/register")
def register(payload: RegisterRequest, db: Session = Depends(get_db)):

    # Kullanıcı boş alan bırakmış mı kontrol ediyoruz.
    if not payload.username.strip() or not payload.email.strip() or not payload.password.strip():
        raise HTTPException(
            status_code=400,
            detail="Lütfen tüm alanları doldurun."
        )

    # Şifre yeterince uzun mu?
    if len(payload.password) < 6:
        raise HTTPException(
            status_code=400,
            detail="Şifre en az 6 karakter olmalıdır."
        )

    # Aynı kullanıcı adı daha önce alınmış mı?
    ayni_username = (
        db.query(models.User)
        .filter(models.User.username == payload.username)
        .first()
    )

    if ayni_username:
        raise HTTPException(
            status_code=400,
            detail="Bu kullanıcı adı zaten kullanılıyor."
        )

    # Aynı e-posta kayıtlı mı?
    ayni_email = (
        db.query(models.User)
        .filter(models.User.email == payload.email)
        .first()
    )

    if ayni_email:
        raise HTTPException(
            status_code=400,
            detail="Bu e-posta adresi zaten kayıtlı."
        )

    # Yeni kullanıcı oluşturuyoruz.
    yeni_kullanici = models.User(
        username=payload.username,
        email=payload.email,

        # Şifreyi HASHLEYİP kaydediyoruz.
        password_hash=sifreyi_hashle(payload.password)
    )

    db.add(yeni_kullanici)
    db.commit()
    db.refresh(yeni_kullanici)

    return {
        "message": "Üyelik başarıyla oluşturuldu.",
        "user": {
            "id": yeni_kullanici.id,
            "username": yeni_kullanici.username,
            "email": yeni_kullanici.email
        }
    }


@app.post("/api/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):

    # Kullanıcı boş alan bırakmış mı?
    if not payload.username.strip() or not payload.password.strip():
        raise HTTPException(
            status_code=400,
            detail="Kullanıcı adı ve şifre boş bırakılamaz."
        )

    # Kullanıcıyı veritabanında arıyoruz.
    kullanici = (
        db.query(models.User)
        .filter(models.User.username == payload.username)
        .first()
    )

    # Kullanıcı bulunamadıysa
    if not kullanici:
        raise HTTPException(
            status_code=404,
            detail="Bu kullanıcı adına ait hesap bulunamadı."
        )

    # Şifre yanlış mı?
    if not sifre_dogru_mu(payload.password, kullanici.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Şifre yanlış. Lütfen tekrar deneyiniz."
        )

    return {
        "message": "Giriş başarılı.",
        "user": {
            "id": kullanici.id,
            "username": kullanici.username,
            "email": kullanici.email
        }
    }

@app.get("/api/tests")
def get_tests(db: Session = Depends(get_db)):
    tests = (
        db.query(models.Test)
        .filter(models.Test.is_active == True)
        .order_by(models.Test.display_order.asc())
        .all()
    )

    return [
        {
            "id": test.id,
            "slug": test.slug,
            "title": test.title,
            "shortTitle": test.short_title,
            "description": test.description,
            "category": test.category,
            "icon": test.icon,
            "buttonText": test.button_text,
            "order": test.display_order,
        }
        for test in tests
    ]


@app.get("/api/tests/{test_id}")
def get_test_detail(test_id: int, db: Session = Depends(get_db)):
    test = (
        db.query(models.Test)
        .options(
            selectinload(models.Test.questions).selectinload(models.Question.options)
        )
        .filter(models.Test.id == test_id, models.Test.is_active == True)
        .first()
    )

    if not test:
        raise HTTPException(status_code=404, detail="Test bulunamadı.")

    sorted_questions = sorted(test.questions, key=lambda q: q.display_order)

    return {
        "id": test.id,
        "slug": test.slug,
        "title": test.title,
        "description": test.description,
        "icon": test.icon,
        "category": test.category,
        "questions": [
            {
                "id": question.id,
                "text": question.text,
                "order": question.display_order,
                "options": [
                    {
                        "id": option.id,
                        "text": option.text,
                        "optionKey": option.option_key,
                    }
                    for option in sorted(question.options, key=lambda o: o.display_order)
                ],
            }
            for question in sorted_questions
        ],
    }


@app.post("/api/tests/{test_id}/submit")
def submit_test(test_id: int, payload: SubmitTestRequest, db: Session = Depends(get_db)):
    test = (
        db.query(models.Test)
        .options(
            selectinload(models.Test.profiles),
            selectinload(models.Test.questions).selectinload(models.Question.options)
        )
        .filter(models.Test.id == test_id, models.Test.is_active == True)
        .first()
    )

    if not test:
        raise HTTPException(status_code=404, detail="Test bulunamadı.")

    if not payload.option_ids:
        raise HTTPException(status_code=400, detail="En az bir seçenek seçilmelidir.")

    selected_options = (
        db.query(models.Option)
        .options(
            selectinload(models.Option.scores).selectinload(models.OptionScore.profile),
            selectinload(models.Option.question),
        )
        .filter(models.Option.id.in_(payload.option_ids))
        .all()
    )

    if len(selected_options) != len(payload.option_ids):
        raise HTTPException(status_code=400, detail="Geçersiz seçenek gönderildi.")

    scores = defaultdict(float)

    for option in selected_options:
        if option.question.test_id != test_id:
            raise HTTPException(status_code=400, detail="Seçenek bu teste ait değil.")

        for score_item in option.scores:
            scores[score_item.profile.code] += score_item.score

    if not scores:
        raise HTTPException(status_code=400, detail="Bu test için puanlama bulunamadı.")

    profiles_by_code = {profile.code: profile for profile in test.profiles}

    max_score = max(scores.values())
    winner_codes = [code for code, score in scores.items() if score == max_score]

    winner_code = resolve_winner_by_tiebreaker(
        winner_codes=winner_codes,
        selected_options=selected_options,
        test=test,
        db=db
    )

    winner_profile = profiles_by_code.get(winner_code)

    if not winner_profile:
        raise HTTPException(status_code=500, detail="Sonuç profili bulunamadı.")

    return {
        "resultTitle": winner_profile.title,
        "resultDescription": winner_profile.description,
        "scores": dict(scores),
    }


def resolve_winner_by_tiebreaker(winner_codes, selected_options, test, db):
    if len(winner_codes) == 1:
        return winner_codes[0]

    selected_by_question_id = {
        option.question_id: option for option in selected_options
    }

    tiebreak_questions = sorted(
        [q for q in test.questions if q.is_tiebreaker],
        key=lambda q: q.tiebreaker_order or 999
    )

    for question in tiebreak_questions:
        selected_option = selected_by_question_id.get(question.id)
        if not selected_option:
            continue

        option_scores = (
            db.query(models.OptionScore)
            .join(models.ResultProfile)
            .filter(
                models.OptionScore.option_id == selected_option.id,
                models.ResultProfile.code.in_(winner_codes)
            )
            .all()
        )

        if not option_scores:
            continue

        local_scores = defaultdict(float)
        for item in option_scores:
            local_scores[item.profile.code] += item.score

        local_max = max(local_scores.values())
        local_winners = [
            code for code, value in local_scores.items()
            if value == local_max
        ]

        if len(local_winners) == 1:
            return local_winners[0]

    return winner_codes[0]