import random
import string

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


CHAT_GROUP = "chat"
USER_LOG_GROUP = "user_log"


async def get_random_username():
    return "".join(random.choice(string.ascii_uppercase) for _ in range(4))



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = await get_random_username()

        await self.channel_layer.group_add(CHAT_GROUP, self.channel_name)

        await self.accept()

        await get_channel_layer().group_send(
            CHAT_GROUP,
            {
                "type": "chat.message",
                "message": f"SERVER: User {self.username} has connected"
            },
        )
        await get_channel_layer().group_send(
            USER_LOG_GROUP,
            {
                "type": "userlog.message",
                "message": f"SERVER: User {self.username} has connected"
            },
        )

    async def disconnect(self, code):
        await self.channel_layer.group_discard(CHAT_GROUP, self.channel_name)

        await get_channel_layer().group_send(
            CHAT_GROUP,
            {
                "type": "chat.message",
                "message": f"SERVER: User {self.username} has disconnected"
            },
        )
        await get_channel_layer().group_send(
            USER_LOG_GROUP,
            {
                "type": "userlog.message",
                "message": f"SERVER: User {self.username} has disconnected"
            },
        )

    async def receive(self, text_data=None, bytes_data=None):
        await get_channel_layer().group_send(
            CHAT_GROUP,
            {
                "type": "chat.message",
                "message": f"{self.username}: {text_data}",
            },
        )

    async def chat_message(self, event):
        await self.send(event["message"])


class UserLogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username = await get_random_username()

        await self.channel_layer.group_add(USER_LOG_GROUP, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(USER_LOG_GROUP, self.channel_name)

    async def userlog_message(self, event):
        print("userlog_message Triggered")
        await self.send(event["message"])
