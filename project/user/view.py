# -*- coding: utf-8 -*-
"""User views."""
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
    return redirect(url_for('index.home'))


@blueprint.route('/user/change_userinfo')
@login_required
def change_userinfo():
    return redirect(url_for('index.home'))


@blueprint.route('/user/logout')
@login_required
def logout():
    logout_user()
    flash('See you later！')
    return redirect(url_for('index.home'))
