"""
WSGI config for check_apache project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import mod_wsgi
print(mod_wsgi.version)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'check_apache.settings')
from django.contrib.auth.handlers.modwsgi import check_password
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
