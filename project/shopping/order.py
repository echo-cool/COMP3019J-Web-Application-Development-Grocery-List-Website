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
from project.utils import seller_required, buyer_required

blueprint = Blueprint("order", __name__, static_folder="../static")


@blueprint.route("/order/view", methods=["GET", "POST"])
@login_required
def view_order():

    user: User = current_user
    total_price: dict = {}
    order_dict: dict = {}

    if user.is_shopper:
        orders = OrderModel.get_orders_by_shopper(user.id)
    else:
        orders = OrderModel.get_orders_by_userid(user.id)

    for order_id in orders:
        tmp_price = 0
        for order in orders[order_id]:
            shop_user_id: int = order.get_shop_userID()
            item_id: int = order.item_id
            item: Item = Item.get_by_id(item_id)
            order.item = item
            user_id: int = order.user_id
            buyer: User = User.get_by_id(user_id)
            shopper: User = User.get_by_id(shop_user_id)
            order.buyer = buyer
            order.shopper = shopper
            tmp_price += item.price * order.count

            order.status = "Not Confirmed"
            if order.is_confirmed_by_shopper:
                order.status = "Confirmed By Shopper"
            if order.is_confirmed_delivery:
                order.status = "Confirmed Delivered"
        total_price[order_id] = tmp_price

    return render_template("shopping/order.html", order_dict=order_dict, isshopper=user.is_shopper,
                           orders=orders, total_price=total_price)


@blueprint.route("/order/shopper_confirm/<int:order_id>", methods=["GET", "POST"])
@login_required
@seller_required
def shopper_confirm_order(order_id):
    orders = OrderModel.get_order_items_by_id(order_id)
    for order in orders:
        if order.shopper_id == current_user.id:
            order.is_confirmed_by_shopper = True
            order.save()

    flash("Order Confirmed Successfully !")
    return redirect(url_for("order.view_order"))


@blueprint.route("/order/buyer_confirm/<int:order_id>", methods=["GET", "POST"])
@login_required
@buyer_required
def buyer_confirm_order(order_id):
    orders = OrderModel.get_order_items_by_id(order_id)
    for order in orders:
        if order.user_id == current_user.id:
            order.is_confirmed_delivery = True
            order.save()

    flash("Order Confirmed Successfully !")
    return redirect(url_for("order.view_order"))
