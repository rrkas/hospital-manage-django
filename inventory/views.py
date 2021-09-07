from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, ListView

import hospital_manage.settings as global_settings
from .forms import (
    CreateManufacturerForm,
    UpdateManufacturerForm,
    CreateEquipmentForm,
    UpdateEquipmentForm,
)
from .models import Manufacturer, Equipment, InventoryItem


@login_required
def home(request):
    context = {
        "items": [
            InventoryItem("Manufacturers", "manufacturer-home", Manufacturer.objects.all().count()),
            InventoryItem("Equipments", "equipment-home", Equipment.objects.all().count()),
        ],
    }
    return render(request, f"inventory/home.html", context=context)


# ================== Manufacturers ===========================


class ManufacturerCreate(LoginRequiredMixin, CreateView):
    model = Manufacturer
    context_object_name = "manufacturer"
    template_name = "manufacturers/manufacturer_form.html"
    form_class = CreateManufacturerForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["update_mode"] = False
        return data


class ManufacturerDetail(LoginRequiredMixin, DetailView):
    model = Manufacturer
    template_name = "manufacturers/manufacturer_detail.html"
    context_object_name = "manufacturer"


class ManufacturerUpdate(LoginRequiredMixin, UpdateView):
    template_name = "manufacturers/manufacturer_form.html"
    model = Manufacturer
    context_object_name = "manufacturer"
    form_class = UpdateManufacturerForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["update_mode"] = True
        return data


class ManufacturerList(LoginRequiredMixin, ListView):
    model = Manufacturer
    context_object_name = "manufacturers"
    template_name = "manufacturers/manufacturer_list.html"
    ordering = ["name"]
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            if str(query).isnumeric():
                result = Manufacturer.objects.filter(
                    Q(pk=query) | Q(name__icontains=query)
                )
            else:
                result = Manufacturer.objects.filter(Q(name__icontains=query))
        else:
            result = Manufacturer.objects.all()
        return result.order_by("name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context


# ================== Equipments ===========================


class EquipmentCreate(LoginRequiredMixin, CreateView):
    model = Equipment
    context_object_name = "equipment"
    template_name = "equipments/equipment_form.html"
    form_class = CreateEquipmentForm

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


class EquipmentDetail(LoginRequiredMixin, DetailView):
    model = Equipment
    template_name = "equipments/equipment_detail.html"
    context_object_name = "equipment"


class EquipmentUpdate(LoginRequiredMixin, UpdateView):
    template_name = "equipments/equipment_form.html"
    model = Equipment
    context_object_name = "equipment"
    form_class = UpdateEquipmentForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["update_mode"] = True
        return data


class EquipmentList(LoginRequiredMixin, ListView):
    model = Equipment
    context_object_name = "equipments"
    template_name = "equipments/equipment_list.html"
    ordering = ["name"]
    paginate_by = global_settings.PAGINATION_COUNT

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            if str(query).isnumeric():
                result = Equipment.objects.filter(
                    Q(pk=query) | Q(name__icontains=query)
                )
            else:
                result = Equipment.objects.filter(Q(name__icontains=query))
        else:
            result = Equipment.objects.all()
        return result.order_by("name")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search")
        return context
