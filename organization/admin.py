from django.contrib import admin
from .models import Doctor, Department, Patient, Profile

admin.site.register(Profile)
admin.site.register(Patient)
admin.site.register(Department)
admin.site.register(Doctor)
