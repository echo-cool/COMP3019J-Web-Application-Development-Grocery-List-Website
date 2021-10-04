# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required, current_user

blueprint = Blueprint("user", __name__, static_folder="../static")


@blueprint.route("/userinfo")
@login_required
def members():
    """List members."""
    return render_template("userinfo/userinfo.html", current_user=current_user)
