# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from sqlalchemy.util import text_type

from project.database_model import Column, PkModel, db, reference_col, relationship
from project import bcrypt


class UserMixin(object):
    '''
    This provides default implementations for the methods that Flask-Login
    expects user objects to have.
    '''

    __hash__ = object.__hash__

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return text_type(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def __eq__(self, other):
        '''
        Checks the equality of two `UserMixin` objects using `get_id`.
        '''
        if isinstance(other, UserMixin):
            return self.get_id() == other.get_id()
        return NotImplemented

    def __ne__(self, other):
        '''
        Checks the inequality of two `UserMixin` objects using `get_id`.
        '''
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal


# @login_manager.user_loader
# def load_user(user_id):
#     # load user for login_manager
#     user = User.query.get(user_id)
#     return user


class Role(PkModel):
    """A role for a user."""

    __tablename__ = "roles"
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col("users", nullable=True)
    user = relationship("User", backref="roles")

    def __init__(self, name, **kwargs):
        """Create instance."""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Role({self.name})>"


class User(UserMixin, PkModel):
    """A user of the project."""

    __tablename__ = "users"
    username = Column(db.String(80), unique=True, nullable=False)
    main_image_url = Column(db.VARCHAR(255), nullable=True, default="static/image/user_info/default_avatar.jpg")
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.String(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_shopper = Column(db.Boolean(), default=False)
    items = db.relationship("Item", backref='owned_user', lazy=True)
    cart = db.relationship("Cart", backref='cart_user', lazy=True)
    order = db.relationship("Order", backref='order_user', lazy=True)

    # order_shopper = db.relationship("Order", backref='order_shopper_user', lazy=True)

    def __init__(self, username: str, email: str, password=None, **kwargs):
        """Create instance."""
        super().__init__(username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password: str):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value: str) -> bool:
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self) -> str:
        """Full user name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        """Represent instance as a unique string."""
        return f"<User(ID:{self.id},Name:{self.username!r})>"
