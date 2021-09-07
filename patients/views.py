from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import *

import hospital_manage.settings as global_settings
from .forms import CreatePatientForm, UpdatePatientForm
from .models import Patient


class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    context_object_name = "patient"
    form_class = CreatePatientForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["update_mode"] = False
        return data

    def form_valid(self, form):
        valid = super().form_valid(form)
        if valid:
            data = form.save(commit=False)
            data.created_by = self.request.user
            data.save()
        return valid


class PatientDetail(LoginRequiredMixin, DetailView):
    model = Patient
    context_object_name = "patient"


class PatientUpdate(LoginRequiredMixin, UpdateView):
    template_name = "patients/patient_form.html"
    model = Patient
    context_object_name = "patient"
    form_class = UpdatePatientForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["update_mode"] = True
        return data


class PatientList(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = "patients"
    ordering = ["name"]
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            if str(query).isnumeric():
                result = Patient.objects.filter(Q(pk=query) | Q(name__icontains=query))
            else:
                result = Patient.objects.filter(Q(name__icontains=query))
        else:
            result = Patient.objects.all()
        return result.order_by("name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context


def patient_archive(request, pk):
    patient = Patient.objects.get(pk=pk)
    if patient and not patient.archived:
        patient.archived = True
        patient.archived_by = request.user
        patient.date_archived = timezone.now()
        patient.save()
        messages.warning(request, f"Patient {pk} archived!")
    return redirect("patient-detail", pk=pk)
