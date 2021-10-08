from flask import Blueprint
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_user, login_required, current_user, logout_user

from project import app
from project.models import ItemModel
from project.models.Cart import Cart
from project.models.ItemModel import Item
from project.models.UserModel import User

blueprint = Blueprint("product_details", __name__, static_folder="../static")


@blueprint.route("/product_details/<int:itemID>", methods=["GET", "POST"])
def details(itemID):
    item = Item.get_by_id(itemID)
    return render_template("shopping/product_details.html", item=item)
