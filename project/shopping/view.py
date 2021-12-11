from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for, jsonify,
)

from project import app, db
from project.models import ItemModel
from project.models.AnnouncementModel import Announcement
from project.models.CartModel import Cart
from project.models.ItemModel import Item
from project.models.UserModel import User
from project.utils import get_current_user

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
# This is the main index page
@blueprint.route("/", methods=["GET", "POST"])
def home() -> str:
    # Find all items that are not disabled
    all_items = Item.query.filter_by(disabled=False).all()
    shop_sellers = {}
    # Find all announcements in the database
    announcements = Announcement.query.all()
    announcements = [i.content.split(" ") for i in announcements]
    # announcement: Announcement = Announcement.get_by_id(0)
    for item in all_items:
        user_id = item.owner
        shopper = User.get_by_id(user_id)
        if shopper in shop_sellers.keys():
            shop_sellers[shopper].append(item)
        else:
            shop_sellers[shopper] = [item]

    all_items.sort(key=lambda i: i.sold_count, reverse=True)
    return render_template("shopping/index.html", items=all_items, current_user=get_current_user(),
                           shop_sellers=shop_sellers,
                           announcements=announcements)


# This is to handle user's search requests
@blueprint.route("/search", methods=["GET", "POST"])
def search() -> str:
    keyword: str = request.args.get(key='keyword')
    print(keyword)
    # search all the item
    items: list = Item.query.filter(Item.name.like("%" + keyword + "%")).all()
    # remove disabled items
    for i in items:
        if i.disabled:
            items.remove(i)

    have_res = True
    if len(items) == 0:
        have_res = False
    return render_template("shopping/search.html", have_res=have_res, items=items, current_user=get_current_user(),
                           keyword=keyword)


@blueprint.route("/search_ajax", methods=["POST"])
def search_ajax():
    keyword = request.form.get("keyword")
    items = Item.query.filter(Item.name.like("%" + keyword + "%")).all()
    res = []
    for i in items:
        if i.disabled:
            continue
        if len(res) > 5:
            break
        res.append(i.name)
    return jsonify(res)


# About page
@blueprint.route("/about", methods=["GET", "POST"])
def about() -> str:
    return render_template("about/about.html", current_user=get_current_user())
