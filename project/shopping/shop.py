from flask import Blueprint
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from project import app
from project.models import ItemModel
from project.models.CartModel import Cart
from project.models.ItemModel import Item
from project.models.UserModel import User

blueprint = Blueprint("shop", __name__, static_folder="../static")

# View a specific a shop
@blueprint.route("/shop/<int:userID>", methods=["POST", "GET"])
def shop(userID: int) -> str:
    # find all items
    items = Item.query.filter_by(owner=userID, disabled=False).all()
    return str(len(items))

