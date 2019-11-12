import random
import string
from db import db


def random_string() -> str:
    """Generate a random string of fixed length of 8"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))


class UrlModel(db.Model):
    __tablename__ = "urls"

    id = db.Column(db.Integer, primary_key=True)
    shortened_url = db.Column(db.String(8), nullable=False, unique=True)
    actual_url = db.Column(db.String(564), nullable=False)

    @classmethod
    def find_by_shortened_url(cls, shortened_url: str) -> "UrlModel":
        return cls.query.filter_by(shortened_url=shortened_url).first()

    def save_to_db(self) -> str:
        self.shortened_url = random_string()
        db.session.add(self)
        db.session.commit()
        return self.shortened_url
