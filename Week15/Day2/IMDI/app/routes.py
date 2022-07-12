from sqlalchemy import exc
from app import app, login_mngr
from app.forms import RegisterForm, LoginForm
from app.models import db, User
from flask import render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import current_user, login_user, login_required, logout_user


@login_mngr.user_loader
def load_user(userid):
    userid = int(userid)
    return db.session.query(User).get(userid)


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template('index.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        if not db.session.query(User).filter_by(email=form.email.data).first():
            try:
                player = User(username=form.user_name.data, email=form.email.data,
                              password=generate_password_hash(form.password.data))
                player.add_user()
                return redirect(url_for('login'))

            except exc.IntegrityError:
                flash('Username or email are already in use, please try again.', 'warning')

    return render_template('loginRegister/register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()

        if user is None or not check_password_hash(user.password, form.password.data):
            flash('Invalid username or password.', 'warning')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('loginRegister/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
