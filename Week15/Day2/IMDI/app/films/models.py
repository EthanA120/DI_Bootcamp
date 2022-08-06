from app import db
from datetime import datetime

many_to_many = db.Table('many_to_many',
                        db.Column('film', db.Integer, db.ForeignKey('film.id')),
                        db.Column('country', db.Integer, db.ForeignKey('country.id')),
                        db.Column('category', db.Integer, db.ForeignKey('category.id')),
                        db.Column('director', db.Integer, db.ForeignKey('director.id'))
                        )


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    film = db.relationship('Film', back_populates='country')  # One country to many films
    availability = db.relationship('Film', back_populates='available_in_countries')

    def add_country(self):
        db.session.add(self)
        db.session.commit()
        return self


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    film = db.relationship("Film", secondary=many_to_many, back_populates="category")

    def add_category(self):
        db.session.add(self)
        db.session.commit()
        return self


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    film = db.relationship("Film", secondary=many_to_many, back_populates="director")

    def add_director(self):
        db.session.add(self)
        db.session.commit()
        return self


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    release_date = db.Column(db.DateTime, default=datetime.today())
    country_id = db.Column(db.Integer, db.ForeignKey("country.id"))  # One country to many films
    country = db.relationship("Country", back_populates="film")
    available_in_countries = db.relationship("Country", secondary=many_to_many,
                                             back_populates="availability")  # Many-to-many with Country
    category = db.relationship("Category", secondary=many_to_many, back_populates="film")
    director = db.relationship("Director", secondary=many_to_many, back_populates="film")

    def add_film(self):
        db.session.add(self)
        db.session.commit()
        return self


# db.create_all()
