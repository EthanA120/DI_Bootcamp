import json
from app import db
from sqlalchemy import exists


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(35))
    street = db.Column(db.String(35))
    city = db.Column(db.String(35))
    zipcode = db.Column(db.String(35))


def populate(clause=1):
    User.query.delete()
    with open(r"app\static\Users.json", "r") as read_file:
        json_users = json.load(read_file)

    lim = None
    for user in json_users:
        if not db.session.query(exists().where(User.name == user['name'])).scalar():
            user_row = User(name=user['name'],
                            street=user['address']['street'],
                            city=user['address']['city'],
                            zipcode=user['address']['zipcode'])
            match clause:
                case 1:
                    db.session.add(user_row)

                case 2:
                    if user['address']['city'] == "Roscoeview":
                        db.session.add(user_row)

                case 3:
                    db.session.add(user_row)
                    lim = 5

                case 4:
                    if user['address']['zipcode'][0] == "5":
                        db.session.add(user_row)

    db.session.commit()

    return User.query.limit(lim).all()
