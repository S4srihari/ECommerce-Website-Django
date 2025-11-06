"""
ASGI config for ecomm project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more documentation on this file, visit
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecomm.settings')

application = get_asgi_application()