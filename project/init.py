import logging
import sys

from flask import render_template, url_for
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView

from project import app, shopping, login, item, admin, db, userinfo
from project.models.ItemModel import Item
from project.models.UserModel import User, Role
from project.models.Cart import Cart

"""Register Flask blueprints."""
app.register_blueprint(shopping.view.blueprint)
app.register_blueprint(login.view.blueprint)
app.register_blueprint(item.view.blueprint)
app.register_blueprint(userinfo.view.blueprint)
"""Configure loggers."""
handler = logging.StreamHandler(sys.stdout)
if not app.logger.handlers:
    app.logger.addHandler(handler)

"""Register error handlers."""
def render_error(error):
    """Render error template."""
    # If a HTTPException, pull the `code` attribute; default to 500
    error_code = getattr(error, "code", 500)
    return render_template(f"errors/{error_code}.html"), error_code


for errcode in [401, 404, 500]:
    app.errorhandler(errcode)(render_error)


"""Init Admin"""
admin.add_view(ModelView(User, db.session, name="Users", endpoint="users"))
admin.add_view(ModelView(Item, db.session, name="items", endpoint="items"))
admin.add_view(ModelView(Role, db.session, name="roles", endpoint="roles"))
admin.add_view(ModelView(Cart, db.session, name="Cart", endpoint="Cart"))
admin.add_view(FileAdmin("."))


# @app.route('/css/<file>')
# def css(file):
#     return url_for("static", filename="css/" + file)