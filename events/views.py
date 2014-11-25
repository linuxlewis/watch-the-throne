from rest_framework import viewsets, serializers

from django.shortcuts import render

from events.models import EnvironmentEvent, Device


class EnvironmentEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnvironmentEvent


class EnvironmentEventViewSet(viewsets.ModelViewSet):

    queryset = EnvironmentEvent.objects.all()
    serializer_class = EnvironmentEventSerializer

    def create(self, request, *args, **kwargs):
        # add the device to the request data from guid
        if 'device_id' in request.DATA:
            try:
                request.DATA['device'] = Device.objects.get(device_guid=request.DATA['device_id']).id
            except Device.DoesNotExist:
                pass

        return super(viewsets.ModelViewSet, self).create(request, *args, **kwargs)
