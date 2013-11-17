#_-*- encoding:utf-8 -*-
from os.path import realpath, dirname, join


location = lambda x: realpath(
    join(dirname(dirname(realpath(__file__))), x))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(location('../'), 'android.db'),
    }
}

# DEBUG = True
DEBUG = True
TEMPLATE_DEBUG = True