import os

from project import db

from project.shopping.models import Item
from project.user.models import User

db.drop_all()
db.create_all()

username = os.urandom(10).hex();
user = User(username=username, email=username)
user.save()
item = Item(owner=user.id)


item.save()