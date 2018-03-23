from decouple import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, configure_mappers, scoped_session

import logging


def map_models():
    import shms.models
    shms.models.BaseModel.metadata.create_all(bind=engine)
    # maps the abstract user class
    configure_mappers()


def configure_logging():
    _default_logging_format = '[%(levelname)s][%(asctime)s][%(name)s]: %(message)s'
    if DEBUG:
        logging.basicConfig(level=config('LOGGING_LEVEL', cast=int, default=logging.ERROR),
                            filename='./logging.log',
                            filemode='w',
                            format=config('LOGGING_FORMAT', default=_default_logging_format))
    else:
        logging.basicConfig(level=config('LOGGING_LEVEL', cast=int, default=logging.ERROR),
                            format=config('LOGGING_FORMAT', default=_default_logging_format))


DEBUG = config('DEBUG', cast=bool, default=False)

# JTW Config
JWT_SECRET_KEY = config('JWT_SECRET_KEY', cast=str, default='I_LIKE_POTATOES')
JWT_ALGORITHM = config('JWT_ALGORITHM', cast=str, default='HS256')

# set the storege module
storage_path = config('STORAGE_PATH', './images')

# set the db connection
engine = create_engine(config('DATABASE_URI', None), echo=False)
Session = scoped_session(sessionmaker(bind=engine))

configure_logging()
map_models()
