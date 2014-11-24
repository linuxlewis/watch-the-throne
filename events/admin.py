from django.contrib import admin

from events.models import EnvironmentEvent

# Register your models here.


@admin.register(EnvironmentEvent)
class EnvironmentEventAdmin(admin.ModelAdmin):
    pass
