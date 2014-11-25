from rest_framework import viewsets, serializers

from django.shortcuts import render

from throne.models import Bathroom, BathroomAlert


class BathroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bathroom

class BathroomAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = BathroomAlert


class BathroomViewSet(viewsets.ModelViewSet):

    queryset = Bathroom.objects.all()
    serializer_class = BathroomSerializer


class BathroomAlertViewSet(viewsets.ModelViewSet):

    queryset = BathroomAlert.objects.all()
    serailzer_class = BathroomAlertSerializer
