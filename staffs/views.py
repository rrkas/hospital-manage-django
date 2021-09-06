from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import *

import hospital_manage.settings as global_settings
from staffs.forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    ProfileCreateForm,
    StaffUserUpdateForm,
    StaffProfileUpdateForm,
)
from staffs.models import Profile

staffs = "staffs"


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
    return render(request, f"{staffs}/register.html", context)


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
    return render(request, f"{staffs}/profile.html", context)


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
                result = Profile.objects.filter(
                    Q(pk=query)
                    | Q(user__first_name__icontains=query)
                    | Q(user__last_name__icontains=query)
                    | Q(user__username__icontains=query)
                )
            else:
                result = Profile.objects.filter(
                    Q(user__first_name__icontains=query)
                    | Q(user__last_name__icontains=query)
                    | Q(user__username__icontains=query)
                )
        else:
            result = Profile.objects.all()
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
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        u_form = StaffUserUpdateForm(request.POST, instance=profile.user)
        p_form = StaffProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Account updated successfully!")
            return redirect("staff-detail", pk=pk)
    else:
        u_form = StaffUserUpdateForm(instance=profile.user)
        p_form = StaffProfileUpdateForm(instance=profile)
    context = {
        "u_form": u_form,
        "p_form": p_form,
        "pk": pk,
    }
    return render(request, f"{staffs}/staff_form.html", context)
