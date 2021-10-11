import datetime as dt

from flask_login import UserMixin

from project.database_model import Column, PkModel, db, reference_col, relationship
from project import bcrypt, login_manager


class Category(PkModel):
    __tablename__ = "category"
    name = Column(db.String(80), nullable=False, unique=True)
    item = db.relationship("Item", backref='item_category', lazy=True)
