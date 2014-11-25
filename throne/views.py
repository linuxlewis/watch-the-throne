from rest_framework import viewsets, serializers

from django.shortcuts import render

from throne.models import Bathroom, BathroomAlert


class BathroomSerializer(serializers.ModelSerializer):

    available = serializers.Field(source='available')
    last_cycle_time = serializers.Field(source='last_cycle_time')
    cool_down = serializers.Field(source='cool_down')

    class Meta:
        model = Bathroom
        fields = ('name', 'picture', 'device', 'available', 'last_cycle_time', 'cool_down')


class BathroomAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = BathroomAlert


class BathroomViewSet(viewsets.ModelViewSet):

    queryset = Bathroom.objects.all()
    serializer_class = BathroomSerializer


class BathroomAlertViewSet(viewsets.ModelViewSet):

    queryset = BathroomAlert.objects.all()
    serailzer_class = BathroomAlertSerializer
