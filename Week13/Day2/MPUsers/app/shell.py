from app import app, db
from app.models import User


def get_users():
    users = User.query.all()
    return [user.username for user in users]


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'all_usernames': get_users()}
