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

blueprint = Blueprint("shop", __name__, static_folder="../static")


@blueprint.route("/shop/<int:userID>", methods=["POST", "GET"])
def shop(userID):
    items = Item.query.filter_by(owner=userID).all()
    return str(len(items))
