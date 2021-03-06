# dashboard/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class DashboardConsumer(WebsocketConsumer):
    GROUPNAME = 'dashboard'
    def connect(self):
        # Join dashboard group
        async_to_sync(self.channel_layer.group_add)(
            DashboardConsumer.GROUPNAME,
            self.channel_name
        )
        self.accept()


    def disconnect(self, close_code):
        # Leave dashboard group
        async_to_sync(self.channel_layer.group_discard)(
            DashboardConsumer.GROUPNAME,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            DashboardConsumer.GROUPNAME,
            {
                'type': 'mqtt_update',
                'message': message
            }
        )
        

    # Receive message from dashboard group
    def mqtt_update(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))