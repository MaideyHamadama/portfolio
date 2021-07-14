"""
WSGI config for Portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

"""For local development"""
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')
#application = get_wsgi_application()
"""For live development"""
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Portfolio.settings")
application = Cling(get_wsgi_application())
