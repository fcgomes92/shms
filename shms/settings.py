import logging

from decouple import config

DEBUG = config('DEBUG', cast=bool, default=False)

config('SECRET_KEY', cast=str, default='I_LIKE_POTATOES_A_LOT')

# JTW Config
JWT_SECRET_KEY = config('JWT_SECRET_KEY', cast=str, default='I_LIKE_POTATOES')
JWT_ALGORITHM = config('JWT_ALGORITHM', cast=str, default='HS256')

STORAGE_PATH = config('STORAGE_PATH', './images')

DATABASE_URI = config('DATABASE_URI', None)

_default_logging_format = '[%(levelname)s][%(asctime)s][%(name)s]: %(message)s'
LOGGING_LEVEL = config('LOGGING_LEVEL', cast=int, default=logging.ERROR)
LOGGING_FORMAT = config('LOGGING_FORMAT', default=_default_logging_format)
