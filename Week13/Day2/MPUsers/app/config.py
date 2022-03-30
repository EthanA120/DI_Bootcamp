import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "slkjfnvajhtvnlkjdhrtgvlksd"
    db_info = {'host': 'localhost',
               'database': 'bookstore',
               'user': 'postgres',
               'port': ''}
    SQLALCHEMY_DATABASE_URI = f"postgresql://{db_info['user']}:{os.environ['GENERAL']}@{db_info['host']}/{db_info['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
