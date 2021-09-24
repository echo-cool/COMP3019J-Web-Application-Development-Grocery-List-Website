from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from project.models.ItemModel import Item

blueprint = Blueprint("index", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    all_items = Item.query.all()

    return render_template("shopping/index.html", items=all_items)


@blueprint.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")