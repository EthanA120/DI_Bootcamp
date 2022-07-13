from flask import Flask
from app.config import Config
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

login_mngr = LoginManager(app)
login_mngr.login_view = 'login'

from app import routes
