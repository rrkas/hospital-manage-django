from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import *

import hospital_manage.settings as global_settings
from staffs.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from staffs.models import Profile

staffs = "staffs"


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account created successfully! You are now able to login!"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, f"{staffs}/register.html", {"form": form})


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


class ProfileList(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = "staffs"
    ordering = ["first_name", "last_name"]
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            result = Profile.objects.filter(
                Q(user__first_name__icontains=query)
                | Q(user__last_name__icontains=query)
            )
        else:
            result = Profile.objects.all()
        return result.order_by("user__first_name", "user__last_name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context


class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = "staff"
