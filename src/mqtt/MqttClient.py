import paho.mqtt.client as mqtt
from channels.layers import get_channel_layer
from dashboard.consumers import DashboardConsumer
from asgiref.sync import async_to_sync

class MqttClient(mqtt.Client):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.channel_layer = get_channel_layer()

    def on_connect(self, mqttc, obj, flags, rc):
        self.ctx.stdout.write(self.ctx.style.SUCCESS('Successfully connected to mqtt broker'))

        self.subscribe("/xd")

    def on_message(self, mqttc, obj, msg):
        self.ctx.stdout.write("{} {} {}".format(msg.topic, msg.qos, msg.payload))
        if msg.topic == "/xd":
            try:
                payload = msg.payload.decode("ascii")
                async_to_sync(self.channel_layer.group_send)(
                    DashboardConsumer.GROUPNAME, 
                    {
                        "type": "mqtt_update", 
                        "message": payload,
                    }
                )
            except Exception as e:
                 self.ctx.stdout.write(self.ctx.style.ERROR("Failed to process payload %s" % e))

    # def on_publish(self, mqttc, obj, mid):
    #     print("mid: "+str(mid))

    # def on_subscribe(self, mqttc, obj, mid, granted_qos):
    #     print("Subscribed: "+str(mid)+" "+str(granted_qos))

    # def on_log(self, mqttc, obj, level, string):
    #     print(string)

    def run(self):
        # self.enable_logger()
        self.connect("mqtt", 1883, 60)

        self.loop_forever()