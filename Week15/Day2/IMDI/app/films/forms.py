from flask_wtf import FlaskForm
from country_list import countries_for_language
from wtforms.validators import DataRequired
from wtforms import SubmitField, StringField, DateField, SelectField
from app.films.models import db, Film

films = db.session.query(Film).all()
print(films)
countries = list(dict(countries_for_language('en')).values())


class AddFilmForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    release_date = DateField('ReleaseDate', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    country = SelectField('Country', choices=countries, validators=[DataRequired()])
    director = StringField('Director', validators=[DataRequired()])
    availability = StringField('Availability')
    submit = SubmitField('AddFilm')


class AddDirectorForm(FlaskForm):
    first_name = StringField('FirstName', validators=[DataRequired()])
    last_name = StringField('LastName', validators=[DataRequired()])
    film = SelectField('Country', choices=["Atlas"], validators=[DataRequired()])
    submit = SubmitField('AddDirector')
