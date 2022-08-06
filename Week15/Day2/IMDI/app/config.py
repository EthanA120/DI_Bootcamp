import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)
    # SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{os.environ['ppass']}@localhost:5432/postgres"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'users.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
