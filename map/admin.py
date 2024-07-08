from django.contrib import admin
from django import forms
from .models import Locations, Regions
from .widgets import LeafletWidget

class LocationAdminForm(forms.ModelForm):
    latitude = forms.FloatField(widget=LeafletWidget())
    longitude = forms.FloatField(widget=LeafletWidget())

    class Meta:
        model = Locations
        fields = ['name', 'latitude', 'longitude', 'regions']

class LocationAdmin(admin.ModelAdmin):
    form = LocationAdminForm
    list_display = ['name', 'latitude', 'longitude', 'regions']

admin.site.register(Locations, LocationAdmin)
admin.site.register(Regions)
