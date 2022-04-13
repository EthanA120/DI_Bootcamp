from app import app
from app.models import db
from sqlalchemy import exc
from app.forms import PhoneForm
from flask import render_template, redirect, url_for, session, request

db.create_all()


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

# try:
#     Expression
# except exc.IntegrityError:
#     print('Error!')
#     flash('Explanation!', 'danger')
# return redirect(url_for('function'))
