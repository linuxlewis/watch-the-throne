import os

from django.db import models
from django.db.models import Q

from tesselapi.settings import BASE_DIR

from events.models import EnvironmentEvent


class Bathroom(models.Model):

    name = models.CharField(max_length=200)
    # https://docs.djangoproject.com/en/dev/ref/models/fields/#filepathfield
    picture = models.FilePathField(path=os.path.join(BASE_DIR, 'throne/static/bathroom_pics'))
    device = models.ForeignKey('events.Device')

    @property
    def available(self):
        return self.device.environmentevent_set.latest('created_on').event_type == 'lights-off'

    @property
    def cool_down(self):
        # half life of the last trip % 10
        minutes = self.last_cycle_time.total_seconds() / 60
        return minutes / 2 % 10

    @property
    def last_cycle_time(self):
        '''
        returns timedelta between last 'lights-off' event with the previous
        'lights-on' events.
        '''

        last_5_events = self.device.environmentevent_set.filter(Q(event_type='lights-off') | Q(event_type='lights-on')).order_by('-created_on').all()[:5]
        last_5_events = list(last_5_events)

        try:
            assert len(last_5_events) >= 3
        except AssertionError:
            return None

        end_event = last_5_events.pop(0)
        # if currently mid cycle
        if end_event.event_type == 'lights-on':
            end_event = last_5_events.pop(0)
        start_event = last_5_events.pop(0)

        return end_event.created_on - start_event.created_on
