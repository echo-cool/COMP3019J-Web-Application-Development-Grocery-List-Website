from flask_wtf import FlaskForm
from wtforms import StringField


class UpdateFrom(FlaskForm):
    content = StringField("content")


class AddTaskFrom(FlaskForm):
    content = StringField("content")
