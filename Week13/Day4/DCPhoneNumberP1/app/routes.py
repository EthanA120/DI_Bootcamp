from app import app
from app.models import db, initial_values
from app.forms import PhoneForm
from flask import render_template, redirect, url_for, session, request

db.create_all()
initial_values(50)


@app.route('/', methods=["POST", "GET"])
def index():
    form = PhoneForm()
    if request.method == 'POST':
        session['phone'] = form.phone.data
        return redirect(url_for('show_phone'))
    return render_template('index.html', form=form)


@app.route('/showphone', methods=["POST", "GET"])
def show_phone():
    return render_template('show_phone.html', phone=session['phone'])


@app.route("/person/<phonenumber>")
def owner_info():
    return render_template('owner_info.html', phone=session['phone'])


@app.route("/person/<name>")
def owner_name():
    return render_template('owner_name.html', phone=session['phone'])
