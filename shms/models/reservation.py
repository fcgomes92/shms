from sqlalchemy import Column, Sequence, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import backref, relationship, validates

from shms.models import BaseModel


class Reservation(BaseModel):
    id = Column(Integer, Sequence('reservation_id_seq'), primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('room.id'), primary_key=True)
    client_id = Column(Integer, ForeignKey('client.id'), primary_key=True)
    guests = Column(Integer, default=1)
    checkin = Column(DateTime, nullable=False)
    checkout = Column(DateTime, nullable=False)

    code = Column(String(256), index=True, unique=True)

    room = relationship('Room',
                        lazy="subquery",
                        cascade='save-update, merge, expunge',
                        backref=backref('reservations',
                                        lazy="subquery",
                                        cascade="all, delete-orphan", ))
    client = relationship('Client',
                          lazy="subquery",
                          cascade='save-update, merge, expunge',
                          backref=backref('reservations',
                                          lazy="subquery",
                                          cascade="all, delete-orphan", ))

    @validates
    def validates_guests(self, key, guests):
        assert guests > 0
        return guests

    def __repr__(self):
        return f"<{self.__class__.__name__} (name={self.name})>"
