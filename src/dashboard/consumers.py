# dashboard/consumers.py
from asgiref.sync import async_to_sync
from django.conf import settings
from channels.generic.websocket import JsonWebsocketConsumer
import json
import paho.mqtt.publish as publish

devices = """{
  "devices": {
    "cloudmqtt-user": {
      "status": "good",
      "color": "#4D90FE",
      "endPoints": {
        "backDoorLock": {
          "title": "Employee Door",
          "card-type": "crouton-simple-toggle",
          "labels": {
            "false": "Unlocked",
            "true": "Locked"
          },
          "values": {
            "value": true
          },
          "icons": {
            "false": "lock",
            "true": "lock"
          }
        },
        "reset": {
          "card-type": "crouton-simple-button",
          "title": "Reset Cards",
          "values": {
            "value": false
          },
          "icons": {
            "icon": "cutlery"
          }
        },
        "drinks": {
          "units": "drinks",
          "values": {
            "value": 0
          },
          "card-type": "crouton-simple-text",
          "title": "Drinks Ordered"
        }
      },
      "description": "Kroobar's IOT devices"
    },
    "cloudmqtt-user2": {
      "status": "good",
      "color": "#ff0000",
      "endPoints": {
        "backDoorLock2": {
          "title": "Employee Door2",
          "card-type": "crouton-simple-toggle",
          "labels": {
            "false": "Unlocked2",
            "true": "Locked2"
          },
          "values": {
            "value": false
          },
          "icons": {
            "false": "lock",
            "true": "lock"
          }
        },
        "reset2": {
          "card-type": "crouton-simple-button",
          "title": "Reset Cards2",
          "values": {
            "value": true
          },
          "icons": {
            "icon": "cutlery"
          }
        },
        "drinks": {
          "units": "drinks2",
          "values": {
            "value": 100
          },
          "card-type": "crouton-simple-text",
          "title": "Drinks Ordered2"
        }
      },
      "description": "Kroobar's IOT devices2"
    }
  },
  "type": "devices"
}
"""
class DashboardConsumer(JsonWebsocketConsumer):
    GROUPNAME = 'dashboard'
    def connect(self):
        # Join dashboard group
        async_to_sync(self.channel_layer.group_add)(
            DashboardConsumer.GROUPNAME,
            self.channel_name
        )
        self.accept()

        # # TODO  for all devices in database
        publish.single(
            topic="/inbox/cloudmqtt-user/deviceInfo", 
            payload="get", 
            hostname=settings.MQTT_BROKER["HOST"],
            port=settings.MQTT_BROKER["PORT"],
            keepalive=settings.MQTT_BROKER["KEEP_ALIVE"]
        )

        # self.send(devices)


    def disconnect(self, close_code):
        # Leave dashboard group
        async_to_sync(self.channel_layer.group_discard)(
            DashboardConsumer.GROUPNAME,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive_json(self, data):
        print ("data: ", data)

        topic = "/inbox/{device_name}/{endpoint}".format(**data)
        payload = data['payload']
        print ("topic: ", topic)

        publish.single(
            topic=topic, 
            payload=payload, 
            hostname=settings.MQTT_BROKER["HOST"],
            port=settings.MQTT_BROKER["PORT"],
            keepalive=settings.MQTT_BROKER["KEEP_ALIVE"]
        )

    # Receive message from dashboard group
    def mqtt_device_update(self, event):
        device_name = event['device_name']
        endpoint = event['endpoint']
        value = event['value']

        # print("<device {} update on {}> {}".format(device_name, endpoint, value))
        # Send message to WebSocket
        self.send_json({
            'type': 'update',
            'device_name': device_name,
            'endpoint': endpoint,
            'values': json.loads(value),
        })

    # Receive message from dashboard group
    def mqtt_device_connected(self, event):
        device_name = event['device_name']
        device_info = event['device_info']

    
        print("<device {} connected>".format(device_name))
        # print(JSON.parse(device_info)['deviceInfo'])
        # Send message to WebSocket
        self.send_json({
            'type': 'devices',
            'devices': {
              device_name: json.loads(device_info)['deviceInfo']
            }
        })

        
    # Receive message from dashboard group
    def mqtt_device_disconnected(self, event):
        device_name = event['device_name']

        print("<device {} disconnected>".format(device_name))
        # Send message to WebSocket
        # self.send_json({
        #     'message': template.format(device_name)
        # })