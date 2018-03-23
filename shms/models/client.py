from sqlalchemy import Column, Sequence, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from shms.models.base import BaseModel


class Client(BaseModel):
    __table_name__ = 'client'

    id = Column(Integer, Sequence('client_id_seq'), primary_key=True, autoincrement=False)
    company_id = Column(Integer, ForeignKey('company.id'), primary_key=True)

    name = Column(String(128))
    document = Column(String(32))
    code = Column(String(256), index=True, unique=True)
    origin = Column(String(32))

    company = relationship('Company', lazy="subquery", cascade='save-update, merge, expunge')
    reservations = relationship('Reservation', lazy="subquery", cascade='save-update, merge, expunge')

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
