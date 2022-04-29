from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    details = db.Column(db.String(500))
    completed = db.Column(db.Boolean(), default=False)
    image = db.relationship('Image', backref='todo', uselist=False)

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(500))
    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'), unique=True)
