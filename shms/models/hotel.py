from sqlalchemy import Column, Sequence, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from shms.models import BaseModel


class Hotel(BaseModel):
    id = Column(Integer, Sequence('hotel_id_seq'), primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('company.id'), primary_key=True)

    name = Column(String(128))
    code = Column(String(256), index=True, unique=True)

    company = relationship('Company',
                           lazy="subquery",
                           cascade='save-update, merge, expunge',
                           backref=backref('hotels',
                                           lazy="subquery",
                                           cascade="all, delete-orphan", ))
    rooms = relationship('Room',
                         lazy="subquery",
                         cascade='save-update, merge, expunge',
                         backref=backref('hotel',
                                         lazy="subquery",
                                         cascade="all, delete-orphan", ))

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
