import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_SIFRE = os.getenv("MYSQL_SIFRE", "")
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_DB = os.getenv("MYSQL_DB", "quizard_db")

if MYSQL_SIFRE:
	DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_SIFRE}@{MYSQL_HOST}/{MYSQL_DB}?charset=utf8mb4"
else:
	DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}@{MYSQL_HOST}/{MYSQL_DB}?charset=utf8mb4"

motor = create_engine(DATABASE_URL, echo=False)

OturumYerel = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=motor
)

Taban = declarative_base()

