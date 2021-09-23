import project.user.models
from project.database_model import PkModel, Column
from project import db
import datetime as dt


class Item(PkModel):
    """The products in this project"""
    __tablename__ = "item"
    name = Column(db.VARCHAR(255), nullable=False, default="")
    # category = Column(db.String(50), nullable=False, default="Default")
    price = Column(db.Float(50), nullable=False, default=0.0)
    description = db.Column(db.String(length=1024), nullable=False, default="")
    inventory = Column(db.Integer, nullable=False, default=0)
    sold_count = Column(db.Integer, nullable=False, default=0)
    disabled = Column(db.Boolean, nullable=False, default=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return f'<Item:{self.name},owner:{self.owner}>'
