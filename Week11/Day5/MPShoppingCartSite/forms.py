from flask_wtf import FlaskForm
from wtforms import validators, IntegerField, SubmitField


class AddItem(FlaskForm):
    quantity = IntegerField('Quantity', validators=[validators.DataRequired()])
    submit = SubmitField('Add')

