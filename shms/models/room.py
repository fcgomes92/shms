from sqlalchemy import Column, Sequence, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import backref, relationship, validates

from shms.models import BaseModel


class Room(BaseModel):
    valid_types = ['shared', 'private', ]

    id = Column(Integer, Sequence('room_id_seq'), primary_key=True, autoincrement=True)
    hotel_id = Column(ForeignKey('hotel.id'), primary_key=True)

    name = Column(String(128), nullable=False)
    type = Column(String(32))
    vacancies = Column(Integer, default=0)
    shared = Column(Boolean, default=False)
    code = Column(String(256), index=True, unique=True)

    reservations = relationship('Reservation',
                                lazy="subquery",
                                cascade='save-update, merge, expunge',
                                backref=backref('room',
                                                lazy="subquery",
                                                cascade="all, delete-orphan", ))
    features = relationship('Feature',
                            lazy="subquery",
                            cascade='save-update, merge, expunge',
                            backref=backref('room',
                                            lazy="subquery",
                                            cascade="all, delete-orphan", ))
    hotel = relationship('Hotel',
                         lazy="subquery",
                         cascade='save-update, merge, expunge',
                         backref=backref('rooms',
                                         lazy="subquery",
                                         cascade="all, delete-orphan", ))

    @validates('type')
    def validate_types(self, key, tp):
        assert tp in self.valid_types
        return tp

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
