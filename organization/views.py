from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from .forms import *
from .models import *

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


# ================== Users =========================


def register(request):
    if request.method == "POST":
        u_form = UserRegisterForm(request.POST)
        p_form = ProfileCreateForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            form = p_form.instance
            form.user = user
            form.save()
            messages.success(
                request,
                "Account created successfully! You will be able to login once activated by admins!",
            )
            return redirect("login")
    else:
        u_form = UserRegisterForm()
        p_form = ProfileCreateForm()
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, f"staffs/register.html", context)


# ================== Staffs =========================


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Account updated successfully!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "staffs/profile.html", context)


class StaffList(LoginRequiredMixin, ListView):
    model = Profile
    template_name = "staffs/staff_list.html"
    context_object_name = "staffs"
    ordering = ["first_name", "last_name"]
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            if str(query).isnumeric():
                result = self.model.objects.filter(
                    Q(pk=query)
                    | Q(user__first_name__icontains=query)
                    | Q(user__last_name__icontains=query)
                    | Q(user__username__icontains=query)
                )
            else:
                result = self.model.objects.filter(
                    Q(user__first_name__icontains=query)
                    | Q(user__last_name__icontains=query)
                    | Q(user__username__icontains=query)
                )
        else:
            result = self.model.objects.all()
        return result.order_by("user__first_name", "user__last_name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context


class StaffDetail(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "staffs/staff_detail.html"
    context_object_name = "staff"


@login_required
def staff_edit(request, pk):
    profile_obj = Profile.objects.get(pk=pk)
    if request.method == "POST":
        u_form = StaffUserUpdateForm(request.POST, instance=profile_obj.user)
        p_form = StaffProfileUpdateForm(
            request.POST, request.FILES, instance=profile_obj
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Account updated successfully!")
            return redirect("staff-detail", pk=pk)
    else:
        u_form = StaffUserUpdateForm(instance=profile_obj.user)
        p_form = StaffProfileUpdateForm(instance=profile_obj)
    context = {
        "u_form": u_form,
        "p_form": p_form,
        "pk": pk,
    }
    return render(request, "staffs/staff_form.html", context)


# ================== Doctors =========================


class DoctorCreate(LoginRequiredMixin, CreateView):
    model = Doctor
    context_object_name = "doctor"
    template_name = "doctors/doctor_form.html"
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
    template_name = "doctors/doctor_detail.html"
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
    template_name = "doctors/doctor_list.html"
    ordering = ["name"]
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            if str(query).isnumeric():
                result = self.model.objects.filter(Q(pk=query) | Q(name__icontains=query))
            else:
                result = self.model.objects.filter(Q(name__icontains=query))
        else:
            result = self.model.objects.all()
        return result.order_by("name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context


@login_required
def doctor_archive(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if doctor and not doctor.archived:
        doctor.archived = True
        doctor.archived_by = request.user
        doctor.date_archived = timezone.now()
        doctor.save()
        messages.warning(request, f"Doctor {pk} archived!")
    return redirect("doctor-detail", pk=pk)


# ================== Departments =========================


class DepartmentCreate(LoginRequiredMixin, CreateView):
    model = Department
    context_object_name = "department"
    template_name = "departments/department_form.html"
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
    template_name = "departments/department_detail.html"
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
    template_name = "departments/department_list.html"
    ordering = ["name"]
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            if str(query).isnumeric():
                result = self.model.objects.filter(
                    Q(pk=query) | Q(name__icontains=query) | Q(abbr__icontains=query)
                )
            else:
                result = self.model.objects.filter(
                    Q(name__icontains=query) | Q(abbr__icontains=query)
                )
        else:
            result = self.model.objects.all()
        return result.order_by("name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context


@login_required
def department_archive(request, pk):
    department = Department.objects.get(pk=pk)
    if department and not department.archived:
        department.archived = True
        department.archived_by = request.user
        department.date_archived = timezone.now()
        department.save()
        messages.warning(request, f"Department {pk} archived!")
    return redirect("department-detail", pk=pk)


# ================== Patients =========================


class PatientCreate(LoginRequiredMixin, CreateView):
    model = Patient
    context_object_name = "patient"
    template_name = "patients/patient_form.html"
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
    template_name = "patients/patient_detail.html"
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
    template_name = "patients/patient_list.html"
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            if str(query).isnumeric():
                result = self.model.objects.filter(Q(pk=query) | Q(name__icontains=query))
            else:
                result = self.model.objects.filter(Q(name__icontains=query))
        else:
            result = self.model.objects.all()
        return result.order_by("name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context


@login_required
def patient_archive(request, pk):
    patient = Patient.objects.get(pk=pk)
    if patient and not patient.archived:
        patient.archived = True
        patient.archived_by = request.user
        patient.date_archived = timezone.now()
        patient.save()
        messages.warning(request, f"Patient {pk} archived!")
    return redirect("patient-detail", pk=pk)
