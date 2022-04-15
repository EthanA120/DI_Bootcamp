from app import db
from faker import Faker
from random import randint, choices


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(60), unique=True)
    phonenumbers = db.relationship("PhoneNumber", back_populates="person")
    address = db.Column(db.String(60))


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(60))
    owner = db.Column(db.Integer, db.ForeignKey('person.id'))
    person = db.relationship("Person", back_populates="phonenumbers", uselist=False)


def initial_values(amount=10):
    if db.session.query(Person).count() < amount and db.session.query(PhoneNumber).count() < amount:
        amount -= db.session.query(Person).count()
        fake = Faker()

        for num in range(amount):
            full_name = fake.unique.name()
            if db.session.query(Person).filter_by(name=full_name).count() == 0:
                owner = Person(
                    name=full_name,
                    email=fake.ascii_safe_email(),
                    address=fake.address()
                )
                db.session.add(owner)
            else:
                continue

            for count in range(choices([1, 2, 3], weights=[10, 4, 1], k=1)[0]):
                phone_number = fake.unique.phone_number()
                if db.session.query(PhoneNumber).filter_by(number=phone_number).count() == 0:
                    db.session.add(PhoneNumber(number=phone_number, person=owner))
                else:
                    count -= count

        db.session.commit()
