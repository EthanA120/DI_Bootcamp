from app import app
from flask import render_template, flash, redirect, url_for
from app.models import populate
from app.forms import Login


@app.route("/")
@app.route("/<int:clause>")
def index(clause=1):
    users = populate(clause)
    return render_template('index.html', title="Home", users=users)


@app.route("/login", methods=["GET", "POST"])
def login():
    users = {user.name: user.city for user in populate()}
    form = Login()
    if form.validate_on_submit():
        name = form.name.data.title()
        city = form.city.data.title()
        print(name, city)
        if not name.istitle() or not city.istitle():
            flash(f"Sorry, you have used some prohibited letters, please use only alphabet latin letters", "danger")
            return redirect(url_for("login"))

        elif name.title() in users and city.title() == users[name]:
            flash(f"Welcome {name}, you are now logged in", "success")
            return redirect(url_for("index"))

        elif name.title() not in users or (name.title() in users and not city.title() == users[name]):
            flash(f"Sorry {name}, you are not registered", "warning")
            return redirect(url_for("login"))

    return render_template('login.html', title="Login", form=form)
