from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
<<<<<<< HEAD

engine = create_engine(DATABASE_URL, echo=True)
=======
print(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True,pool_pre_ping=True)
>>>>>>> 19ffcea (updated db connection and added models)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
<<<<<<< HEAD
=======

from db import engine

try:
    conn = engine.connect()
    print("✅ Connected to Neon DB")
    conn.close()
except Exception as e:
    print("❌ Error:", e)        
>>>>>>> 19ffcea (updated db connection and added models)
