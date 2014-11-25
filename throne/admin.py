from django.contrib import admin

from throne.models import Bathroom, BathroomAlert


@admin.register(Bathroom)
class BathroomAdmin(admin.ModelAdmin):
    pass


@admin.register(BathroomAlert)
class BathroomAlertAdmin(admin.ModelAdmin):
    pass
