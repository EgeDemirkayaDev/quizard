from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Taban

# --- KULLANICI İŞLEMLERİ ---
class Kullanici(Taban):
    __tablename__ = "kullanicilar"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_adi = Column(String(50), unique=True, nullable=False)
    eposta = Column(String(100), unique=True, nullable=False)
    sifre_hash = Column(String(255), nullable=False)
    bildirimler_acik = Column(Boolean, default=True)
    tema_tercihi = Column(String(20), default='gunduz')
    aktif_mi = Column(Boolean, default=True)
    olusturulma_tarihi = Column(DateTime(timezone=True), server_default=func.now())

# --- TEST YAPISI (İÇERİK) ---
class Test(Taban):
    __tablename__ = "testler"

    id = Column(Integer, primary_key=True, index=True)
    baslik = Column(String(100), nullable=False)
    aciklama = Column(Text)
    ikon = Column(String(10))
    kategori = Column(String(50)) # Örn: 'Karakter', 'Akademik'
    
    # Testin içindeki sorulara hızlı erişim
    sorular = relationship("Soru", back_populates="test", cascade="all, delete-orphan")

class Soru(Taban):
    __tablename__ = "sorular"

    id = Column(Integer, primary_key=True, index=True)
    test_id = Column(Integer, ForeignKey("testler.id", ondelete="CASCADE"))
    soru_metni = Column(Text, nullable=False)
    sira = Column(Integer) # Soruların hangi sırayla çıkacağı

    test = relationship("Test", back_populates="sorular")
    secenekler = relationship("Secenek", back_populates="soru", cascade="all, delete-orphan")

class Secenek(Taban):
    __tablename__ = "secenekler"

    # BURASI ÖNEMLİ: Her şıkkın kendi benzersiz ID'si var (Senin istediğin kural)
    id = Column(Integer, primary_key=True, index=True)
    soru_id = Column(Integer, ForeignKey("sorular.id", ondelete="CASCADE"))
    metin = Column(Text, nullable=False)
    
    # ALGORİTMA BURADA ÇALIŞACAK:
    # Hangi profile puan vereceğini tutar (Örn: 'Golden Retriever', 'Turgut Hoca', 'A')
    etiket = Column(String(50)) 
    # Bazı testlerde (Hoca testi gibi) her şıkkın ağırlığı farklı olabilir
    puan_agirligi = Column(Float, default=1.0) 

    soru = relationship("Soru", back_populates="secenekler")

# --- KULLANICI ETKİLEŞİMİ VE SONUÇLAR ---
class TestSonucu(Taban):
    __tablename__ = "test_sonuclari"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id", ondelete="CASCADE"))
    test_id = Column(Integer, ForeignKey("testler.id", ondelete="CASCADE"))
    alinan_sonuc = Column(String(100)) # Örn: 'Siber Güvenlik Uzmanı'
    detayli_analiz = Column(Text) # Sonuç paragrafı buraya gelecek
    olusturulma_tarihi = Column(DateTime(timezone=True), server_default=func.now())

class Favori(Taban):
    __tablename__ = "favoriler"
    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id", ondelete="CASCADE"))
    test_id = Column(Integer, ForeignKey("testler.id", ondelete="CASCADE"))

class Yorum(Taban):
    __tablename__ = "yorumlar"
    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id", ondelete="CASCADE"))
    test_id = Column(Integer, ForeignKey("testler.id", ondelete="CASCADE"))
    icerik = Column(Text, nullable=False)
    olusturulma_tarihi = Column(DateTime(timezone=True), server_default=func.now())