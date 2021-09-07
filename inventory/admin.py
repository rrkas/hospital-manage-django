from django.contrib import admin

from inventory.models import Manufacturer, Equipment

admin.site.register(Manufacturer)
admin.site.register(Equipment)
