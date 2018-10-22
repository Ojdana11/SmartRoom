from django.core.management.base import BaseCommand, CommandError
from dashboard.signals import mqtt_device_update

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print(mqtt_device_update.send(sender=self.__class__, device="devices", endpoint="endpoints", value="values"))
        self.stdout.write(self.style.SUCCESS('Successfully closed poll'))