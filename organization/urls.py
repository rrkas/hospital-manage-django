from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="org-home"),
]

doctor = "doctors/"
urlpatterns += [
    path(doctor + "", views.DoctorList.as_view(), name="doctor-home"),
    path(doctor + "new/", views.DoctorCreate.as_view(), name="doctor-create"),
    path(doctor + "<int:pk>/", views.DoctorDetail.as_view(), name="doctor-detail"),
    path(
        doctor + "<int:pk>/update", views.DoctorUpdate.as_view(), name="doctor-update"
    ),
    path(doctor + "<int:pk>/archive", views.doctor_archive, name="doctor-archive"),
]

dept = "departments/"
urlpatterns += [
    path(dept + "", views.DepartmentList.as_view(), name="department-home"),
    path(dept + "new/", views.DepartmentCreate.as_view(), name="department-create"),
    path(
        dept + "<int:pk>/", views.DepartmentDetail.as_view(), name="department-detail"
    ),
    path(
        dept + "<int:pk>/update",
        views.DepartmentUpdate.as_view(),
        name="department-update",
    ),
    path(
        dept + "<int:pk>/archive", views.department_archive, name="department-archive"
    ),
]

patients = "patients/"
urlpatterns += [
    path(patients + "", views.PatientList.as_view(), name="patient-home"),
    path(patients + "new/", views.PatientCreate.as_view(), name="patient-create"),
    path(patients + "<int:pk>/", views.PatientDetail.as_view(), name="patient-detail"),
    path(
        patients + "<int:pk>/update",
        views.PatientUpdate.as_view(),
        name="patient-update",
    ),
    path(patients + "<int:pk>/archive", views.patient_archive, name="patient-archive"),
]

staffs = "staffs/"
urlpatterns += [
    path(staffs + "", views.StaffList.as_view(), name="staff-home"),
    path(staffs + "<int:pk>/", views.StaffDetail.as_view(), name="staff-detail"),
    path(staffs + "<int:pk>/update", views.staff_edit, name="staff-update"),
]
