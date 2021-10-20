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
    order_dict: dict = {}

    if user.is_shopper:
        orders = OrderModel.get_orders_by_shopper(user.id)
    else:
        orders = OrderModel.get_orders_by_userid(user.id)

    for order_id in orders:
        for order in orders[order_id]:
            shop_user_id: int = order.get_shop_userID()
            shopper: User = User.get_by_id(shop_user_id)
            item_id: int = order.item_id
            item: Item = Item.get_by_id(item_id)
            order.item = item

            user_id: int = order.user_id
            buyer: User = User.get_by_id(user_id)
            order.buyer = buyer

            # if shopper in orders.keys():
            #     order_dict[shopper].append(item)
            # else:
            #     order_dict[shopper] = [item]

    return render_template("shopping/order.html", order_dict=order_dict, isshopper=user.is_shopper,
                           orders=orders)
