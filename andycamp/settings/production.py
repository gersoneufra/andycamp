# -*- encoding; utf-8 -*-
from .base import *  # pyflakes.ignore

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Victor Aguilar Cusicanqui', 'jvacx.log@gmail.com'),
)

MANAGERS = ADMINS
# Databases ---------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER':'',
        'PASSWORD':'',
        'HOST':'',
        'PORT':'5432'
    }
}


# Sessions ---------------------------------------------------------------------
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

