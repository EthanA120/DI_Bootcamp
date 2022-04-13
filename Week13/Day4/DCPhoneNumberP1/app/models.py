from app import db
from json import load
from faker import Faker
from sqlalchemy import func
from datetime import datetime, date

fake = Faker()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(60), unique=True)
    phonenumbers = db.relationship('Phonenumber', backref='person')
    address = db.Column(db.String(60))


class Phonenumber(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(60))
    owner = db.Column(db.ForeignKey('person.id'), unique=True)
