from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.CreatePatient.as_view(), name="patient-create"),
    path("<int:pk>/", views.ViewPatient.as_view(), name="patient-view"),
]
