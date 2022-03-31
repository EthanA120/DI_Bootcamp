from app import db
from json import load


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35))
    street = db.Column(db.String(35))
    city = db.Column(db.String(35))
    zipcode = db.Column(db.String(35))

def populate():
    with open("app/static/users.json", "r") as read_file:
        json_users = load(read_file)
    for user in json_users:
        db.session.add(User(name=user['name'], street=user['address']['street'], city=user['address']['city'], zipcode=user['address']['zipcode']))
    db.session.commit()

    return User.query.all()
