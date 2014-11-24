from rest_framework import viewsets, serializers

from django.shortcuts import render

from events.models import EnvironmentEvent


class EnvironmentEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnvironmentEvent


class EnvironmentEventViewSet(viewsets.ModelViewSet):

    queryset = EnvironmentEvent.objects.all()
    serializer_class = EnvironmentEventSerializer
