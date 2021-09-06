from django.urls import path

from . import views

urlpatterns = [
    path("", views.DepartmentList.as_view(), name="department-home"),
    path("new/", views.DepartmentCreate.as_view(), name="department-create"),
    path("<int:pk>/", views.DepartmentDetail.as_view(), name="department-detail"),
    path("<int:pk>/update", views.DepartmentUpdate.as_view(), name="department-update"),
    path("<int:pk>/archive", views.department_archive, name="department-archive"),
]
