from project import db
import datetime as dt
from project.database_model import PkModel, Column


# This is the Announcement model for showing the Announcements in the main index page
class Announcement(PkModel):
    __tablename__ = "announcements"
    name = Column(db.String, nullable=False, default="")
    content = Column(db.String, nullable=False, default="")

    def __init__(self, name, content) -> None:
        """Create instance."""
        self.name = name
        self.content = content
        super().__init__()

    def __repr__(self) -> str:
        """Represent instance as a unique string."""
        return f'<name:{self.name},content:{self.content}>'
