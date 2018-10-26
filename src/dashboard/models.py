from django.utils import timezone


from django.db import models


class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=100)
    status = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    is_connected = models.BooleanField(default=False)

    def get_endpoints(self):
        return Endpoint.objects.filter(device_id=self.device_id)


class Endpoint(models.Model):
    endpoint_id = models.AutoField(primary_key=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    endpoint_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255, null=True)
    card_type = models.CharField(max_length=255, null=True)
    units = models.CharField(max_length=255, null=True)

    def get_values(self):
        return EndpointsValue.objects.filter(endpoint_id=self.endpoint_id)

    def get_current_value(self):
        return EndpointsValue.objects.order_by('date').filter(endpoint_id=self.endpoint_id)[0]

    def get_values_for_date(self, first_date, second_date):
        return EndpointsValue.objects.order_by('date')\
            .filter(endpoint_id=self.endpoint_id, date__lte=second_date, date__gte=first_date)


class EndpointsValue(models.Model):
    endpoint_id = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    value_name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
