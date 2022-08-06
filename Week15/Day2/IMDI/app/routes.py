from app import app, db
from flask import render_template


@app.route('/', methods=["POST", "GET"])
def index():

    return render_template('index.html')
