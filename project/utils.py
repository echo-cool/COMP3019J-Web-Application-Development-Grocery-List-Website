# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from functools import wraps

from flask import flash, redirect, url_for, session
from flask_wtf import FlaskForm

from project.models.ItemModel import Item
from project.models.UserModel import User


def flash_errors(form: FlaskForm, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)


# A decorator for checking if a user's role is a seller
def seller_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if get_current_user().is_authenticated and get_current_user().is_shopper:
            return func(*args, **kwargs)
        else:
            flash("You must be seller to access this page !")
            return redirect(url_for("index.home"))

    return decorated_view


# A decorator for checking if a user's role is a buyer
def buyer_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if get_current_user().is_authenticated and not get_current_user().is_shopper:
            return func(*args, **kwargs)
        else:
            flash("You must be buyer to access this page !")
            return redirect(url_for("index.home"))

    return decorated_view


# A decorator for checking if a product is available
# and having stock in the warehouse
def product_available_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        item_id: int = kwargs["itemID"]
        item: Item = Item.get_by_id(item_id)

        if item.disabled:
            flash("This product has been removed by the shopper and can't be viewed !")
            return redirect(url_for("index.home"))

        if item.inventory <= 0:
            flash("This product has no stock in the warehouse, you can't buy it !")

        return func(*args, **kwargs)

    return decorated_view


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session.get("USER_ID") is None:
            return func(*args, **kwargs)
        else:
            flash("You must be login to access this page !")
            return redirect(url_for("login.login"))

    return decorated_view

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if get_current_user().is_authenticated and get_current_user().is_admin:
            return func(*args, **kwargs)
        else:
            flash("Only admin can access this page !")
            return redirect(url_for("index.home"))

    return decorated_view

def logout_user():
    session.pop("USER_ID", None)



def login_user(user):
    session["USER_ID"] = user.id

def get_current_user() -> User:
    user_id = session.get("USER_ID")
    return User.get_by_id(user_id) if user_id else None
