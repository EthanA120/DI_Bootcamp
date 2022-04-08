import math
from app import app
from flask import render_template, flash, redirect, url_for
from app.models import db, Pet, first_pets

first_pets()


@app.route("/")
@app.route("/pets/<int:page>")
def pets(page=1, limit=20, offset=20):
    count = db.session.query(Pet).count()
    ceil = math.floor(count / limit)
    if page > ceil:
        page = ceil
    offset = (page-1) * offset
    pet_list = db.session.query(Pet).offset(offset).limit(limit).all()
    return render_template('pets.html', title="Pets", page=page, limit=limit, offset=offset, pet_list=pet_list, ceil=ceil)


@app.route("/pet/<int:pet_id>")
def pet(pet_id):
    pet_list = db.session.query(Pet).all()
    pet_detail = next(pet for pet in pet_list if pet.id == pet_id)
    return render_template('pet.html', title="Pet", pet_detail=pet_detail)


@app.route("/cart")
def cart():
    return render_template('cart.html', title="Cart")
