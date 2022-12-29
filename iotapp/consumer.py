from channels.generic.websocket import AsyncJsonWebsocketConsumer
#from channels.db import database_sync_to_async
from django.contrib import messages
import json
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
#from iotapp.models import Token
class DashConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        me=self.scope['user']
        device_username=str(self.scope['url_route']['kwargs']['username'])
        self.room_name=f"personal_dash_{device_username}"
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name,
        )
        print(f'[{self.channel_name}]-You are connected')
        await self.accept()
        
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name,
           
        )
        #await self.disconnect()
        pass
    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val =datapoint['value']
        node=datapoint['node']
        #token_recv=datapoint['token']
    
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type':'deprocessing',
                'value':val,
                'node':node,
            }
        )
        print(f"{node}"+ " "+f"{val}")
    async def deprocessing(self,event):
        valOther=event['value']
        node=event['node']
        await self.send(text_data=json.dumps({'value':valOther,'node':node }))
        print("send")