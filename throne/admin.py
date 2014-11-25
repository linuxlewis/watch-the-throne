from django.contrib import admin

from throne.models import Bathroom

@admin.register(Bathroom)
class BathroomAdmin(admin.ModelAdmin):
    pass
