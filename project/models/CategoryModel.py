
from project.database_model import Column, PkModel, db


class Category(PkModel):
    __tablename__ = "category"
    name = Column(db.String(80), nullable=False, unique=True)
    item = db.relationship("Item", backref='item_category', lazy=True)
