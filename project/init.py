import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from urllib import request

from flask.logging import default_handler
from flask.logging import wsgi_errors_stream

from flask import render_template, url_for, flash, redirect, has_request_context
# from flask_admin.contrib.fileadmin import FileAdmin
# from flask_admin.contrib.sqla import ModelView
# from flask_login import current_user

from project import app, shopping, login, item, db, user

# from project.models.CategoryModel import Category
# from project.models.ItemModel import Item
# from project.models.OrderModel import Order
# from project.models.UserModel import User, Role
# from project.models.Cart import Cart
# from project.shopping import shop

session: dict = {

}

"""Register Flask blueprints."""
app.register_blueprint(shopping.view.blueprint)
app.register_blueprint(shopping.cart.blueprint)
app.register_blueprint(shopping.shop.blueprint)
app.register_blueprint(shopping.checkout.blueprint)
app.register_blueprint(shopping.order.blueprint)
app.register_blueprint(login.view.blueprint)
app.register_blueprint(item.view.blueprint)
app.register_blueprint(user.view.blueprint)
"""Configure loggers."""

# handler = logging.StreamHandler(sys.stdout)
# if not app.logger.handlers:
#     app.logger.addHandler(handler)

"""Register error handlers."""


def render_error(error):
    """Render error template."""
    # If a HTTPException, pull the `code` attribute; default to 500
    error_code = getattr(error, "code", 500)
    return render_template(f"errors/{error_code}.html"), error_code


# Replace original error pages
for errcode in [401, 404, 500]:
    app.errorhandler(errcode)(render_error)


@app.route("/favicon.ico")
def favicon_ico():
    return app.send_static_file('image/favicon.ico')


# """Init Admin"""
# admin.add_view(ModelView(User, db.session, name="Users", endpoint="users"))
# admin.add_view(ModelView(Item, db.session, name="items", endpoint="items"))
# admin.add_view(ModelView(Role, db.session, name="roles", endpoint="roles"))
# admin.add_view(ModelView(Cart, db.session, name="Cart", endpoint="Cart"))
# admin.add_view(ModelView(Category, db.session, name="Category", endpoint="Category"))
# admin.add_view(ModelView(Order, db.session, name="Order", endpoint="Order"))
# admin.add_view(FileAdmin("."))


# @app.route('/css/<file>')
# def css(file):
#     return url_for("static", filename="css/" + file)

class LevelFilter(object):

    def __init__(self, level):
        self.level = logging._checkLevel(level)

    def filter(self, record):
        return record.levelno == self.level


if not os.path.exists("log"):
    os.makedirs("log")


# logging config
# logging.basicConfig(
#                     format='asctime:        %(asctime)s \n'  # 时间
#                            'filename_line:  %(filename)s_[line:%(lineno)d] \n'  # 文件名_行号
#                            'level:          %(levelname)s \n'  # log级别
#                            'message:        %(message)s \n',  # log信息
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='log/log.log',
#                     filemode='a')  # 如果模式为'a'，则为续写（不会抹掉之前的log）
# yyyy-MM-dd HH:mm:ss,SSS
# HH:mm:ss.SSS
class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.msg = record.msg.replace("\n","")
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


# root = logging.getLogger()
# log_handler = logging.handlers.RotatingFileHandler('log/app.log', mode="a")
# log_handler.setFormatter(
#     RequestFormatter(
#         "%(asctime)s [%(lineno)d]%(levelname)8s - %(filename)s - %(message)s requested %(url)s"
#     )
# )
# log_handler.setLevel(logging.DEBUG)
# root.addHandler(log_handler)





# logging.basicConfig(
#     format="%(asctime)s [%(lineno)d]%(levelname)8s - %(filename)s - %(message)s",
#     datefmt='%Y-%m-%d %H:%M:%S,000',
#     level=logging.DEBUG,
#     filename='log/app.log',
#     filemode='a')
# root = logging.getLogger()
# info_handler = logging.handlers.RotatingFileHandler('log/info.log', mode="w")
# debug_handler = logging.handlers.RotatingFileHandler('log/debug.log', mode="w")
# error_handler = logging.handlers.RotatingFileHandler('log/error.log', mode="w")
# critical_handler = logging.handlers.RotatingFileHandler('log/critical.log', mode="w")
#
# formatter = logging.Formatter(
#     '[%(asctime)s] %(message)s'
# )
# info_handler.addFilter(LevelFilter('INFO'))
# info_handler.setFormatter(formatter)
#
# error_handler.addFilter(LevelFilter('ERROR'))
# error_handler.setFormatter(formatter)
#
# debug_handler.addFilter(LevelFilter("DEBUG"))
# debug_handler.setFormatter(formatter)
#
# critical_handler.addFilter(LevelFilter("CRITICAL"))
# critical_handler.setFormatter(formatter)
# # set formatters, etc..
#
# root.addHandler(info_handler)
# root.addHandler(error_handler)
# root.addHandler(debug_handler)
# root.addHandler(critical_handler)
# root.setLevel(logging.DEBUG)
#
# logging.log(logging.ERROR, "Start ERROR Logging")
# logging.log(logging.INFO, "Start INFO Logging")
# logging.log(logging.DEBUG, "Start DEBUG Logging")
# logging.log(logging.CRITICAL, "Start CRITICAL logging")
