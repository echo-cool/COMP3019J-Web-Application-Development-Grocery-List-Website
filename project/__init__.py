from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_static_digest import FlaskStaticDigest
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_caching import Cache
from flask_bcrypt import Bcrypt
from flask_admin import Admin, BaseView, expose

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'ec9439cfc6d796ae3029594d'
db = SQLAlchemy(app)
csrf_protect = CSRFProtect(app)
migrate = Migrate(app, db)
debug_toolbar = DebugToolbarExtension(app)
flask_static_digest = FlaskStaticDigest(app)
cache = Cache(app)
login_manager = LoginManager(app)
login_manager.login_view="login.login"
bcrypt = Bcrypt(app)
admin = Admin(app)

from project import init

