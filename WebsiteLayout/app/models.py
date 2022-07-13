from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    def add_user(self):
        db.session.add(self)
        db.session.commit()


# db.create_all()
# User(username="Ethan", email="Ethan@Gmail.com", password='123456').add_user()
