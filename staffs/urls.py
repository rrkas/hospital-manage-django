from django.urls import path

from .views import *

urlpatterns = [
    path("", ProfileList.as_view(), name="staff-home"),
    path("<int:pk>/", ProfileDetail.as_view(), name="staff-detail"),
]
