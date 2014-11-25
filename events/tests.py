from rest_framework.test import APITestCase

from django.test import TestCase

from events.models import Device
from throne.models import Bathroom

# Create your tests here.


class EnvironmentEventAPITestCase(APITestCase):

    def setUp(self):
        self.device = Device.objects.create(device_guid='some-lengthy-text')
        Bathroom.objects.create(name='Some Room', device=self.device)

    def test_create(self):
        data = {'device_id': self.device.device_guid, 'event_type': 'lights-on'}

        response = self.client.post('/events/', data, format='json')

        assert response.status_code == 201
