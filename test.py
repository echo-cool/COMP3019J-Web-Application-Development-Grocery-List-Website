import os

from project import db

from project.models.ItemModel import Item
from project.models.UserModel import User

db.drop_all()
db.create_all()

# username = os.urandom(10).hex();
# user = User(username=username, email=username)
# user.save()
# item = Item(owner=user.id)
#
#
# item.save()