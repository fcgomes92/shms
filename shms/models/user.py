import hashlib
import uuid

from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import AbstractConcreteBase

from shms.database import session
from shms.util import auth

from shms.models.base import BaseModel


class User(AbstractConcreteBase, BaseModel):
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True,
                autoincrement=True)
    email = Column(String(128), unique=True)
    first_name = Column(String(128))
    last_name = Column(String(128))
    password = Column(String(256))
    seed = Column(String(128))
    code = Column(String(256), index=True, unique=True)

    __mapper_args__ = {
        'confirm_deleted_rows': False,
    }

    def __repr__(self):
        return "<{} (id={}, email={}, first_name={}, last_name={})>" \
            .format(self.__class__.__name__, self.id, self.email,
                    self.first_name, self.last_name)

    @staticmethod
    def hash_password(password, seed):
        if not seed:
            seed = uuid.uuid4().hex
        return hashlib.sha512((password + seed).encode()).hexdigest(), seed

    def set_password(self, password):
        self.password, self.seed = self.hash_password(password, None)

    @classmethod
    def get_by_email(cls, email):
        return session().query(cls).filter(cls.email == email).first()

    @classmethod
    def get_by_token(cls, token):
        data = auth.decode(token)
        return cls.get_by_email(data.get('email'))

    def get_token(self):
        from shms.util.auth import encode
        return encode(dict(code=self.code, email=self.email)).decode()
