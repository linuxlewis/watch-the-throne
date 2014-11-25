from rest_framework import viewsets, serializers

from django.shortcuts import render

from throne.models import Bathroom


class BathroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bathroom


class BathroomViewSet(viewsets.ModelViewSet):

    queryset = Bathroom.objects.all()
    serializer_class = BathroomSerializer
