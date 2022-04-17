from app import app
from app.models import db, initial_values, Person, PhoneNumber
from app.forms import PhoneForm, NameForm
from flask import render_template, redirect, url_for, session, request, flash

db.create_all()
initial_values(50)


@app.route('/', methods=["POST", "GET"])
def index():
    phone_form = PhoneForm()
    name_form = NameForm()

    if request.method == 'POST':
        if phone_form.phone.data and len(phone_form.phone.data) > 0:
            session['full_phone'] = phone_form.phone.data
            session['phone'] = session['full_phone'].split("-")[1]
            return redirect(url_for('show_phone', phonenumber=session['phone']))

        elif name_form.name.data and len(name_form.name.data) > 0:
            session['name'] = name_form.name.data.title()
            return redirect(url_for('owner_name', name=session['name']))

    return render_template('index.html', phone_form=phone_form, name_form=name_form)


@app.route('/person/<phonenumber>', methods=["POST", "GET"])
def show_phone(phonenumber):
    phone_db = [value for (value,) in db.session.query(PhoneNumber.number).all()]
    print(phone_db)
    if phonenumber in phone_db:
        phone = db.session.query(PhoneNumber).filter_by(number=phonenumber).all()[0]
        owner = db.session.query(Person).filter_by(id=phone.owner).all()[0]

    else:
        flash('There is no such phone number in our data base', 'danger')
        return redirect(url_for('index'))

    return render_template('show_phone.html', full_phone=session['full_phone'], owner=owner)


@app.route("/persona/<name>", methods=["POST", "GET"])
def owner_name(name):
    name_list = [value for (value,) in db.session.query(Person.name).all()]
    if name in name_list:
        owner = db.session.query(Person).filter_by(name=name).all()[0]
        phone = db.session.query(PhoneNumber).filter_by(owner=owner.id).all()[0]
        phone_number = phone.number

    else:
        flash('There is no such name in our data base', 'danger')
        return redirect(url_for('index'))
    return render_template('owner_name.html', owner=owner, phone_number=phone_number)
