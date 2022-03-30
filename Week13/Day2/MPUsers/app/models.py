from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35))
    street = db.Column(db.String(35))
    city = db.Column(db.String(35))
    zipcode = db.Column(db.String(35))

