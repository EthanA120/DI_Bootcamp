from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class AddCity(FlaskForm):
    name = StringField("City's name", validators=[DataRequired(), Length(max=15)])
    country = StringField("City's Country", validators=[DataRequired()])
    inhabitants = IntegerField("Number of inhabitants", validators=[DataRequired()])
    area = IntegerField("Area [squared km]")
    submit = SubmitField("Submit")
