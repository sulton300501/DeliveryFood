"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.auth import (
    AuthMiddlewareStack,  # foudalanuvchilarni tanip olish uchun ishlatiladigan middlware
)
from channels.routing import ProtocolTypeRouter, URLRouter

import django
from django.core.asgi import get_asgi_application

from apps.notifications import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.develop")

django.setup()


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # ASGI uchun to'g'ri bo'lishi kerak
        "websocket": AuthMiddlewareStack(
            URLRouter(routing.websocket_urlpatterns)  # marshrut yani web socker so'rovlariga yunaltruvchi
        ),
    }
)
