# app/main.py

from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine
from fastapi import Depends

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/candidato")
def create_applicant(applicant: schemas.ApplicantCreate, db: Session = Depends(get_db)):
    db_applicant = models.Applicant(dni=applicant.dni, name=applicant.name, surname=applicant.surname)

    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)

    return db_applicant