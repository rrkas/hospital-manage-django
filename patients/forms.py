from django import forms

from patients.models import Patient


class CreatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            "image", "name", "dob",
            "mobile", "email", "gender",
            "aadhaar", "address",
        )
        widgets = {
            'dob': forms.DateInput(
                attrs={'type': 'date'},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['email'].required = False
        self.fields['aadhaar'].required = False


class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            "image", "name", "dob",
            "mobile", "email", "gender",
            "aadhaar", "address",
        )
        widgets = {
            'dob': forms.DateInput(
                attrs={'type': 'date'},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['email'].required = False
        self.fields['aadhaar'].required = False

    def save(self, commit=True):
        if not self.aadhaar:
            self.aadhaar = None
        return super().save(commit)
