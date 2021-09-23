from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from project.login.forms import LoginForm, RegisterForm
from project.user.models import User
from project.utils import flash_errors

blueprint = Blueprint("index", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    return render_template("shopping/shoppping_main_page.html")
