from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from app.user.forms import LoginForm, RegisterForm
from app.user.models import User
from app.utils import flash_errors

blueprint = Blueprint("login", __name__, static_folder="../static")


@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("index.home"))
    else:
        flash_errors(form)
    return render_template("login/register.html", form=form)


@blueprint.route("/login/", methods=["GET", "POST"])
def login():
    """login"""
    form = LoginForm(request.form)
    if form.validate_on_submit():
        print("Validate Success")
        username = form.username.data
        password = form.password.data

        print(username, password)
        user = User.query.filter_by(username=username).first()
        if user:
            if user.check_password(password):
                flash("Login Success", "success")
                return redirect(url_for("index.home"))
            else:
                flash("Wrong password", "warning")
        else:
            flash("User not exist", "warning")
            flash_errors(form)
    else:
        flash_errors(form)
    return render_template("login/login.html", form=form)
