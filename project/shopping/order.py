from flask import Blueprint, Response
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_user, login_required, current_user, logout_user
from sqlalchemy import null

from project import app, db
from project.models import ItemModel, OrderModel
from project.models.Cart import Cart
from project.models.ItemModel import Item
from project.models.OrderModel import Order
from project.models.UserModel import User

blueprint = Blueprint("order", __name__, static_folder="../static")

@blueprint.route("/order/view", methods=["GET", "POST"])
@login_required
def view_order():
    user: User = current_user
    if user.is_shopper:
        orders = OrderModel.get_orders_by_shopper(user.id)
        return render_template("shopping/order.html", orders=orders, isshopper=user.is_shopper)
    else:
        orders = OrderModel.get_orders_by_userid(user.id)
        return render_template("shopping/order.html", orders=orders, isshopper=user.is_shopper)

