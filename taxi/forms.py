from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from taxi.models import Driver, Car
from django import forms
from django.core.exceptions import ValidationError


class CarCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "license_number",
        )


class DriverLicenseUpdateForm(forms.ModelForm):
    LEN_LICENSE_NUMBER = 8

    class Meta:
        model = Driver
        fields = ("license_number",)
