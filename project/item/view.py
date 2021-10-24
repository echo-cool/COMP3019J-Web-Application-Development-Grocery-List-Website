import os

from flask import Blueprint, render_template, flash, current_app, url_for, Response, redirect
from flask_login import current_user, login_required
from project import db
from project.item.forms import AddNewItem, UpdateItem
from project.models.CartModel import Cart
from project.models.ItemModel import Item
from project.models.UserModel import User
from project.utils import seller_required, product_available_required, flash_errors

blueprint = Blueprint("item", __name__, static_folder="../static")

# This is a route if a user want to view a product detail
@blueprint.route("/item/<int:itemID>", methods=["GET", "POST"])
@product_available_required
def details(itemID: int) -> str:
    item = Item.get_by_id(itemID)
    owner = User.get_by_id(item.owner)
    return render_template("shopping/product_details.html", item=item, shop=owner)

# This is used when shoppers need to manage his shop
@blueprint.route("/item/manage", methods=["POST", "GET"])
@login_required
@seller_required
def ManageItem() -> str:
    user = current_user
    # Get all the items for this shopper
    items = Item.query.filter_by(
        owner=user.id,
        disabled=False
    ).all()
    itemsLength = len(items)
    form = AddNewItem()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        userid = current_user.id
        item_name = form.item_name.data
        item_price = form.item_price.data
        description = form.description.data
        inventory = form.inventory.data
        main_image_file = form.main_image_file.data
        print(main_image_file)
        main_image_url = ""
        # if uploaded a image
        if main_image_file.filename != "":
            filename = str(os.urandom(30).hex()) + "." + main_image_file.filename.split(".")[-1]
            main_image_file.save(os.path.join(current_app.static_folder, 'uploaded_files', filename))
            main_image_url = filename

        new_item = Item(name=item_name,
                        price=item_price,
                        description=description,
                        inventory=inventory,
                        main_image_url=main_image_url,
                        owner=userid)
        try:
            new_item.save()
            flash("Save " + item_name + " Successfully to database !")
        except Exception as e:
            # save failed
            flash("Save Failed, Check your input !")
            print(e.message)
            db.session.rollback()
    flash_errors(form)
    return render_template("item/manage.html", items=items, form=form, itemsLength=itemsLength)


@blueprint.route("/item/delete/<int:item_id>", methods=["POST", "GET"])
@login_required
@seller_required
def DeleteItem(item_id: int) -> Response:
    item = Item.get_by_id(item_id)
    # item.delete()
    # Set item state to disable
    item.disabled = True
    item.save()
    # remove all the related cart item
    for i in Cart.query.filter_by(item_id=item_id).all():
        i.delete()
    flash("Delete Success")
    return redirect(url_for("item.ManageItem"))

# a shopper need to modify the item
@blueprint.route("/item/modify/<int:item_id>", methods=["POST", "GET"])
@login_required
@seller_required
def ModifyNewItem(item_id: int) -> str:
    item = Item.get_by_id(item_id)
    form = UpdateItem()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        item_name = form.item_name.data
        item_price = form.item_price.data
        description = form.description.data
        inventory = form.inventory.data
        main_image_file = form.main_image_file.data
        # print()
        # a new image uploaded
        if main_image_file.filename != "":
            filename = str(os.urandom(30).hex()) + "." + main_image_file.filename.split(".")[-1]
            main_image_file.save(os.path.join(current_app.static_folder, 'uploaded_files', filename))

        item.name = item_name
        item.price = item_price
        item.description = description
        item.inventory = inventory
        if main_image_file.filename != "":
            item.main_image_url = filename
        item.update()
        flash("Update Success")
    flash_errors(form)
    return render_template("item/update.html", item=item, form=form)

# a shopper need to add new items
@blueprint.route("/item/add", methods=["POST", "GET"])
@login_required
@seller_required
def addNewItem() -> str:
    form = AddNewItem()
    # print(form.data)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        userid = current_user.id
        item_name = form.item_name.data
        item_price = form.item_price.data
        description = form.description.data
        inventory = form.inventory.data
        main_image_file = form.main_image_file.data
        print(main_image_file)
        main_image_url = ""
        if main_image_file.filename != "":
            filename = str(os.urandom(30).hex()) + "." + main_image_file.filename.split(".")[-1]
            main_image_file.save(os.path.join(current_app.static_folder, 'uploaded_files', filename))
            main_image_url = filename

        new_item = Item(name=item_name,
                        price=item_price,
                        description=description,
                        inventory=inventory,
                        main_image_url=main_image_url,
                        owner=userid)

        try:
            new_item.save()
            flash("Save " + item_name + " Successfully to database !")
        except Exception as e:
            flash("Save Failed, Check your input !")
            print(e.message)
            db.session.rollback()
    flash_errors(form)
    return render_template("item/add.html", form=form)

# get all user's items
@blueprint.route("/item/show/<int:userid>", methods=["POST", "GET"])
@login_required
def show_all_items(userid: int) -> str:
    # user = User.query.filter_by(username=username).first()
    # print(user)
    user = User.query.filter_by(id=userid).first()
    username = user.username
    items = Item.query.filter_by(owner=userid, disabled=False).all()
    # print(items)
    return render_template("shopping/shopper_all_items.html", items=items, username=username)
