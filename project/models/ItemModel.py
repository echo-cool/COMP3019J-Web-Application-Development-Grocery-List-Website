from sqlalchemy import or_

from project.database_model import PkModel, Column
from project import db
import datetime as dt


class Item(PkModel):
    """The products in this project"""
    __tablename__ = "item"
    name = Column(db.VARCHAR(255), nullable=False, default="")
    # category = Column(db.String(50), nullable=False, default="Default")
    price = Column(db.Float(50), nullable=False, default=0.0)
    description = db.Column(db.String(length=1024), nullable=False, default="")
    inventory = Column(db.Integer, nullable=False, default=0)
    sold_count = Column(db.Integer, nullable=False, default=0)
    disabled = Column(db.Boolean, nullable=False, default=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    main_image_url = Column(db.VARCHAR(255), nullable=False, default="")
    owner = db.Column(db.Integer, db.ForeignKey("users.id"))
    cart = db.relationship("Cart", backref='cart_item', lazy=True)
    order = db.relationship("Order", backref='order_item', lazy=True)
    #category_id = Column(db.Integer, db.ForeignKey("category.id"), nullable=True, default=db.null)

    def __init__(self, name, price, description, inventory, main_image_url, owner) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.inventory = inventory
        self.main_image_url = main_image_url
        self.owner = owner
        super().__init__()

    def __repr__(self) -> str:
        return f'<Item:{self.name},price:{self.price},description:{self.description},inventory:{self.inventory},' \
               f'main_image_url:{self.main_image_url},owner:{self.owner}> '
