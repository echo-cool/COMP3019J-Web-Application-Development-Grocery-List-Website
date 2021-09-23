import logging
import sys

from flask import Flask, render_template

from project import app, shopping, login

"""Register Flask blueprints."""
app.register_blueprint(shopping.view.blueprint)
app.register_blueprint(login.view.blueprint)

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

