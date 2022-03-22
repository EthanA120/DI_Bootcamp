from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UserDetails(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    hobbies = StringField('Hobbies', validators=[DataRequired()])
    skills = StringField('Skills', validators=[DataRequired()])
    strengths = StringField('Strengths', validators=[DataRequired()])
    weaknesses = StringField('Weaknesses', validators=[DataRequired()])
    submit = SubmitField('Create Form')


