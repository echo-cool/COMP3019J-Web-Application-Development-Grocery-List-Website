# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    redirect,
    render_template,
    request, flash,
)
from app.extensions import db
from app.index.forms import AddTaskFrom
from app.index.model import Todo
from app.utils import flash_errors

blueprint = Blueprint("index", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    form = AddTaskFrom()
    if form.validate_on_submit():
        task_content = form.content.data
        new_task = Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "Error"
    else:
        flash_errors(form)
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

@blueprint.route("/about/")
def about():
    """About page."""
    return render_template("about.html")
