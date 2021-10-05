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


@blueprint.route("/product_details", methods=["GET", "POST"])
def details():
    return render_template("shopping/product_details.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('See you later！')
    return redirect(url_for('index.home'))


# @app.route('/product_details')
# @login_required
# def logout():
#     logout_user()
#     flash('View Product Details！')
#     return render_template("shopping/product_details.html")
