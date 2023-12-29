from django import forms
from .models import Activity, Package, TripPlan
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_google_maps_url(value):
    if not value.startswith("https://www.google.com/maps/place/"):
        raise ValidationError("La URL debe ser de Google Maps, comenzando por 'https://www.google.com/maps/place/' .")
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
            'description': forms.Textarea(attrs={'style': 'resize: none;'}),

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

    new_activity_button = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Nombre de la nueva actividad'})
    )

    class Meta:
        model = Package
        fields = ['name', 'description', 'activities']
        widgets = {
            'description': forms.Textarea(attrs={'style': 'resize: none;'}),
        }

    def __init__(self, *args, **kwargs):
        super(NewPackage, self).__init__(*args, **kwargs)
        self.fields['new_activity_button'].label = 'Crear Nueva Actividad'

    def clean(self):
        cleaned_data = super().clean()
        activities = cleaned_data.get("activities")
        new_activity_button = cleaned_data.get("new_activity_button")

        if not activities and not new_activity_button:
            raise ValidationError(
                "Debe seleccionar al menos una actividad o crear una nueva.")

        return cleaned_data


class ModPackage(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'description', 'activities']
        widgets = {
            'description': forms.Textarea(attrs={'style': 'resize: none;'}),
        }

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
            'customized_activities': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'style': 'resize: none;'}),
        }

    def __init__(self, *args, **kwargs):
        super(NewTripPlan, self).__init__(*args, **kwargs)
        self.fields['customized_activities'].queryset = Activity.objects.all()


class ModTripPlan(forms.ModelForm):
    class Meta:
        model = TripPlan
        fields = ['name', 'description', 'package', 'customized_activities']
        widgets = {
            'customized_activities': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'style': 'resize: none;'}),

        }

    def __init__(self, *args, **kwargs):
        super(ModTripPlan, self).__init__(*args, **kwargs)
        self.fields['package'].queryset = Package.objects.all()
        self.fields['customized_activities'].queryset = Activity.objects.all()
