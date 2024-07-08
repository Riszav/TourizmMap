from rest_framework import serializers
from .models import Locations, Regions


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = [
            'id',
            'name',
            'latitude',
            'longitude'
        ]

class RegionSerializer(serializers.ModelSerializer):
    locations = serializers.SerializerMethodField(LocationsSerializer)
    class Meta:
        model = Regions
        fields = [
            'id',
            'region_name',
            'locations'
        ]
