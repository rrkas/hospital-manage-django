from django import forms

from .models import Manufacturer, Equipment


# ================ Manufacturers ====================


class CreateManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        exclude = []

    non_required = ["address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.non_required:
            self.fields[field].required = False


class UpdateManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        exclude = []

    non_required = ["address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.non_required:
            self.fields[field].required = False


# ================ Equipments ====================


class CreateEquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = []


class UpdateEquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        exclude = []
