from project import db
import datetime as dt
from project.database_model import PkModel, Column
from project.models.ItemModel import Item


class Cart(PkModel):
    __tablename__ = "carts"
    count = Column(db.Integer, nullable=False, default=0)

    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, item_id, user_id, count) -> None:
        self.item_id = item_id;
        self.user_id = user_id;
        self.count = count;
        super().__init__()

    def get_shop_userID(self):
        return Item.get_by_id(self.item_id).owner

    def __repr__(self):
        return f'<Item:{self.item_id},user:{self.user_id},count:{self.count},shop:{self.get_shop_userID()}>'
