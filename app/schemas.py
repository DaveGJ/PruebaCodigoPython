# app/schemas.py

from pydantic import BaseModel


class ApplicantCreate(BaseModel):
    dni: str
    name: str
    surname: str