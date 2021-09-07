from django.contrib import admin

from inventory.models import Manufacturer, Equipment, Medicine

admin.site.register(Manufacturer)
admin.site.register(Equipment)
admin.site.register(Medicine)
