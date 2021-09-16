from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from app.login.forms import LoginForm, RegisterForm
from app.user.models import User
from app.utils import flash_errors

blueprint = Blueprint("login", __name__, static_folder="../static")


# @blueprint.route("/register/", methods=["GET", "POST"])
# def register():
#     """Register new user."""
#     form = RegisterForm(request.form)
#     print(form.validate_on_submit())
#     if form.validate_on_submit():
#         User.create(
#             username=form.username.data,
#             email=form.email.data,
#             password=form.password.data,
#             active=True,
#         )
#         flash("Thank you for registering. You can now log in.", "success")
#         return redirect(url_for("index.home"))
#     else:
#         flash_errors(form)
#     return render_template("login/register.html", form=form)


@blueprint.route("/login/", methods=["GET", "POST"])
def login():
    """login"""
    login_form = LoginForm(request.form)
    register_from = RegisterForm(request.form)

    print(login_form.data)
    print(register_from.data)
    if login_form.submit_login.data and login_form.validate_on_submit():
        print("Login")
        print(login_form.submit_login.data)
        print("Validate Success")
        username = login_form.username.data
        password = login_form.password.data

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
            flash_errors(login_form)

    elif register_from.submit_register.data and register_from.validate_on_submit():
        print("Register")
        print(register_from.submit_register.data)
        User.create(
            username=register_from.username.data,
            email=register_from.email.data,
            password=register_from.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("index.home"))

    else:
        flash_errors(login_form)
        flash_errors(register_from)

    return render_template("login/login_register.html", login_form=login_form, register_from=register_from)
