from datetime import datetime, date
from app import db
from sqlalchemy import exists


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35), unique=True)
    gender = db.Column(db.String(35))
    breed = db.Column(db.String(35))
    date_of_birth = db.Column(db.DATE(), default=datetime.today())
    details = db.Column(db.TEXT(70))
    price = db.Column(db.Integer())
    image = db.Column(db.String(200))


def first_pets():
    if not db.session.query(exists().where(Pet.name in ['Tiger', 'Nalla'])).scalar():
        db.session.add(Pet(
            name="Tiger",
            gender="M",
            breed="Dog",
            date_of_birth=date(2021, 10, 12),
            details="Good dog with spicy personality",
            price=500,
            image="https://c.wallhere.com/photos/3b/95/puppies_Corgi_dog_animals-2088671.jpg!d")
        )

        db.session.add(Pet(
            name="Nalla",
            gender="F",
            breed="Cat",
            date_of_birth=date(2022, 3, 22),
            details="Naughty cat but scares from his own shadow",
            price=450,
            image="https://c.wallhere.com/photos/37/1e/1920x1200_px_autumn_cuddly_cute_grass_Kitten_leaves-1904563.jpg!d")
        )
    db.session.commit()
