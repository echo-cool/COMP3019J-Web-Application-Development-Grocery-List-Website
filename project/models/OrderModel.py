from project import db
import datetime as dt
from project.database_model import PkModel, Column
from project.models.ItemModel import Item


class Order(PkModel):
    __tablename__ = "orders"
    order_id = Column(db.Integer, nullable=False)
    count = Column(db.Integer, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    shopper_id = db.Column(db.Integer)
    is_confirmed_by_shopper = db.Column(db.Boolean, nullable=False, default=False)
    is_confirmed_delivery = db.Column(db.Boolean, nullable=False, default=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, order_id, item_id, user_id, count) -> None:
        self.order_id = order_id
        self.item_id = item_id
        self.user_id = user_id
        self.shopper_id = Item.get_by_id(self.item_id).owner
        self.count = count
        super().__init__()

    def get_shop_userID(self) -> int:
        return Item.get_by_id(self.item_id).owner

    def __repr__(self) -> str:
        return f'<Item:{self.item_id},user:{self.user_id},count:{self.count},shop:{self.get_shop_userID()}>'


def get_order_items_by_id(order_id) -> list:
    return Order.query.filter_by(order_id=order_id).all()


def get_orders_by_userid(user_id) -> dict:
    items: list[Order] = Order.query.filter_by(user_id=user_id).all()
    res: dict[str: Order] = {}
    for i in items:
        order_id: int = i.order_id
        if order_id not in res.keys():
            res[order_id] = [i]
        else:
            res[order_id].append(i)
    return res


def get_orders_by_shopper(shopper_id) -> dict:
    items: list[Order] = Order.query.filter_by(shopper_id=shopper_id).all()
    res: dict[str: Order] = {}
    for i in items:
        order_id: int = i.order_id
        if order_id not in res.keys():
            res[order_id] = [i]
        else:
            res[order_id].append(i)
    return res
