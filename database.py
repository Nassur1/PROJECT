import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL local database configuration
DB_HOST = "localhost"
DB_NAME = "car_management_db"
DB_USER = "postgres"
DB_PASS = "ibra"  # your local PostgreSQL password
DB_PORT = "5432"

# Construct the local database URL
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Initialize SQLAlchemy
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

def close_db(db):
    db.close()
