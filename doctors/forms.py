from django import forms

from .models import Doctor


class CreateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            "image",
            "name",
            "dob",
            "mobile",
            "email",
            "gender",
            "department",
            "aadhaar",
            "address",
        )
        widgets = {
            "dob": forms.DateInput(
                attrs={"type": "date"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].required = False
        self.fields["email"].required = False
        self.fields["aadhaar"].required = False


class UpdateDoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            "image",
            "name",
            "dob",
            "mobile",
            "email",
            "gender",
            "aadhaar",
            "address",
        )
        widgets = {
            "dob": forms.DateInput(
                attrs={"type": "date"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["image"].required = False
        self.fields["email"].required = False
        self.fields["aadhaar"].required = False
