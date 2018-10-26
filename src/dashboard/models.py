from django.db import models


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=100)
    status = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_connected = models.BooleanField

    def get_endpoints(self):
        return Endpoint.objects.filter(device_id=self.device_id)


class Endpoint(models.Model):
    endpoint_id = models.AutoField(primary_key=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    endpoint_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    card_type = models.CharField(max_length=255)
    units = models.CharField(max_length=255)

    def get_values(self):
        return EndpointsValue.objects.filter(endpoint_id=self.id)


class EndpointsValue(models.Model):
    endpoint_id = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
