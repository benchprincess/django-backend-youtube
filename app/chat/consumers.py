# 채널에서 소켓을 연결하는 역할을 Consumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    # 소켓 연결
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_'+str(self.room_id)

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = text_data_json.get('message')
            
        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'message': msg
        })
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    

    async def chat_message(self, event):
        msg = event['message']
        email = event['email']

        await self.send(text_data=json.dumps({
            'type': 'chat.message',
            'message': msg,
            'email': email
        }))