# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from functools import wraps

from flask import flash, redirect, url_for
from flask_login import current_user
from flask_wtf import FlaskForm

from project.models.ItemModel import Item


def flash_errors(form: FlaskForm, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)

# A decorator for checking if a user's role is a seller
def seller_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated and current_user.is_shopper:
            return func(*args, **kwargs)
        else:
            flash("You must be seller to access this page !")
            return redirect(url_for("index.home"))

    return decorated_view

# A decorator for checking if a user's role is a buyer
def buyer_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_user.is_authenticated and not current_user.is_shopper:
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
