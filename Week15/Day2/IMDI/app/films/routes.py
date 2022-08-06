from unicodedata import category
from app import db
from flask import redirect, render_template, Blueprint, flash, url_for
from app.films.models import Country, Category, Director, Film
from app.films.forms import AddFilmForm, AddDirectorForm

films = Blueprint('films', __name__, url_prefix="/films", template_folder='templates', static_folder='static')


@films.route('addFilm', methods=["POST", "GET"])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        title = form.title.data
        release_date = form.release_date.data
        categories = form.category.data
        country = form.country.data
        directors = form.director.data
        availability = form.availability.data

        categories = categories.split(", ") if ", " in categories else [categories]
        directors = directors.split(", ") if ", " in directors else [directors]
        availability = availability.split(", ") if ", " in availability else [availability]

        country_name = db.session.query(Country).filter_by(name=country).first()
        if country_name:
            country = country_name
        else:
            country = Country(name=country).add_country()

        for i, available_country in enumerate(availability):
            country_name = db.session.query(Country).filter_by(name=available_country).first()
            if country_name:
                availability[i] = country_name
            else:
                availability[i] = Country(name=available_country).add_country()

        for i, category in enumerate(categories):
            category_name = db.session.query(Category).filter_by(name=category).first()
            if category_name:
                categories[i] = category_name
            else:
                categories[i] = Category(name=category).add_category()

        for i, director in enumerate(directors):
            director_name = db.session.query(Director).filter_by(name=director).first()
            if director_name:
                directors[i] = director_name
            else:
                directors[i] = Director(name=director).add_director()

        print("title:", title)
        print("release_date:", release_date)
        print("categories:", categories)
        print("country:", country)
        print("directors:", directors)
        print("availability:", availability)

        film = Film(title=title, release_date=release_date, category=categories, country=country,
                    director=directors, available_in_countries=availability).add_film()

        country.film = [film]
        for category in categories:
            category.film = [film]
            print(category.film[0].title)
        for director in directors:
            director.film = [film]

        return redirect(url_for('index'))

    return render_template('films/addFilm.html', form=form)


@films.route('addDirector', methods=["POST", "GET"])
def add_director():
    form = AddDirectorForm()
    if form.validate_on_submit():
        pass
    return render_template('films/addDirector.html', form=form)
