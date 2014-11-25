from events.models import EnvironmentEvent

from django.db import models

# Create your models here.


class Bathroom(models.Model):

    name = models.CharField(max_length=200)
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#filepathfield
    device = models.ForeignKey('events.Device')

    @property
    def available(self):
        pass


    @property
    def state(self):
        #self.device.envrionmentevent_set.all()
        pass
