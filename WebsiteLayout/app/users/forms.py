from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms import SubmitField, StringField, PasswordField, BooleanField


class RegisterForm(FlaskForm):
    user_name = StringField('UserName', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])
    confirm_pass = PasswordField('ConfirmPassword', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')