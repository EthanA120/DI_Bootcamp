# from app import app
# from random import choice
# from app.forms import AddCity
# from string import ascii_letters
# from flask import render_template, redirect
#
# app.config["SECRET_KEY"] = ''.join(choice(ascii_letters) for i in range(256))
# print("Random password is:", app.config["SECRET_KEY"])
#
#
# @app.route("/", methods=["GET", "POST"])
# def index():
#     form = AddCity()
#
#     if form.validate_on_submit():
#         name = form.name.data
#         country = form.country.data
#         inhabitants = form.inhabitants.data
#         area = form.area.data
#         print(name, country, inhabitants, area)
#         return redirect("/")
#
#     return render_template('index.html', title="Home", form=form)
