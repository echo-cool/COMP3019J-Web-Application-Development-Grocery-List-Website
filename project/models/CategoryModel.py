from project.database_model import Column, PkModel, db


# This is the Category for set Category of different items
class Category(PkModel):
    __tablename__ = "category"
    name = Column(db.String(80), nullable=False, unique=True)
    item = db.relationship("Item", backref='item_category', lazy=True)
