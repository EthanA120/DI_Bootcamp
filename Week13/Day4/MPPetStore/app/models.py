import random

from app import db
from json import load
from faker import Faker
from sqlalchemy import func
from datetime import datetime, date

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
    cart = db.relationship('Cart', backref='pet')


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_id = db.Column(db.Integer(), db.ForeignKey('pet.id'))

    def add_to_cart(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_cart(cls):
        return db.session.query(cls).all()

    def get_total(self):
        return db.session.query(func.sum(Pet.price)).filter(Pet.id == Cart.pet_id).all()[0][0]


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


db.create_all()
