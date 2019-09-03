#merch/base_settings.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

"""
Secret key
"""

KEY = 'y12u_6q*&2o$q=^f6d%b=1j%ch3!+ljhd!c#2x&ava$e&nooa9'

"""
Database variables, 
"""

DEV_DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'merch',
        'USER': 'merch_main',
        'PASSWORD': 'merch_main',
        'HOST': 'cerebro.pw',
        'PORT': '',
    }
}

STAGING_DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'merch',
        'USER': 'merch_main',
        'PASSWORD': 'merch_main',
        'HOST': 'cerebro.pw',
        'PORT': '',
    }
}

PRODUCTION_DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'merch',
        'USER': 'merch_main',
        'PASSWORD': 'merch_main',
        'HOST': 'cerebro.pw',
        'PORT': '',
    }
}

SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

