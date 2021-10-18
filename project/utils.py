# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user
from flask_wtf import FlaskForm


def flash_errors(form: FlaskForm, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)


def seller_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated and current_user.is_shopper:
            return func(*args, **kwargs)
        else:
            flash("You must be seller to access this page !")
            return redirect(url_for("index.home"))

    return decorated_view
