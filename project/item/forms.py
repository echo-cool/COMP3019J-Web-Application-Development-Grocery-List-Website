from flask_admin.form import FileUploadField
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, FileField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired


class AddNewItem(FlaskForm):
    userid = StringField("userid", validators=[DataRequired(),])
    item_name = StringField("item_name", validators=[DataRequired(),], default="")
    item_price = FloatField("price", validators=[],default=0.0)
    description = StringField("description", validators=[], default="")
    inventory = IntegerField("inventory", validators=[], default=0)
    # main_image_url = URLField("main_image_url", validators=[], default="")
    main_image_file = FileField("Upload Image")
    add_button = SubmitField("Add this item")

