from sqlalchemy import Column, Sequence, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from shms.models import BaseModel


class Feature(BaseModel):
    id = Column(Integer, Sequence('feature_id_seq'), primary_key=True, autoincrement=True)
    room_id = Column(ForeignKey('room.id'), primary_key=True)

    name = Column(String(128))
    value = Column(String(64))
    code = Column(String(256), index=True, unique=True)

    room = relationship('Room',
                        lazy="subquery",
                        cascade='save-update, merge, expunge',
                        backref=backref('features',
                                        lazy="subquery",
                                        cascade="all, delete-orphan", ))

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
