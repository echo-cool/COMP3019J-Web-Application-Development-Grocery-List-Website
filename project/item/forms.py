from flask import url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, IntegerField, FloatField, SubmitField, FileField
from wtforms.validators import DataRequired, Length


# This form is used when a user adds a new item to the site
class AddNewItem(FlaskForm):
    # userid = StringField("User ID", validators=[DataRequired(), ])
    item_name = StringField("Item Name", validators=[DataRequired(), Length(min=5, max=25)], default="")
    item_price = FloatField("Price", validators=[DataRequired()], default=0.0)
    description = StringField("Description", validators=[DataRequired(), Length(min=5)], default="")
    inventory = IntegerField("Inventory", validators=[DataRequired()], default=0)
    # main_image_url = URLField("main_image_url", validators=[], default="")]
    # Only allow images in the upload field
    main_image_file = FileField("Upload Image", validators=[
        FileRequired(),
        FileAllowed(['png', 'jpg', 'jpeg'], 'Only allow png, jpg')
    ])
    add_button = SubmitField("Add this item")


# This form is used when a user wants to update the information in the site
class UpdateItem(FlaskForm):
    item_name = StringField("Item Name", validators=[DataRequired(), Length(min=5, max=25)], default="")
    item_price = FloatField("Price", validators=[DataRequired()], default=0.0)
    description = StringField("Description", validators=[DataRequired(), Length(min=5)], default="")
    inventory = IntegerField("Inventory", validators=[DataRequired()], default=0)
    # main_image_url = URLField("main_image_url", validators=[], default="")
    # Only allow images in the upload field
    main_image_file = FileField("Upload Image", validators=[
        FileAllowed(['png', 'jpg', 'jpeg'], 'Only allow png, jpg')
    ])
    add_button = SubmitField("Update this item")
