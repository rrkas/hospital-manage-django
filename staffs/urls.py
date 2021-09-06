from django.urls import path

from .views import *

urlpatterns = [
    path("", StaffList.as_view(), name="staff-home"),
    path("<int:pk>/", StaffDetail.as_view(), name="staff-detail"),
    path("<int:pk>/update", staff_edit, name="staff-update"),
]
