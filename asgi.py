"""
ASGI config for poligonosapp_with_django_folium project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poligonosapp_with_django_folium.settings')

application = get_asgi_application()
