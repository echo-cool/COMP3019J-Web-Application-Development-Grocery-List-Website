from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UpdateFrom(FlaskForm):
    content = StringField(
        "content", validators=[DataRequired(), Length(min=1, max=25)]
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(UpdateFrom, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(UpdateFrom, self).validate()
        if not initial_validation:

            return False
        else:
            return True


class AddTaskFrom(FlaskForm):
    content = StringField(
        "content", validators=[DataRequired(), Length(min=1, max=25)]
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(AddTaskFrom, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(AddTaskFrom, self).validate()
        if not initial_validation:

            return False
        else:
            return True
