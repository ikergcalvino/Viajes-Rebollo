from django import forms
from .models import Activity, Package, TripPlan
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_google_maps_url(value):
    if not value.startswith("https://www.google.com/maps/"):
        raise ValidationError("La URL debe ser de Google Maps.")
    URLValidator()(value)


class NewActivity(forms.ModelForm):
    loc = forms.URLField(validators=[validate_google_maps_url])

    class Meta:
        model = Activity
        fields = ['name', 'description', 'price',
                  'init_date', 'end_date', 'loc']
        widgets = {
            'init_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ModActivity(forms.ModelForm):
    loc = forms.URLField(validators=[validate_google_maps_url])

    class Meta:
        model = Activity
        fields = ['name', 'description', 'price',
                  'init_date', 'end_date', 'loc']
        widgets = {
            'init_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class NewPackage(forms.ModelForm):
    activities = forms.ModelMultipleChoiceField(
        queryset=Activity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Package
        fields = ['name', 'description', 'activities']

    def clean(self):
        cleaned_data = super().clean()
        activities = cleaned_data.get("activities")

        if not activities:
            raise ValidationError("Debe seleccionar al menos una actividad.")

        return cleaned_data


class ModPackage(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'activities']

    def __init__(self, *args, **kwargs):
        super(ModPackage, self).__init__(*args, **kwargs)
        self.fields['activities'].widget = forms.CheckboxSelectMultiple()
        self.fields['activities'].queryset = Activity.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        activities = cleaned_data.get("activities")

        if not activities:
            raise ValidationError("Debe seleccionar al menos una actividad.")

        return cleaned_data


class NewTripPlan(forms.ModelForm):
    class Meta:
        model = TripPlan
        fields = ['name', 'description', 'package', 'customized_activities']
        widgets = {
            'customized_activities': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(NewTripPlan, self).__init__(*args, **kwargs)
        self.fields['customized_activities'].queryset = Activity.objects.all()


class ModTripPlan(forms.ModelForm):
    class Meta:
        model = TripPlan
        fields = ['name', 'description', 'package', 'customized_activities']
        widgets = {
            'customized_activities': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(ModTripPlan, self).__init__(*args, **kwargs)
        self.fields['package'].queryset = Package.objects.all()
        self.fields['customized_activities'].queryset = Activity.objects.all()
