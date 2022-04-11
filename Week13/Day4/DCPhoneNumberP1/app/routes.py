from app import app
from flask import render_template, redirect, url_for, session
from app.forms import PhoneForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PhoneForm()
    if form.validate_on_submit():
        session['phone'] = form.phone.data
        return redirect(url_for('show_phone'))
    return render_template('index.html', form=form)


@app.route('/showphone')
def show_phone():
    return render_template('show_phone.html', phone=session['phone'])
