"""
ASGI config for clonestagram project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clonestagram.settings")


get_asgi_application()


from channels.auth import AuthMiddlewareStack   # noqa
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa

import messenger.routing    # noqa

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clonestagram.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            messenger.routing.websocket_urlpatterns
        )
    ),
})
