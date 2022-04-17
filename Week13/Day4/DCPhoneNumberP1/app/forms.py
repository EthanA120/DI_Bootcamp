import phonenumbers
from flask_wtf import FlaskForm
from wtforms import SubmitField, TelField, StringField
from wtforms.validators import DataRequired, ValidationError


class PhoneForm(FlaskForm):
    phone = TelField('Phone', validators=[DataRequired()])
    submit = SubmitField('Submit')

    @staticmethod
    def validate_phone(phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')


class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    name_submit = SubmitField('Submit')
