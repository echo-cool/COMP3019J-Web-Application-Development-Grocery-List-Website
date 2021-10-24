import os

from project import app, db
from project.models.AnnouncementModel import Announcement
from project.models.CartModel import Cart

from project.models.ItemModel import Item
from project.models.OrderModel import Order
from project.models.UserModel import User

# This file tests the database to avoid null ref in database
print(app.blueprints)
print(app.config)
print(app.view_functions)

print(app.app_context())
print(Item.query.all())
print(User.query.all())
print(Cart.query.all())
print(Order.query.all())
print(Announcement.query.all())
for i in Order.query.all():
    shopper: User = User.get_by_id(i.shopper_id)
    item: Item = Item.get_by_id(i.item_id)
    if item.owner == shopper.id:
        print("pass", end=" ")
    else:
        print("".join(["-" for tmp in range(20)]))
        print("ERROR in DATABASE")
        print(shopper)
        print(item)
        print("".join(["-" for tmp in range(20)]))
        # i.shopper_id = item.owner
        # i.save()
for i in Cart.query.all():
    shopper: User = User.get_by_id(i.get_shop_userID())
    item: Item = Item.get_by_id(i.item_id)
    if item.owner == shopper.id:
        print("pass", end=" ")
    else:
        print("".join(["-" for tmp in range(20)]))
        print("ERROR in DATABASE")
        print(shopper)
        print(item)
        print("".join(["-" for tmp in range(20)]))
        # i.shopper_id = item.owner
        # i.save()

print()
for i in Item.query.all():
    sold_count = len(Order.query.filter_by(item_id=i.id).all())
    # print(i.id, sold_count)
    # i.sold_count = sold_count
    # i.save()
