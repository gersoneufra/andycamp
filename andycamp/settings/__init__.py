# -*- encoding:utf-8 -*-
import os

DJANGO_ENVIRONMENT = os.environ.get('DJANGO_ENVIRONMENT', 'develop')

print "Servidor en:  --->>",DJANGO_ENVIRONMENT

if DJANGO_ENVIRONMENT == 'production':
    from .production import *
elif DJANGO_ENVIRONMENT == 'testing':
    from .testing import *
elif DJANGO_ENVIRONMENT == 'develop':
    from .develop import *
else:
    import sys
    sys.stderr.write("Unknow project environment \"%s\"\n" % DJANGO_ENVIRONMENT)
    sys.exit(1)


if DJANGO_ENVIRONMENT == 'develop':
    try:
        from .local import *
    except ImportError:
        import sys
        sys.stderr.write("Project has no local settings file local.py")
        sys.exit(1)