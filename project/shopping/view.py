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

blueprint = Blueprint("index", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    all_items = Item.query.all()
    return render_template("shopping/index.html", items=all_items, current_user=current_user)


@blueprint.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")


@blueprint.route("/product_details/<int:itemID>", methods=["GET", "POST"])
def details(itemID):
    item = Item.get_by_id(itemID)
    return render_template("shopping/product_details.html", item=item)


@blueprint.route("/add_to_cart", methods=["POST"])
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
    return redirect(url_for('index.details', itemID=itemID))


@blueprint.route("/shopping_cart", methods=["GET", "POST"])
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
        shopping_cart_items.append(item1)
        if shop_user_id in res.keys():
            res[shop_user_id].append(i)
        else:
            res[shop_user_id] = [i]
    # print(res)
    item = Item.get_by_id(2)
    print(item)
    return render_template("shopping/shopping_cart.html", shopping_cart_items=shopping_cart_items, item=item)


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('See you later！')
    return redirect(url_for('index.home'))
