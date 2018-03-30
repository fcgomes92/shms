import logging

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import configure_mappers, scoped_session, sessionmaker


def map_models(bind_engine):
    import shms.models
    shms.models.BaseModel.metadata.create_all(bind=bind_engine)
    # maps the abstract user class
    configure_mappers()


def configure_logging():
    global DEBUG
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
engine = create_engine(config('DATABASE_URI', None), echo=False, convert_unicode=True)
Session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False, ))
map_models(engine)

configure_logging()
