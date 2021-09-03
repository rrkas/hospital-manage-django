from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="patient-home"),
    path("new/", views.CreatePatient.as_view(), name="patient-create"),
    path("<int:pk>/", views.ViewPatient.as_view(), name="patient-view"),
    path("<int:pk>/update", views.UpdatePatient.as_view(), name="patient-update"),
    path("<int:pk>/archive", views.ArchivePatient.as_view(), name="patient-archive"),
]
