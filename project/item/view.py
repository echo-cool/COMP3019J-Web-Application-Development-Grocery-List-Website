import os

from flask import Blueprint, render_template, flash, current_app, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename

from project import db
from project.item.forms import AddNewItem, UpdateItem
from project.models.ItemModel import Item

blueprint = Blueprint("item", __name__, static_folder="../static")


@blueprint.route("/item/modify/<int:item_id>", methods=["POST", "GET"])
@login_required
def ModifyNewItem(item_id):
    item = Item.get_by_id(item_id)
    form = UpdateItem()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        item_name = form.item_name.data
        item_price = form.item_price.data
        description = form.description.data
        inventory = form.inventory.data
        main_image_file = form.main_image_file.data
        print()
        if main_image_file.filename != "":
            filename = str(os.urandom(30).hex()) + "." + main_image_file.filename.split(".")[-1];
            main_image_file.save(os.path.join(current_app.static_folder, 'uploaded_files', filename))

        item.name = item_name
        item.price = item_price
        item.description = description
        item.inventory = inventory
        if main_image_file.filename != "":
            item.main_image_url = filename
        item.update()
        flash("Update Success")
    return render_template("item/update.html", item = item, form = form)






@blueprint.route("/item/add", methods=["POST", "GET"])
@login_required
def addNewItem():
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
        main_image_url=""
        if main_image_file.filename != "":
            filename = str(os.urandom(30).hex()) + "." + main_image_file.filename.split(".")[-1];
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

    return render_template("item/add.html", form=form)
