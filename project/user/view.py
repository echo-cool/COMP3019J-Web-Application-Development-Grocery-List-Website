# -*- coding: utf-8 -*-
"""User views."""
from urllib import request

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user

blueprint = Blueprint("user", __name__, static_folder="../static")


@blueprint.route("/user/info")
@login_required
def info():
    return render_template("userinfo/userinfo.html", current_user=current_user)


@blueprint.route('/user/change_password')
@login_required
def change_password():
    new_password = request.form.get('new_password')
    user = current_user
    user.set_password(new_password)
    logout()
    flash("Set Password successfully, Please Login again !")
    return redirect(url_for('index.home'))


@blueprint.route('/user/change_username')
@login_required
def change_username():
    new_username = request.form.get('new_username')
    user = current_user
    user.username = new_username
    user.save()
    flash("Your new username is " + new_username)
    return redirect(url_for('index.home'))


@blueprint.route('/user/logout')
@login_required
def logout():
    logout_user()
    flash('See you later！')
    return redirect(url_for('index.home'))
