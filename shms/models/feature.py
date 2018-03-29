from sqlalchemy import Column, ForeignKey, Integer, Sequence, String
from sqlalchemy.orm import relationship

from shms.models.base import BaseModel


class Feature(BaseModel):
    __table_name__ = 'feature'

    id = Column(Integer, Sequence('feature_id_seq'), primary_key=True, autoincrement=False)
    room_id = Column(ForeignKey('room.id'), primary_key=True)

    name = Column(String(128))
    value = Column(String(64))
    code = Column(String(256), index=True, unique=True)

    room = relationship('Room', lazy="subquery", cascade='save-update, merge, expunge')

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
