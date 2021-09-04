from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *

from .models import Patient


@login_required
def index(request):
    return render(request, "patients/home.html")


class CreatePatient(LoginRequiredMixin, CreateView):
    model = Patient
    context_object_name = "patient"
    fields = ["name", "mobile", "email", "gender", "address"]


class ViewPatient(LoginRequiredMixin, DetailView):
    model = Patient
    context_object_name = "patient"


class UpdatePatient(LoginRequiredMixin, UpdateView):
    model = Patient
    context_object_name = "patient"
