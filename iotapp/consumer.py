from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib import messages
import json

class DashConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.accept()
        
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
        #await self.disconnect()
        pass

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val =datapoint['value']
        node=datapoint['node']
        token=datapoint['token']
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'value':val,
                'node':node,
                'token':token
            }
        )
        print (f"{node}"+" "+f"{val}")
    async def deprocessing(self,event):
        valOther=event['value']
        node=event['node']
        token=event['token']
        await self.send(text_data=json.dumps({'value':valOther,'node':node,'token':token}))