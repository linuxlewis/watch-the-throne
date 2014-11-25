from datetime import datetime

from model_utils import Choices
from django.db import models


class Device(models.Model):
    device_guid = models.CharField(max_length=36)


class EnvironmentEvent(models.Model):

    TYPES = Choices('lights-on', 'lights-off', 'sound-on', 'sound-off')
    created_on = models.DateTimeField(auto_now_add=True, default=datetime.now())
    device = models.ForeignKey(Device, db_column='other_device_id')
    #device_id = models.CharField(max_length=36, null=False, default='some-value')
    event_type = models.CharField(choices=TYPES, max_length=200)
