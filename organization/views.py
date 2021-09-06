from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from departments.models import Department
from doctors.models import Doctor
from patients.models import Patient
from staffs.models import Profile
from .models import OrganizationItem

org = "organization"


@login_required
def home(request):
    context = {
        "groups": [
            OrganizationItem(
                "Departments", "department-home", Department.objects.all().count()
            ),
        ],
        "individuals": [
            OrganizationItem("Staffs", "staff-home", Profile.objects.all().count()),
            OrganizationItem("Patients", "patient-home", Patient.objects.all().count()),
            OrganizationItem("Doctors", "doctor-home", Doctor.objects.all().count()),
        ],
    }
    return render(request, f"{org}/home.html", context=context)
