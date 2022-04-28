from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.String(240))
    completed = db.Column(db.Boolean(), default=False)

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()
