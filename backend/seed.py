from database import OturumYerel, Taban, motor
import models

from seed_data.kisilik_testi import KISILIK_TESTI
from seed_data.hoca_testi import HOCA_TESTI
from seed_data.alan_testi import ALAN_TESTI
from seed_data.iliski_testi import ILISKI_TESTI


# Tüm testleri istediğimiz sırayla burada topluyoruz.
TESTLER = [
    KISILIK_TESTI,
    HOCA_TESTI,
    ALAN_TESTI,
    ILISKI_TESTI,
]


# Veritabanı tablolarını oluşturur.
def tablolari_olustur():
    Taban.metadata.create_all(bind=motor)


# Eski seed verilerini temizler.
# Böylece seed.py tekrar çalıştırıldığında aynı veriler tekrar tekrar eklenmez.
def verileri_temizle(db):
    db.query(models.OptionScore).delete()
    db.query(models.TestResult).delete()
    db.query(models.Comment).delete()
    db.query(models.SavedTest).delete()
    db.query(models.Favorite).delete()
    db.query(models.Option).delete()
    db.query(models.Question).delete()
    db.query(models.ResultProfile).delete()
    db.query(models.Test).delete()
    db.commit()


# Tek bir testi; profilleri, soruları, şıkları ve puanlarıyla ekler.
def test_ekle(db, test_data):
    yeni_test = models.Test(
        slug=test_data["slug"],
        title=test_data["title"],
        short_title=test_data.get("short_title"),
        description=test_data.get("description"),
        category=test_data.get("category"),
        icon=test_data.get("icon"),
        button_text=test_data.get("button_text"),
        display_order=test_data.get("display_order", 0),
        is_active=True
    )

    db.add(yeni_test)
    db.commit()
    db.refresh(yeni_test)

    profil_map = {}

    # Sonuç profillerini ekliyoruz.
    for profil_data in test_data["profiles"]:
        profil = models.ResultProfile(
            test_id=yeni_test.id,
            code=profil_data["code"],
            title=profil_data["title"],
            description=profil_data["description"],
            icon=profil_data.get("icon"),
            is_hybrid=profil_data.get("is_hybrid", False)
        )

        db.add(profil)
        db.commit()
        db.refresh(profil)

        profil_map[profil.code] = profil

    # Soruları ve seçenekleri ekliyoruz.
    for soru_sira, soru_data in enumerate(test_data["questions"], start=1):
        soru = models.Question(
            test_id=yeni_test.id,
            text=soru_data["text"],
            display_order=soru_sira,
            is_tiebreaker=soru_data.get("is_tiebreaker", False),
            tiebreaker_order=soru_data.get("tiebreaker_order")
        )

        db.add(soru)
        db.commit()
        db.refresh(soru)

        for secenek_sira, secenek_data in enumerate(soru_data["options"], start=1):
            secenek = models.Option(
                question_id=soru.id,
                text=secenek_data["text"],
                option_key=secenek_data["key"],
                display_order=secenek_sira
            )

            db.add(secenek)
            db.commit()
            db.refresh(secenek)

            # Seçeneğin hangi profile kaç puan verdiğini burada ekliyoruz.
            for profil_code, puan in secenek_data["scores"].items():
                profil = profil_map.get(profil_code)

                if profil is None:
                    raise ValueError(f"Profil bulunamadı: {profil_code}")

                skor = models.OptionScore(
                    option_id=secenek.id,
                    profile_id=profil.id,
                    score=puan
                )

                db.add(skor)

            db.commit()


def verileri_yukle():
    tablolari_olustur()
    db = OturumYerel()

    try:
        verileri_temizle(db)

        for test_data in TESTLER:
            test_ekle(db, test_data)

        print("✅ Tüm testler başarıyla veritabanına eklendi.")

    except Exception as hata:
        db.rollback()
        print("❌ Seed sırasında hata oluştu:", hata)

    finally:
        db.close()


if __name__ == "__main__":
    verileri_yukle()