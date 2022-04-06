from app import app
from flask import render_template, flash, redirect, url_for
from app.models import db, Pet, first_pets


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title="Home")


@app.route("/pets")
def pets():
    return render_template('pets.html', title="Pets")


@app.route("/pet/<int:pet_id>")
def pet(pet_id):
    return render_template('pet.html', title="Pet")


@app.route("/cart")
def cart():
    return render_template('cart.html', title="Cart")
