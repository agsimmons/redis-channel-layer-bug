from django.urls import re_path

from demo_app import consumers


websocket_urlpatterns = [
    re_path(
        r"ws/chat/$",
        consumers.ChatConsumer.as_asgi(),
    ),
    re_path(
        r"ws/user_log/$",
        consumers.UserLogConsumer.as_asgi(),
    ),
]
