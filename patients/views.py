from django.contrib.auth.mixins import *
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *

from .models import Patient


def index(request):
    return render(request, "patients/home.html")


class CreatePatient(LoginRequiredMixin, CreateView):
    model = Patient
    context_object_name = "patient"
    fields = ["name", "mobile", "email", "gender", "address"]

    def get_success_url(self):
        return reverse("patient-view", kwargs={"pk": self.object.id})


class ViewPatient(LoginRequiredMixin, DetailView):
    model = Patient
    context_object_name = "patient"


class UpdatePatient(LoginRequiredMixin, UpdateView):
    model = Patient
    context_object_name = "patient"

    def get_success_url(self):
        return reverse("patient-view", kwargs={"pk": self.object.id})


class ArchivePatient(LoginRequiredMixin, View):
    model = Patient
