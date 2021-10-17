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

blueprint = Blueprint("cart", __name__, static_folder="../static")


@blueprint.route("/cart/remove", methods=["GET", "POST"])
@login_required
def remove_from_cart():
    itemID = request.form.get('itemID')
    print(itemID)
    user = current_user
    cart_entry = Cart.query.filter_by(item_id=itemID, user_id=user.id).first()
    if cart_entry:
        cart_entry.delete()
    flash("Removed Successfully")


@blueprint.route("/cart/add", methods=["POST"])
@login_required
def add_to_cart():
    itemID = request.form.get('itemID')
    itemCount = request.form.get('itemCount')
    user = current_user
    item = Item.get_by_id(itemID)
    cart_entry = Cart.query.filter_by(item_id=itemID, user_id=user.id).first()
    if cart_entry:
        current_count = cart_entry.count
        cart_entry.update(
            count=int(current_count) + int(itemCount)
        )
    else:
        Cart.create(
            item_id=itemID,
            user_id=user.id,
            count=itemCount
        )

    flash("Successfully added " + str(itemCount) + " " + str(item.name) + " to your cart !")
    return redirect(url_for('item.details', itemID=itemID))


@blueprint.route("/cart", methods=["GET", "POST"])
@login_required
def shopping_cart():
    user = current_user
    cart = Cart.query.filter_by(user_id=user.id).all()
    res = {}
    for i in cart:
        shop_user_id = i.get_shop_userID()
        item_id = i.item_id
        item = Item.get_by_id(item_id)
        shopper = User.get_by_id(shop_user_id)
        item.count = i.count

        if shopper in res.keys():
            res[shopper].append(item)
        else:
            res[shopper] = [item]

    return render_template("shopping/shopping_cart.html", cart_dict=res)
