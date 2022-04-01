from app import app
from flask import render_template, request
from app.models import populate


@app.route("/")
@app.route("/<int:clause>")
def index(clause=1):
    users = populate(clause)
    print(users)
    return render_template('index.html', title="Home", users=users)
