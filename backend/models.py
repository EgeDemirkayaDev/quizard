from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Taban

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

class Test(Taban):
    __tablename__ = "testler"

    id = Column(Integer, primary_key=True, index=True)
    baslik = Column(String(100), nullable=False)
    aciklama = Column(Text)
    ikon = Column(String(10))
    buton_metni = Column(String(50))

class Favori(Taban):
    __tablename__ = "favoriler"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id", ondelete="CASCADE"))
    test_id = Column(Integer, ForeignKey("testler.id", ondelete="CASCADE"))
    olusturulma_tarihi = Column(DateTime(timezone=True), server_default=func.now())

class Kaydedilen(Taban):
    __tablename__ = "kaydedilenler"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id", ondelete="CASCADE"))
    test_id = Column(Integer, ForeignKey("testler.id", ondelete="CASCADE"))
    olusturulma_tarihi = Column(DateTime(timezone=True), server_default=func.now())

class Yorum(Taban):
    __tablename__ = "yorumlar"

    id = Column(Integer, primary_key=True, index=True)
    kullanici_id = Column(Integer, ForeignKey("kullanicilar.id", ondelete="CASCADE"))
    test_id = Column(Integer, ForeignKey("testler.id", ondelete="CASCADE"))
    icerik = Column(Text, nullable=False)
    olusturulma_tarihi = Column(DateTime(timezone=True), server_default=func.now())