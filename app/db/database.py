from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Motor de la BD
engine = create_engine(settings.database_url, echo=True)

# Sesión (cada request obtiene su propia)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para heredar en modelos
Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()