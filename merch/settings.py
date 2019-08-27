#merch/settings.py

import os

from . import base_settings as base

PRODUCTS = os.path.join(base.BASE_DIR, 'products')
INVENTORY = os.path.join(base.BASE_DIR, 'inventory')
MAIN = os.path.join(base.BASE_DIR, 'main')
ORDERING = os.path.join(base.BASE_DIR, 'ordering')


SECRET_KEY = base.KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user.apps.UserConfig',
    'main',
    'products',
    'inventory',
    'ordering',
    'debug_toolbar',
]

AUTH_USER_MODEL = 'user.CustomUser'

LOGIN_REDIRECT_URL = 'main.index'
LOGOUT_REDIRECT_URL = '/accounts/login'

INTERNAL_IPS = [
    '127.0.0.1',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'merch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(MAIN, 'templates'),
            os.path.join(PRODUCTS, 'templates'),
            os.path.join(INVENTORY, 'templates'),
            os.path.join(ORDERING, 'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'merch.wsgi.application'

# Database
DATABASES = base.SQLITE3

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Boise'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(base.BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(MAIN, 'static/'),
    os.path.join(PRODUCTS, 'static/'),
    os.path.join(INVENTORY, 'static/'),
    os.path.join(ORDERING, 'static/'),
]

#Uploaded media configuration

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(base.BASE_DIR, 'media/')