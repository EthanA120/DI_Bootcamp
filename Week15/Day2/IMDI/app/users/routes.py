import requests
from sqlalchemy import exc
from app import login_mngr
from app.users.models import db, User
from app.users.forms import RegisterForm, LoginForm
from flask import render_template, redirect, url_for, flash, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import current_user, login_user, login_required, logout_user


users = Blueprint('users', __name__, url_prefix="/users", template_folder='templates', static_folder='static')

@login_mngr.user_loader
def load_user(userid):
    userid = int(userid)
    return db.session.query(User).get(userid)


@users.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if not db.session.query(User).filter_by(email=form.email.data).first():
            try:
                player = User(username=form.user_name.data, email=form.email.data,
                              password=generate_password_hash(form.password.data))
                player.add_user()
                return redirect(url_for('users.login'))

            except exc.IntegrityError:
                flash('Username or email are already in use, please try again.', 'warning')

    return render_template('loginRegister/register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()

        if user is None or not check_password_hash(user.password, form.password.data):
            flash('Invalid username or password.', 'warning')
            return redirect(url_for('users.login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('loginRegister/login.html', form=form)

import app.users.google

@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))
