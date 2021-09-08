# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from extensions import login_manager, db
from index.forms import AddTaskFrom
from index.model import Todo

blueprint = Blueprint("public", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = AddTaskFrom()
    if request.method == 'POST':
        task_content = form.content.data
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "Error"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks, form=form)


@blueprint.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "ERROR"


@blueprint.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)
    form = AddTaskFrom(request.form)
    if request.method == "POST":
        task.content = form.content.data
        try:
            db.session.commit()
            return redirect("/")
        except Exception:
            return "Error"
    else:
        return render_template("update.html", task=task, form=form)
