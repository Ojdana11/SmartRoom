from django.core.management.base import BaseCommand, CommandError
from channels.layers import get_channel_layer
from dashboard.consumers import DashboardConsumer
from asgiref.sync import async_to_sync
from mqtt.MqttClient import MqttClient

class Command(BaseCommand):
    help = 'Runs mqtt client'

    def handle(self, *args, **options):
        mqttc = MqttClient(self)
        mqttc.run()
        