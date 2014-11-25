from django.contrib import admin

from events.models import EnvironmentEvent, Device


@admin.register(EnvironmentEvent)
class EnvironmentEventAdmin(admin.ModelAdmin):
    pass

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass