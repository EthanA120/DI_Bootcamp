import random
from datetime import datetime, date
from app import db
from json import load
from faker import Faker
fake = Faker()


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
    # db.session.query(Pet).delete()
    with open("app/static/pets_json.json", "r") as read_file:
        jpets = load(read_file)

    for jpet in jpets:
        start_date = date(year=2007, month=1, day=1)
        if db.session.query(Pet).filter_by(name=jpet['Name']).count() == 0:
            db.session.add(Pet(
                name=jpet['Name'],
                gender=jpet['Gender'],
                breed=jpet['BreedsForDisplay'],
                date_of_birth=fake.date_between(start_date=start_date, end_date='+15y'),
                details=jpet['Story'],
                price=round(random.randint(50, 500), -1),
                image=jpet['PrimaryPhotoUrl'])
            )

    db.session.commit()
