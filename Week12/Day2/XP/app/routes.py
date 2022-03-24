import random
import string
from app import app
from flask import render_template

characters = string.ascii_letters + string.digits + string.punctuation
rnd_pass = ''.join(random.choice(characters) for i in range(8))
print("Random password is:", rnd_pass)


@app.route("/")
def layout():
    return render_template('index.html', posts=posts)
