from app.config import Config
from datetime import timedelta
from flask import Flask, session
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

# from flask_ngrok import run_with_ngrok

app = Flask(__name__, template_folder='templates', static_folder='static')
# run_with_ngrok(app, '296WTGEAyc728DZUXkdEpIQ4S2x_7Q7q7KVMNfKkaqAJyvb5f')

app.config.from_object(Config)
bootstrap = Bootstrap5(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.before_first_request  # runs before FIRST request (only once)
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=1)


login_mngr = LoginManager(app)
login_mngr.login_view = 'login'

from app import routes
from app.users.routes import users
from app.films.routes import films

app.register_blueprint(users)
app.register_blueprint(films)
