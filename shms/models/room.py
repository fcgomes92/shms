from sqlalchemy import Boolean, Column, ForeignKey, Integer, Sequence, String, Text
from sqlalchemy.orm import relationship, validates

from shms.models.base import BaseModel


class Room(BaseModel):
    __table_name__ = 'room'

    valid_types = ['shared', 'private', ]

    id = Column(Integer, Sequence('room_id_seq'), primary_key=True, autoincrement=False)
    hotel_id = Column(ForeignKey('hotel.id'), primary_key=True)

    name = Column(String(128), nullable=False)
    type = Column(String(32), default='private')
    vacancies = Column(Integer, default=0)
    shared = Column(Boolean, default=False)
    code = Column(String(256), index=True, unique=True)
    description = Column(Text, default='', nullable=True)

    reservations = relationship('Reservation', lazy="subquery", cascade='save-update, merge, expunge')
    features = relationship('Feature', lazy="subquery", cascade='save-update, merge, expunge')
    hotel = relationship('Hotel', lazy="subquery", cascade='save-update, merge, expunge')

    @validates('type')
    def validate_types(self, key, tp):
        assert tp in self.valid_types
        return tp

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
