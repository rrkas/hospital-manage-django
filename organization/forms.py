from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Doctor, Department, Patient, Profile


# ================== Users =========================
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    def save(self, commit=True):
        user = super().save(commit)
        return user

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    disabled_fields = ("username", "email")
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class StaffUserUpdateForm(forms.ModelForm):
    disabled_fields = ("username", "email")
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.disabled_fields:
            self.fields[field].disabled = True

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "is_active"]


# ================== Staffs =========================


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "mobile"]

    def __init__(self, *args, **kwargs):
        un_required_fields = ["image"]
        super().__init__(*args, **kwargs)
        for field in un_required_fields:
            self.fields[field].required = False


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "mobile"]


class StaffProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "mobile"]


# ================== Doctors =========================


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


# ================== Departments =========================


class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("name", "abbr", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False


class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("name", "abbr", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].required = False


# ================== Patients =========================


class CreatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
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


class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
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
