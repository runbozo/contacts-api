from pydantic import BaseModel
from typing import Optional
from app import db
from sqlite3 import IntegrityError


class ContactBodyModel(BaseModel):
    id: Optional[int]
    email: str
    first_name: str
    last_name: Optional[str]
    phone: Optional[str]
    country: Optional[str]
    city: Optional[str]
    address: Optional[str]


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), index=True, unique=True)
    first_name = db.Column(db.String(16))
    last_name = db.Column(db.String(16))
    phone = db.Column(db.String(16))
    country = db.Column(db.String(8))
    city = db.Column(db.String(16))
    address = db.Column(db.String(64))

    def __repr__(self):
        return f'<Contact ID {self.id}>'

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                try:
                    setattr(self, key, value)
                except IntegrityError:
                    pass
