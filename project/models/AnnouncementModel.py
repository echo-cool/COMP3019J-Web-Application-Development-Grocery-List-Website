from project import db
import datetime as dt
from project.database_model import PkModel, Column


class Announcement(PkModel):
    __tablename__ = "announcements"
    name = Column(db.String, nullable=False, default="")
    content = Column(db.String, nullable=False, default="")

    def __init__(self, name, content) -> None:
        self.name = name
        self.content = content
        super().__init__()

    def __repr__(self) -> str:
        return f'<name:{self.name},content:{self.content}>'
