from datetime import datetime

from model_utils import Choices
from django.db import models


class Device(models.Model):
    device_guid = models.CharField(max_length=36, unique=True)


class EnvironmentEvent(models.Model):

    TYPES = Choices('lights-on', 'lights-off', 'sound-on', 'sound-off')
    created_on = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device, db_column='other_device_id')
    event_type = models.CharField(choices=TYPES, max_length=200)
