import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Gizli kasadaki (.env) şifreyi oku
load_dotenv()
GIZLI_SIFRE = os.getenv("MYSQL_SIFRE")

# 2. Eğer şifre yoksa boş bırak, varsa şifreli bağlan (Dinamik ve güvenli yapı)
if GIZLI_SIFRE:
    VT_URL = f"mysql+pymysql://root:{GIZLI_SIFRE}@localhost/quizard_db"
else:
    VT_URL = "mysql+pymysql://root@localhost/quizard_db"

# 3. Veritabanı motorunu çalıştır
motor = create_engine(VT_URL)

# 4. Backend'in kullanacağı oturum
OturumYerel = sessionmaker(autocommit=False, autoflush=False, bind=motor)

# 5. Tabloların anası
Taban = declarative_base()