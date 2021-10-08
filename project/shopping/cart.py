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
    return redirect(url_for('product_details.details', itemID=itemID))


@blueprint.route("/cart", methods=["GET", "POST"])
@login_required
def shopping_cart():
    user = current_user
    cart = Cart.query.filter_by(user_id=user.id).all()
    # print(cart)
    res = {}
    shopping_cart_items = []
    for i in cart:
        shop_user_id = i.get_shop_userID()
        id = i.item_id
        # print("id", id)
        item1 = Item.query.filter_by(id=id).first()
        # print("inventory: ",item1.inventory)
        # print("name: ", item1.name)
        shopping_cart_items.append(item1)
        if shop_user_id in res.keys():
            res[shop_user_id].append(Item.query.filter_by(id=id).first())
            print("shop_user_id: ", shop_user_id)
            print("i: ", i)
        else:
            res[shop_user_id] = [Item.query.filter_by(id=id).first()]
    # print(res)
    # item = Item.get_by_id(2)
    # print(item)
    for r in res:
        print("key: ", r)
        print("value: ", res[r])
    return render_template("shopping/shopping_cart.html", shopping_cart_items=shopping_cart_items, res=res)
