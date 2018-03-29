from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import relationship

from shms.models.base import BaseModel


class Company(BaseModel):
    __table_name__ = 'company'

    id = Column(Integer, Sequence('company_id_seq'), primary_key=True, autoincrement=False)

    dba = Column(String(128))
    name = Column(String(128))
    document = Column(String(32))
    code = Column(String(256), index=True, unique=True)

    users = relationship('User', lazy="subquery", cascade='save-update, merge, expunge')
    clients = relationship('Client', lazy="subquery", cascade='save-update, merge, expunge')
    hotels = relationship('Hotel', lazy="subquery", cascade='save-update, merge, expunge')

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
