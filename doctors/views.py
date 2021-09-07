from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import *

import hospital_manage.settings as global_settings
from .forms import CreateDoctorForm, UpdateDoctorForm
from .models import Doctor


class DoctorCreate(LoginRequiredMixin, CreateView):
    model = Doctor
    context_object_name = "doctor"
    form_class = CreateDoctorForm

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


class DoctorDetail(LoginRequiredMixin, DetailView):
    model = Doctor
    context_object_name = "doctor"


class DoctorUpdate(LoginRequiredMixin, UpdateView):
    template_name = "doctors/doctor_form.html"
    model = Doctor
    context_object_name = "doctor"
    form_class = UpdateDoctorForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["update_mode"] = True
        return data


class DoctorList(LoginRequiredMixin, ListView):
    model = Doctor
    context_object_name = "doctors"
    ordering = ["name"]
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            if str(query).isnumeric():
                result = Doctor.objects.filter(Q(pk=query) | Q(name__icontains=query))
            else:
                result = Doctor.objects.filter(Q(name__icontains=query))
        else:
            result = Doctor.objects.all()
        return result.order_by("name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context


def doctor_archive(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if doctor and not doctor.archived:
        doctor.archived = True
        doctor.archived_by = request.user
        doctor.date_archived = timezone.now()
        doctor.save()
        messages.warning(request, f"Doctor {pk} archived!")
    return redirect("doctor-detail", pk=pk)
