from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for
)

from project.login.forms import LoginForm, RegisterForm
from project.models.UserModel import User
from project.utils import flash_errors, login_user, get_current_user

blueprint = Blueprint("login", __name__, static_folder="../static")


# This is the login handler when user wants to login
@blueprint.route("/login/", methods=["GET", "POST"])
def login():
    """login functionality"""
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
            # Check user's password
            if user.check_password(password):
                # Password correct, login
                login_user(user)
                flash("Login Success", "success")
                return redirect(url_for("index.home"))
            else:
                flash("Wrong password", "warning")
        else:
            flash("User not exist", "warning")
            # flash_errors(login_form)
    # The submitted form is register
    elif register_from.submit_register.data and register_from.validate_on_submit():
        print("Register")
        print(register_from.submit_register.data)
        # New user
        User.create(
            username=register_from.username.data,
            email=register_from.email.data,
            password=register_from.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.")
        return redirect(url_for("index.home"))

    else:
        # if there is errors in the form, flash it.
        flash_errors(login_form)
        flash_errors(register_from)

    return render_template("login/login_register.html", login_form=login_form, register_from=register_from,
                           current_user=get_current_user())


# this is used for users to restore their passwords
@blueprint.route("/restore_password/", methods=["GET", "POST"])
def restore_password():
    return render_template("login/restore_password.html",
                           current_user=get_current_user())
