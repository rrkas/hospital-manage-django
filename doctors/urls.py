from django.urls import path

from . import views

urlpatterns = [
    path("", views.DoctorList.as_view(), name="doctor-home"),
    path("new/", views.DoctorCreate.as_view(), name="doctor-create"),
    path("<int:pk>/", views.DoctorDetail.as_view(), name="doctor-detail"),
    path("<int:pk>/update", views.DoctorUpdate.as_view(), name="doctor-update"),
    path("<int:pk>/archive", views.doctor_archive, name="doctor-archive"),
]
