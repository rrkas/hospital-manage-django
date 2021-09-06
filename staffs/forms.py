from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


# new creation
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


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "mobile"]

    def __init__(self, *args, **kwargs):
        unrequired_fields = ["image"]
        super().__init__(*args, **kwargs)
        for field in unrequired_fields:
            self.fields[field].required = False




# -------------------------------------------------

# self update
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


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "mobile"]


# -------------------------------------------------

# update by admin
class StaffProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "mobile"]


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
