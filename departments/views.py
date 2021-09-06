from django.contrib import messages
from django.contrib.auth.mixins import *
from django.db.models import Q
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import *

import hospital_manage.settings as global_settings
from .forms import CreateDepartmentForm, UpdateDepartmentForm
from .models import Department


class DepartmentCreate(LoginRequiredMixin, CreateView):
    model = Department
    context_object_name = "department"
    form_class = CreateDepartmentForm

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


class DepartmentDetail(LoginRequiredMixin, DetailView):
    model = Department
    context_object_name = "department"


class DepartmentUpdate(LoginRequiredMixin, UpdateView):
    template_name = "departments/department_form.html"
    model = Department
    context_object_name = "department"
    form_class = UpdateDepartmentForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["update_mode"] = True
        return data


class DepartmentList(LoginRequiredMixin, ListView):
    model = Department
    context_object_name = "departments"
    ordering = ["id"]
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            if str(query).isnumeric():
                result = Department.objects.filter(
                    Q(pk=query) | Q(name__icontains=query)
                )
            else:
                result = Department.objects.filter(Q(name__icontains=query))
        else:
            result = Department.objects.all()
        return result.order_by("id")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context


def department_archive(request, pk):
    department = Department.objects.get(pk=pk)
    if department and not department.archived:
        department.archived = True
        department.archived_by = request.user
        department.date_archived = timezone.now()
        department.save()
        messages.warning(request, f"Department {pk} archived!")
    return redirect("department-detail", pk=pk)
