import os
from tesselapi.settings import BASE_DIR

from events.models import EnvironmentEvent

from django.db import models


class Bathroom(models.Model):

    name = models.CharField(max_length=200)
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#filepathfield
    picture = models.FilePathField(path=os.path.join(BASE_DIR, 'throne/static/bathroom_pics'))
    device = models.ForeignKey('events.Device')

    @property
    def available(self):
        return self.device.environmentevent_set.latest('created_on').event_type == 'lights-off'
