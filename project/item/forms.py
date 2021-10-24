from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, IntegerField, FloatField, SubmitField, FileField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired


class AddNewItem(FlaskForm):
    # userid = StringField("User ID", validators=[DataRequired(), ])
    item_name = StringField("Item Name", validators=[DataRequired(), ], default="")
    item_price = FloatField("Price", validators=[DataRequired()], default=0.0)
    description = StringField("Description", validators=[DataRequired()], default="")
    inventory = IntegerField("Inventory", validators=[DataRequired()], default=0)
    # main_image_url = URLField("main_image_url", validators=[], default="")
    main_image_file = FileField("Upload Image", validators=[
        FileRequired(),
        FileAllowed(['png', 'jpg', 'jpeg'], 'Only allow png, jpg')
    ])
    add_button = SubmitField("Add this item")


class UpdateItem(FlaskForm):
    item_name = StringField("Item Name", validators=[DataRequired(), ], default="")
    item_price = FloatField("Price", validators=[DataRequired()], default=0.0)
    description = StringField("Description", validators=[DataRequired()], default="")
    inventory = IntegerField("Inventory", validators=[DataRequired()])
    # main_image_url = URLField("main_image_url", validators=[], default="")
    main_image_file = FileField("Upload Image", validators=[
        FileAllowed(['png', 'jpg', 'jpeg'], 'Only allow png, jpg')
    ])
    add_button = SubmitField("Update this item")

