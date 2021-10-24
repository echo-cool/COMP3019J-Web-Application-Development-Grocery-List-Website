# -*- coding: utf-8 -*-
"""User views."""
import os
from urllib import request

from flask import Blueprint, render_template, flash, redirect, url_for, current_app, Response
from flask_login import login_required, current_user, logout_user

from project.models.UserModel import User
from project.user.forms import UpdateUser
from project.utils import flash_errors

blueprint = Blueprint("user", __name__, static_folder="../static")


@blueprint.route("/user/info", methods=["GET", "POST"])
@login_required
def info() -> str:
    form: UpdateUser = UpdateUser()
    user: User = current_user
    if form.validate_on_submit():
        new_username: str = form.username.data
        new_email: str = form.email.data
        new_password: str = form.password.data
        new_main_image = form.image_file.data
        if new_main_image.filename != "":
            filename = str(os.urandom(30).hex()) + "." + new_main_image.filename.split(".")[-1];
            new_main_image.save(os.path.join(current_app.static_folder, 'uploaded_files', filename))

        user.username = new_username
        user.email = new_email
        if new_password != "":
            user.set_password(new_password)

        if new_main_image.filename != "":
            user.main_image_url = "static/uploaded_files/" + filename

        user.save()
        flash("Update Success !")
    flash_errors(form)
    return render_template("userinfo/userinfo.html", current_user=current_user, form=form)


@blueprint.route('/user/change_password')
@login_required
def change_password() -> Response:
    new_password: str = request.form.get('new_password')
    user: User = current_user
    user.set_password(new_password)
    logout()
    flash("Set Password successfully, Please Login again !")
    return redirect(url_for('index.home'))


@blueprint.route('/user/change_username')
@login_required
def change_username() -> Response:
    new_username: str = request.form.get('new_username')
    user: User = current_user
    user.username = new_username
    user.save()
    flash("Your new username is " + new_username)
    return redirect(url_for('index.home'))


@blueprint.route('/user/logout')
@login_required
def logout() -> Response:
    logout_user()
    flash('See you later！')
    return redirect(url_for('index.home'))
