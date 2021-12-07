# -*- coding: utf-8 -*-
"""User forms."""
import re

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError, Email

from project.models.UserModel import User


def validate_email(message=None):
    if message is None:
        message = 'Must email address.'

    def validate_email(form, field):
        if not re.match(r'^([\w]+\.*)([\w]+)\@[\w]+\.\w{3}(\.\w{2}|)$', field.data):
            raise ValidationError(message)

    return validate_email


# reset password
class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', render_kw={"placeholder": "Your Email"},
                        validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Reset Password')


# reset password inside the email
class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', render_kw={"placeholder": "New Password"},
                             validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', render_kw={"placeholder": "Confirm password"},
                              validators=[DataRequired()])
    submit = SubmitField('Reset Password')


# This is the RegisterForm which will be used in the register page
class RegisterForm(FlaskForm):
    """Register form."""

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = StringField(
        "Email", validators=[DataRequired(), validate_email(), Length(min=3, max=40)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=3, max=40)]
    )
    confirm = PasswordField(
        "Verify password",
        [DataRequired(), EqualTo("password", message="Passwords must match")],
    )
    submit_register = SubmitField("Register")

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True


class LoginForm(FlaskForm):
    """Register form."""

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=1, max=25)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=1, max=40)]
    )
    submit_login = SubmitField("Login")

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False
        else:
            return True
