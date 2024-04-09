from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db



class Users(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, unique=True)
    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return f"<User: {self.username}>"


class Articles(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    category: so.Mapped[str] = so.mapped_column(sa.String(128))
    filename: so.Mapped[str] = so.mapped_column(sa.String(1024))

    def __repr__(self):
        return f"{self.id}, {self.category}, {self.filename}"

