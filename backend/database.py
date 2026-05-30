from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite veritabanı dosyasının yolu (Proje klasöründe otomatik oluşur)
DATABASE_URL = "sqlite:///./quizard.db"

# Motoru oluşturuyoruz (SQLite için check_same_thread ayarı zorunludur)
motor = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}, 
    echo=False
)

# Veritabanı oturumu yönetimi (Aynen korundu)
OturumYerel = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=motor
)

# Modellerin türeyeceği ana sınıf (Aynen korundu)
Taban = declarative_base()