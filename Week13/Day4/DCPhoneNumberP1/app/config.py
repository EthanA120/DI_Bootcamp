import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "slkjfnvajhtvnlkjdhrtgvlksd"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'phone.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
