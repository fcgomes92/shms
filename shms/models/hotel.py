from sqlalchemy import Column, Sequence, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from shms.models.base import BaseModel


class Hotel(BaseModel):
    __table_name__ = 'hotel'

    id = Column(Integer, Sequence('hotel_id_seq'), primary_key=True, autoincrement=False)
    company_id = Column(Integer, ForeignKey('company.id'), primary_key=True)

    name = Column(String(128))
    code = Column(String(256), index=True, unique=True)

    company = relationship('Company', lazy="subquery", cascade='save-update, merge, expunge')
    rooms = relationship('Room', lazy="subquery", cascade='save-update, merge, expunge')

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
