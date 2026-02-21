from django.shortcuts import render
from django.http import JsonResponse
from django.db import connections
from django.conf import settings
import os
import sys

def debug_info(request):
    """Debug endpoint to check system status"""
    info = {
        'status': 'ok',
        'debug_mode': settings.DEBUG,
        'database': {
            'engine': settings.DATABASES['default']['ENGINE'],
            'name': settings.DATABASES['default']['NAME'],
            'exists': os.path.exists(settings.DATABASES['default']['NAME']),
        },
        'static': {
            'root': settings.STATIC_ROOT,
            'exists': os.path.exists(settings.STATIC_ROOT) if settings.STATIC_ROOT else False,
        },
        'environment': {
            'vercel_env': os.environ.get('VERCEL_ENV', 'not set'),
            'python_version': sys.version,
        }
    }
    
    # Test database connection
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            info['database']['connection'] = 'ok'
    except Exception as e:
        info['database']['connection'] = str(e)
        info['status'] = 'error'
    
    return JsonResponse(info)
