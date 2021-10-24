
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, IntegerField, FloatField, SubmitField, FileField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired

# This form is used when user want to update his personal information
class UpdateUser(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), ])
    email = StringField("Email", validators=[DataRequired(), ])
    password = StringField("Username", validators=[])
    image_file = FileField("Upload Image", validators=[
        FileAllowed(['png', 'jpg', 'jpeg'], 'Only allow png, jpg')
    ])
    submit_button = SubmitField("Update user information")
