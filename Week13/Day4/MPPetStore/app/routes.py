import math
from app import app
from app.forms import CartItems
from flask import render_template, redirect, url_for, flash
from app.models import db, Pet, first_pets, Cart
from sqlalchemy import exc

first_pets()

@app.route("/")
@app.route("/pets/<int:page>")
def pets(page=1, limit=20, offset=20):
    count = db.session.query(Pet).count()
    ceil = math.floor(count / limit)
    if page > ceil:
        page = ceil
    offset = (page - 1) * offset
    pet_list = db.session.query(Pet).offset(offset).limit(limit).all()
    return render_template('pets.html', title="Pets", page=page, limit=limit, offset=offset, pet_list=pet_list,
                           ceil=ceil)


@app.route("/pet/<int:pet_id>", methods=["POST", "GET"])
def pet(pet_id):
    pet_list = db.session.query(Pet).all()
    pet_detail = next(pet for pet in pet_list if pet.id == pet_id)
    form = CartItems()
    if form.validate_on_submit():
        return redirect(url_for('add_pet', pet_id=pet_id))
    return render_template('pet.html', title="Pet", pet_detail=pet_detail, form=form)


@app.route("/cart", methods=["POST", "GET"])
def cart():
    cart_list = Cart().get_cart()
    total = Cart().get_total()
    if not total:
        total = 0
    form = CartItems()
    return render_template('cart.html', title='Cart', cart_list=cart_list, form=form, total=total)


@app.route("/add_pet/<int:pet_id>", methods=["POST", "GET"])
def add_pet(pet_id):
    try:
        Cart(pet_id=pet_id).add_to_cart()
    except exc.IntegrityError:
        print('Error!')
        flash('This pet is already in your cart!', 'danger')
    return redirect(url_for('cart'))
    # Cart(pet_id=pet_id).add_to_cart()


@app.route("/remove_pet/<int:pet_id>", methods=["POST", "GET"])
def remove_pet(pet_id):
    db.session.query(Cart).filter_by(pet_id=pet_id).delete()
    db.session.commit()
    return redirect(url_for('cart'))
