from sqlalchemy import Column, Sequence, Integer, String
from sqlalchemy.orm import backref, relationship

from shms.models import BaseModel


class Company(BaseModel):
    id = Column(Integer, Sequence('company_id_seq'), primary_key=True, autoincrement=True)

    dba = Column(String(128))
    name = Column(String(128))
    document = Column(String(32))
    code = Column(String(256), index=True, unique=True)

    users = relationship('User',
                         lazy="subquery",
                         cascade='save-update, merge, expunge',
                         backref=backref('company',
                                         lazy="subquery", cascade="all, delete-orphan", ))
    clients = relationship('Client',
                           lazy="subquery",
                           cascade='save-update, merge, expunge',
                           backref=backref('company',
                                           lazy="subquery",
                                           cascade="all, delete-orphan", ))
    hotels = relationship('Hotel',
                          lazy="subquery",
                          cascade='save-update, merge, expunge',
                          backref=backref('company',
                                          lazy="subquery",
                                          cascade="all, delete-orphan", ))

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
