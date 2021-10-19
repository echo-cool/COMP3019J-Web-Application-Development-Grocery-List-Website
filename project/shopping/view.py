from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_user, login_required, current_user, logout_user

from project import app, db, cache
from project.models import ItemModel
from project.models.Cart import Cart
from project.models.ItemModel import Item
from project.models.UserModel import User

blueprint = Blueprint("index", __name__, static_folder="../static")


# res = {}
# for i in cart:
#     shop_user_id = i.get_shop_userID()
#     item_id = i.item_id
#     item = Item.get_by_id(item_id)
#     shopper = User.get_by_id(shop_user_id)
#     item.count = i.count
#
#     if shopper in res.keys():
#         res[shopper].append(item)
#     else:
#         res[shopper] = [item]
#
#     return render_template("shopping/shopping_cart.html", cart_dict=res)

@blueprint.route("/", methods=["GET", "POST"])
def home() -> str:
    all_items = Item.query.all()
    shop_sellers = {}
    for item in all_items:
        user_id = item.owner
        shopper = User.get_by_id(user_id)
        if shopper in shop_sellers.keys():
            shop_sellers[shopper].append(item)
        else:
            shop_sellers[shopper] = [item]

    all_items.sort(key=lambda i: i.sold_count, reverse=True)
    return render_template("shopping/index.html", items=all_items, current_user=current_user, shop_sellers=shop_sellers)


@blueprint.route("/search", methods=["GET", "POST"])
def search() -> str:
    keyword: str = request.args.get(key='keyword')
    items = Item.query.filter(Item.name.like("%" + keyword + "%")).all()
    have_res = True
    if len(items) == 0:
        have_res = False
    return render_template("shopping/search.html", have_res=have_res, items=items, current_user=current_user)


@blueprint.route("/about", methods=["GET", "POST"])
def about() -> str:
    return render_template("about/about.html")
