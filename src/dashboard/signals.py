# dashboard/signals.py
from django.dispatch import Signal

mqtt_device_update = Signal(providing_args=["device", "endpoint", "value"])