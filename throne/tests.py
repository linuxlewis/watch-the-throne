from datetime import timedelta

from django.test import TestCase

# Create your tests here.

from events.models import Device, EnvironmentEvent
from throne.models import Bathroom


class BathroomTestCase(TestCase):

    def setUp(self):
        # make a device
        d = Device.objects.create(device_guid='some-lengthy-text')
        # make a bathroom
        self.bathroom = Bathroom.objects.create(name='Test Room', device=d)

    def test_available(self):
        # make  events
        start = EnvironmentEvent()
        start.event_type = 'lights-off'
        start.device = self.bathroom.device
        start.save()

        self.assertEqual(self.bathroom.available, True)

    def test_last_cycle(self):
        # make  events
        EnvironmentEvent.objects.create(event_type='lights-off', device=self.bathroom.device)
        start = EnvironmentEvent.objects.create(event_type='lights-on', device=self.bathroom.device)
        end = EnvironmentEvent.objects.create(event_type='lights-off', device=self.bathroom.device)

        self.assertEqual(self.bathroom.last_cycle_time, end.created_on - start.created_on)

    def test_cool_down(self):
        # make  events
        EnvironmentEvent.objects.create(event_type='lights-off', device=self.bathroom.device)
        EnvironmentEvent.objects.create(event_type='lights-on', device=self.bathroom.device)
        EnvironmentEvent.objects.create(event_type='lights-off', device=self.bathroom.device)
        self.assertTrue(self.bathroom.cool_down)
