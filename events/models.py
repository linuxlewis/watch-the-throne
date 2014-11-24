from datetime import datetime

from model_utils import Choices
from django.db import models


class EnvironmentEvent(models.Model):

    TYPES = Choices('lights-on', 'lights-off')
    created_on = models.DateTimeField(auto_now_add=True, default=datetime.now())
    device_id = models.CharField(max_length=36, null=False, default='some-value')
    event_type = models.CharField(choices=TYPES, max_length=200)
