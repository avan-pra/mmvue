from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Birthday(Base):
    __tablename__ = 'birthday'

    id: Mapped[int] = mapped_column(primary_key=True)
    name = mapped_column(String(30))
    date = mapped_column(Date)

    def to_dict(self):
        return { 'id': self.id, 'name': self.name, 'date': datetime.strftime(self.date, '%Y-%m-%d')}
