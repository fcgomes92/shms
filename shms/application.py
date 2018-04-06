import logging

import falcon
from falcon_cors import CORS

from shms import settings
from shms.database import Database

app = None


class Config(object):
    DEBUG = True
    DATABASE_URI = None
    LOGGING_LEVEL = None
    LOGGING_FORMAT = None


class SHMSApplication(object):
    def __init__(self):
        self.config = self.set_config()
        self.database = Database(database_url=self.config.DATABASE_URI)
        self.app = falcon.API(middleware=self.register_middleware())

    @staticmethod
    def set_config():
        config = Config()

        for key in dir(settings):
            if key.isupper():
                setattr(config, key, getattr(settings, key))

        return config

    @staticmethod
    def register_middleware():
        from shms.middleware import NonBlockingAuthentication, LoggerMiddleware
        cors = CORS(allow_all_origins=True,
                    allow_all_headers=True,
                    allow_credentials_all_origins=True,
                    allow_all_methods=True)

        return [
            cors.middleware,
            NonBlockingAuthentication(),
            LoggerMiddleware(logging.getLogger(__name__)),
        ]

    def configure_logging(self):
        if self.config.DEBUG:
            logging.basicConfig(level=self.config.LOGGING_LEVEL,
                                filename='./logging.log',
                                filemode='w',
                                format=self.config.LOGGING_FORMAT)
        else:
            logging.basicConfig(level=self.config.LOGGING_LEVEL,
                                format=self.config.LOGGING_FORMAT)


try:
    app = SHMSApplication()
except Exception as e:
    print(e)
