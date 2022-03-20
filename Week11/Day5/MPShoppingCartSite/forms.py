from flask_wtf import FlaskForm
from wtforms import SubmitField


class CartItems(FlaskForm):
    add_to_cart = SubmitField('Add to cart')
    remove_from_cart = SubmitField('Remove From Cart')


