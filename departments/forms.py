from django import forms

from .models import Department


class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("name", "abbr", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["abbr"].required = False
        self.fields["description"].required = False


class UpdateDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ("name", "abbr", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["abbr"].required = False
        self.fields["description"].required = False
