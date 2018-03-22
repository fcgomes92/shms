from sqlalchemy import Column, Sequence, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from shms.models import BaseModel


class Client(BaseModel):
    id = Column(Integer, Sequence('client_id_seq'), primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('company.id'), primary_key=True)

    name = Column(String(128))
    document = Column(String(32))
    code = Column(String(256), index=True, unique=True)
    origin = Column(String(32))

    company = relationship('Company',
                           lazy="subquery",
                           cascade='save-update, merge, expunge',
                           backref=backref('clients',
                                           lazy="subquery",
                                           cascade="all, delete-orphan", ))
    reservations = relationship('Reservation',
                                lazy="subquery",
                                cascade='save-update, merge, expunge',
                                backref=backref('client',
                                                lazy="subquery",
                                                cascade="all, delete-orphan", ))

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
