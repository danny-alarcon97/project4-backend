import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp_django.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websockets": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websockets_urlpatterns
        )
    )
})

