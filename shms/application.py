import logging

from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import configure_mappers, scoped_session, sessionmaker


class SHMSApplication(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object('shms.settings')
        self.config = self.app.config

        self.engine = create_engine(self.config['DATABASE_URI'], echo=False, convert_unicode=True)
        self.Session = scoped_session(sessionmaker(bind=self.engine, autocommit=False, autoflush=False, ))

        self.configure_cors()

    def configure_cors(self):
        CORS(self.app)

    def map_models(self, bind_engine):
        import shms.models
        shms.models.BaseModel.metadata.create_all(bind=bind_engine)
        # maps the abstract user class
        configure_mappers()

    def configure_logging(self):
        if self.config.DEBUG:
            logging.basicConfig(level=self.config.LOGGING_LEVEL,
                                filename='./logging.log',
                                filemode='w',
                                format=self.config.LOGGING_FORMAT)
        else:
            logging.basicConfig(level=self.config.LOGGING_LEVEL,
                                format=self.config.LOGGING_FORMAT)

# app = SHMSApplication()
