# app/models.py

from sqlalchemy import Column, String
from .database import Base


class Applicant(Base):
    __tablename__ = 'applicants'

    dni = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)