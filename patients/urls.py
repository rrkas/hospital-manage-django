from django.urls import path

from . import views

urlpatterns = [
    path("", views.PatientList.as_view(), name="patient-home"),
    path("new/", views.PatientCreate.as_view(), name="patient-create"),
    path("<int:pk>/", views.PatientDetail.as_view(), name="patient-detail"),
    path("<int:pk>/update", views.PatientUpdate.as_view(), name="patient-update"),
    path("<int:pk>/archive", views.patient_archive, name="patient-archive"),
]
