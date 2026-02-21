"""
WSGI config for slms project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
# import os
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'slms.settings')
# application = get_wsgi_application()

# slms/wsgi.py
import os
import sys
import traceback
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'slms.settings')

try:
    app = get_wsgi_application()
    print("Django application loaded successfully")
except Exception as e:
    print(f"Error loading Django application: {e}")
    traceback.print_exc()
    raise
