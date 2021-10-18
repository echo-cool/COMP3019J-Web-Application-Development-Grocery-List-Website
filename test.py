import os

from project import app, db
from project.models.Cart import Cart

from project.models.ItemModel import Item
from project.models.UserModel import User

# db.drop_all()
# db.create_all()

# username = os.urandom(10).hex();
# user = User(username=username, email=username)
# user.save()
# item = Item(owner=user.id)
#
#
# item.save()

print(app.blueprints)
print(app.config)
print(app.view_functions)

print(app.app_context())
print(Item.query.all())
print(User.query.all())
print(Cart.query.all())