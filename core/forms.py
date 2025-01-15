from django import forms
from django.core.exceptions import ValidationError


class LocationFormBase(forms.ModelForm):
    coordinates = forms.CharField(
        required=False,
        help_text="Paste coordinates in format: latitude, longitude (e.g. 45.523, -122.676)",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["latitude"].required = False
        self.fields["longitude"].required = False

    def clean_coordinates(self):
        value = self.cleaned_data.get("coordinates")
        if not value:
            return None
        try:
            lat_str, lon_str = map(str.strip, value.split(","))
            return float(lat_str), float(lon_str)
        except (ValueError, TypeError):
            raise ValidationError('Enter coordinates in format: "latitude, longitude"')

    def clean(self):
        cleaned_data = super().clean()
        coordinates = cleaned_data.get("coordinates")
        latitude = cleaned_data.get("latitude")
        longitude = cleaned_data.get("longitude")
        if coordinates:
            lat, lon = coordinates
            cleaned_data["latitude"] = lat
            cleaned_data["longitude"] = lon
            if hasattr(self, "errors"):
                self.errors.pop("latitude", None)
                self.errors.pop("longitude", None)
            latitude = lat
            longitude = lon
        if latitude is None or longitude is None:
            raise ValidationError(
                "Either enter latitude and longitude directly, or provide coordinates."
            )
        return cleaned_data
