from app import db
from flask import render_template, Blueprint, flash
from app.films.models import Country, Category, Director, Film
from app.films.forms import AddFilmForm, AddDirectorForm

films = Blueprint('films', __name__, url_prefix="/films", template_folder='templates', static_folder='static')


@films.route('addFilm', methods=["POST", "GET"])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        title = form.title.data
        release_date = form.release_date.data
        country_name = form.country.data
        availability = form.availability.data.split(", ")

        print("availability", availability)

        if country_name not in db.session.query(Country.name).all():
            country = Country(name=country_name).add_country()
        else:
            country = db.session.query(Country).filter_by(name=country_name).first()

        print("release_date", release_date)

        Film(title=title, release_date=release_date, created_in_country=country,
             available_in_countries=availability).add_film()

    return render_template('films/addFilm.html')


@films.route('addDirector', methods=["POST", "GET"])
def add_director():
    form = AddDirectorForm()
    if form.validate_on_submit():
        pass
    return render_template('films/addDirector.html')
