from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

blueprint = Blueprint("index", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    return render_template("shopping/shoppping_main_page.html")


@blueprint.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")