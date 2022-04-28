from app import app
from app.models import db, Todo
from app.forms import TaskForm, ClearForm
from flask import render_template, redirect, url_for, session, request, flash

db.create_all()


@app.route('/', methods=["POST", "GET"])
def index():
    form = TaskForm()
    clear_form = ClearForm()

    tasks = db.session.query(Todo).all()

    if request.method == 'POST':
        if form.submit.data:
            Todo(details=form.task.data).save_task_to_db()

        if clear_form.clear.data:
            db.session.query(Todo).delete()
            db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html', form=form, clear_form=clear_form, tasks=tasks)


@app.route('/remove/<task_id>', methods=["POST", "GET"])
def remove(task_id):
    db.session.query(Todo).filter(Todo.id == task_id).delete()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/done/<task_id>', methods=["POST", "GET"])
def task_done(task_id):
    task = db.session.query(Todo).get(task_id)
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    db.session.commit()
    return redirect(url_for('index'))
