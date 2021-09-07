from django import forms
from django.forms import DateInput

from .models import Manufacturer, Equipment, Medicine


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


# ================ Medicines ====================


class CreateMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        exclude = []
        widgets = {
            "mfg_date": DateInput(attrs={"type": "date"}),
            "expiry_date": DateInput(attrs={"type": "date"}),
        }


class UpdateMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        exclude = []
        widgets = {
            "mfg_date": DateInput(attrs={"type": "date"}),
            "expiry_date": DateInput(attrs={"type": "date"}),
        }
