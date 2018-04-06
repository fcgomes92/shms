from datetime import datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from shms.application import app
from shms.util import friendly_code


class Base(object):
    created = Column(DateTime)
    updated = Column(DateTime)

    __table__ = None
    id = None
    code = None

    def save(self):
        if not getattr(self, 'id', None):
            self.created = datetime.utcnow()
            app.database.session().add(self)
        else:
            cls = self.__class__
            query = app.database.session().query(cls)
            query = query.filter(cls.id == self.id)
            query.update({
                column: getattr(self, column)
                for column in self.__table__.columns.keys()
            })
        self.updated = datetime.utcnow()
        app.database.session().flush()

        if 'code' in self.__table__.columns.keys():
            if not self.code:
                self.code = friendly_code.encode(int(self.id))
                app.database.session().flush()

    def delete(self):
        app.database.session().delete(self)
        app.database.session().flush()

    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()

    @classmethod
    def get_all(cls):
        return app.database.session().query(cls).all()

    @classmethod
    def get_by_id(cls, model_id):
        if cls.id:
            return app.database.session().query(cls).filter(cls.id == model_id).first()
        else:
            return None

    @classmethod
    def get_by_code(cls, code):
        if getattr(cls, 'code', None):
            return app.database.session().query(cls).filter(cls.code == code).first()
        else:
            return None


BaseModel = declarative_base(cls=Base)
