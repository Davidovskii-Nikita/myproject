from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
#from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
#from myprojectder.main.routing import websockets

from main import consumers

websocket_urlPattern=[
	path ('ws/data/', consumers.MainConsumer),
]

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})