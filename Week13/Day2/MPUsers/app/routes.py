from app import app
from flask import render_template
from app.models import populate


@app.route("/")
def index():
    users = populate()
    print(users)
    return render_template('index.html', title="Home", users=users)
