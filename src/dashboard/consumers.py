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
                'type': 'caht_update',
                'message': message
            }
        )

    def caht_update(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    # Receive message from dashboard group
    def mqtt_device_update(self, event):
        device_name = event['device_name']
        endpoint = event['endpoint']
        value = event['value']

        template = "<device {} update on {} endpoint> {}"
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': template.format(device_name, endpoint, value)
        }))

    # Receive message from dashboard group
    def mqtt_device_connected(self, event):
        device_name = event['device_name']

        template = "<device {} connected>"
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': template.format(device_name)
        }))

        
    # Receive message from dashboard group
    def mqtt_device_disconnected(self, event):
        device_name = event['device_name']

        template = "<device {} disconnected>"
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': template.format(device_name)
        }))