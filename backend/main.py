from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel   # YENİ EKLENDİ
from collections import Counter  # YENİ EKLENDİ
import models
from database import OturumYerel, motor

# Veritabanı tablolarını onaylıyoruz
models.Taban.metadata.create_all(bind=motor)

# Backend sunucumuzu başlatıyoruz
app = FastAPI(title="Quizard API")

# React (Vite) farklı portta çalıştığı için güvenlik duvarını (CORS) esnetiyoruz
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # React'ın bizimle konuşmasına izin ver
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Her işlemde veritabanı kapısını açıp kapatan yardımcı fonksiyon
def get_db():
    db = OturumYerel()
    try:
        yield db
    finally:
        db.close()

# 1. Ana Sayfa Kontrolü
@app.get("/")
def ana_sayfa():
    return {"mesaj": "🚀 Quizard Backend Motoru Tıkır Tıkır Çalışıyor!"}

# 2. Testi ve Sorularını React'a Gönderen Gişe (Endpoint)
@app.get("/api/testler/{test_id}")
def testi_getir(test_id: int, db: Session = Depends(get_db)):
    # Kasadan ID'si girilen testi bul
    test = db.query(models.Test).filter(models.Test.id == test_id).first()
    
    if not test:
        raise HTTPException(status_code=404, detail="Kanka böyle bir test yok!")
        
    # React'ın anlayacağı tertemiz bir JSON paketine çevirip yolluyoruz
    return {
        "id": test.id,
        "baslik": test.baslik,
        "aciklama": test.aciklama,
        "kategori": test.kategori,
        "sorular": [
            {
                "id": soru.id,
                "metin": soru.soru_metni,
                "secenekler": [
                    {
                        "id": secenek.id,
                        "metin": secenek.metin
                        # Dikkat: Hangi hocaya ait olduğunu (etiket) Frontend'e GÖNDERMİYORUZ.
                        # Kopya çekemesinler, algoritma backend'de gizli kalacak!
                    } for secenek in soru.secenekler
                ]
            } for soru in test.sorular
        ]
    }
# React'tan gelecek verinin şablonu (Kullanıcı hangi şıkları seçti?)
class TestCevap(BaseModel):
    secenek_idleri: list[int]

# 3. Sonuç Hesaplama ve Gönderme Gişesi
@app.post("/api/testler/{test_id}/hesapla")
def test_sonucunu_hesapla(test_id: int, cevap: TestCevap, db: Session = Depends(get_db)):
    # 1. React'tan gelen şık ID'lerini veritabanında bul
    secilen_siklar = db.query(models.Secenek).filter(models.Secenek.id.in_(cevap.secenek_idleri)).all()

    # 2. Hocaların puanlarını topla (Örn: Turgut: 2, Aydın: 1)
    # Burada notundaki "aynı anda birkaç hocanın özelliklerini taşıyabiliyor" kuralı devreye giriyor!
    puanlar = Counter([sik.etiket for sik in secilen_siklar if sik.etiket])

    if not puanlar:
        raise HTTPException(status_code=400, detail="Hiç şık seçilmemiş!")

    # 3. En yüksek puanı alan hocayı bul
    kazanan_hoca = puanlar.most_common(1)[0][0]

    # 4. Word dosyasındaki efsane analiz metinleri (Şimdilik örnek, ileride veritabanına alacağız)
    sonuc_metni = ""
    if kazanan_hoca == "Turgut":
        sonuc_metni = "Sende ders saati bir öneri değil, adeta bölüm anayasasının ilk maddesi gibidir; kapı açılmışsa açılmıştır, kapanmışsa da 'ama trafik vardı' hikâyesi seni pek etkilemez."
    elif kazanan_hoca == "Aydın":
        sonuc_metni = "Sen tam anlamıyla klasik üniversite hocası enerjisi taşırsın: kuralları sever, düzeni önemser, ama bunu bağırıp çağırarak değil, hafif eski usul bir ciddiyetle yaparsın."
    elif kazanan_hoca == "Deniz":
        sonuc_metni = "Senin enerjin sınıfa girer girmez 'sert görünmeden otorite kurulabiliyormuş' hissi yaratır."
    else:
        sonuc_metni = f"Senin içindeki hoca ruhu tam bir {kazanan_hoca} hocadır!"

    # 5. TODO: Burada ileride bu sonucu 'test_sonuclari' tablosuna kaydedeceğiz.

    # 6. React'a sonucu jilet gibi gönder
    return {
        "kazanan": kazanan_hoca,
        "aciklama": sonuc_metni,
        "detayli_puanlar": dict(puanlar) # Hangi hocadan kaç puan aldığını da gizlice gönderiyoruz
    }