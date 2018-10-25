import paho.mqtt.client as mqtt
from channels.layers import get_channel_layer
from dashboard.consumers import DashboardConsumer
from asgiref.sync import async_to_sync
from django.conf import settings

class MqttClient(mqtt.Client):
    devices = ["cloudmqtt-user"]

    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.channel_layer = get_channel_layer()

    def on_connect(self, mqttc, obj, flags, rc):
        self.ctx.stdout.write(self.ctx.style.SUCCESS('Successfully connected to mqtt broker'))

        for device_name in MqttClient.devices:
            self.subscribe("/outbox/{}/+".format(device_name))
            # ask for device info
            self.publish("/inbox/{}/deviceInfo".format(device_name), "get")

    def on_message(self, mqttc, obj, msg):
        self.ctx.stdout.write("{} {} {}".format(msg.topic, msg.qos, msg.payload))
        _, box, device_name, endpoint = msg.topic.split('/')

        if box == "outbox" and endpoint == "deviceInfo":
            device_info = msg.payload.decode("ascii")
            if device_info == 'get':
                return
                
            self.dashboard_send({
                "type": "mqtt_device_connected", 
                "device_name": device_name,
                "device_info": device_info,
            })
            return 

        if box == "outbox" and endpoint == "lwt":
            payload = msg.payload.decode("ascii")
            self.dashboard_send({
                "type": "mqtt_device_disconnected", 
                "device_name": device_name,
            })
            return 

        self.dashboard_send({
            "type": "mqtt_device_update", 
            "device_name": device_name,
            "endpoint": endpoint,
            "value": msg.payload.decode("ascii"),
        })
            # try:
            # except Exception as e:
                #  self.ctx.stdout.write(self.ctx.style.ERROR("Failed to process payload %s" % e))

    def dashboard_send(self, data):
        async_to_sync(self.channel_layer.group_send)(
            DashboardConsumer.GROUPNAME, 
            data
        )

    def run(self):
        # self.enable_logger()
        self.connect(
            settings.MQTT_BROKER["HOST"], 
            settings.MQTT_BROKER["PORT"], 
            settings.MQTT_BROKER["KEEP_ALIVE"], 
        )

        self.loop_forever()