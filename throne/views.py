import os
from rest_framework import viewsets, serializers

from django.shortcuts import render
from django.views.generic.base import TemplateView

from throne.models import Bathroom, BathroomAlert
from tesselapi.settings import BASE_DIR


class BathroomSerializer(serializers.ModelSerializer):

    available = serializers.Field(source='available')
    last_cycle_time = serializers.Field(source='last_cycle_time')
    cool_down = serializers.Field(source='cool_down')

    class Meta:
        model = Bathroom
        fields = ('id', 'name', 'picture', 'device', 'available', 'last_cycle_time', 'cool_down')


class BathroomAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = BathroomAlert


class BathroomViewSet(viewsets.ModelViewSet):

    queryset = Bathroom.objects.all()
    serializer_class = BathroomSerializer


class BathroomAlertViewSet(viewsets.ModelViewSet):

    queryset = BathroomAlert.objects.all()
    serializer_class = BathroomAlertSerializer


class UiView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(UiView, self).get_context_data(**kwargs)
        context['bathroom_pic_location'] = os.path.join(BASE_DIR, 'throne/static/bathroom_pics')
        return context
