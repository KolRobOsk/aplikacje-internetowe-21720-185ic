import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chatter_21720.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab8_kolke.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            chatter_21720.routing.websocket_urlpatterns
        )
    ),
})
