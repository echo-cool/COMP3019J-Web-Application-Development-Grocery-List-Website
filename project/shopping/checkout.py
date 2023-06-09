from flask import Blueprint, Response
from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from sqlalchemy import null

from project import app, db
from project.models import ItemModel
from project.models.CartModel import Cart
from project.models.ItemModel import Item
from project.models.OrderModel import Order
from project.models.UserModel import User
from project.utils import login_required, get_current_user

blueprint = Blueprint("checkout", __name__, static_folder="../static")


# This is to handle checkout_confirm action
@blueprint.route("/checkout/confirm", methods=["GET", "POST"])
@login_required
def checkout_confirm() -> str:
    user: User = get_current_user()
    cart: Cart = Cart.query.filter_by(user_id=user.id).all()
    res: dict = {}
    total_price: int = 0
    for i in cart:
        shop_user_id: int = i.get_shop_userID()
        item_id: int = i.item_id
        item: Item = Item.get_by_id(item_id)
        shopper: User = User.get_by_id(shop_user_id)
        item.count = i.count
        total_price += item.price * i.count

        if shopper in res.keys():
            res[shopper].append(item)
        else:
            res[shopper] = [item]

    return render_template("shopping/checkout.html", cart_dict=res, total_price=total_price,
                           current_user=get_current_user())


# def do_create_order():
#     pass
#
#
# def do_clear_cart():
#     pass

# This is to handle the pay action
@blueprint.route("/checkout/pay", methods=["GET", "POST"])
@login_required
def checkout_pay() -> str:
    user: User = get_current_user()
    # Get all cart items
    cart: list[Cart] = Cart.query.filter_by(user_id=user.id).all()
    res: dict = {}
    total_price: int = 0
    full_order_status = True
    for i in cart:
        shop_user_id: int = i.get_shop_userID()
        item_id: int = i.item_id
        item: Item = Item.get_by_id(item_id)
        shopper: User = User.get_by_id(shop_user_id)
        item.count = i.count
        total_price += item.price * i.count

        if shopper in res.keys():
            res[shopper].append(item)
        else:
            res[shopper] = [item]

    if request.method == "POST":
        pay_now: bool = request.form.get('pay_now')
        # do pay
        pay_status = True
        if pay_status:
            # do_create_order()
            newest: Order = Order.query.order_by(db.desc(Order.order_id)).first()
            if newest is None:
                order_id_count = 0
            else:
                order_id_count = newest.order_id + 1
            for i in cart:
                tmp_item: Item = Item.get_by_id(i.item_id)
                if tmp_item.inventory - i.count < 0:
                    full_order_status = False
                else:
                    # reduce inventory and add sold count
                    tmp_item.inventory -= i.count
                    tmp_item.sold_count += i.count
                    tmp_item.save()
                    Order.create(
                        order_id=order_id_count,
                        count=i.count,
                        item_id=i.item_id,
                        user_id=i.user_id,
                    )
                    # do_clear_cart()
                    i.delete()
            # Check if a order is fully succeed
            if full_order_status:
                flash("Order successfully done !")
            else:
                flash("Some items were failed to be ordered, because the shopper dose not have enough inventory.")
            return render_template("shopping/pay.html", pay_status=pay_status, total_price=total_price,
                                   full_order_status=full_order_status, current_user=get_current_user())
        else:
            return render_template("shopping/pay.html", pay_status=pay_status, total_price=total_price,
                                   full_order_status=full_order_status, current_user=get_current_user())
    else:
        return render_template("shopping/pay.html", pay_status=False, total_price=total_price, current_user=get_current_user())
