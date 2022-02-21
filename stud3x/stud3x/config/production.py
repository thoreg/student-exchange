import os

from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('STUD3X_PSQL_DB'),
        'USER': os.getenv('STUD3X_PSQL_USER'),
        'PASSWORD': os.getenv('STUD3X_PSQL_PASSWORD'),
        'HOST': os.getenv('STUD3X_PSQL_HOST'),
        'PORT': int(os.getenv('STUD3X_PSQL_PORT')),
    }
}

DEBUG = False
SECRET_KEY = os.getenv('STUD3X_PRODUCTION_DJANGO_SECRET')

STATIC_ROOT = os.getenv('STATIC_ROOT')

EMAIL_BACKEND = 'django_ses.SESBackend'

AWS_ACCESS_KEY_ID = os.getenv('STUD3X_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('STUD3X_AWS_SECRET_ACCESS_KEY')

LOG_DIR = os.getenv('STUD3X_LOG_DIR', '/var/log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{LOG_DIR}/django/stud3x/default.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{LOG_DIR}/django/stud3x/requests.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {

        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {  # Stop SQL debug from logging to main logger
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
