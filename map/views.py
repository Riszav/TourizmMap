from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .models import Locations, Regions
from .serializers import LocationsSerializer, RegionSerializer


class LocationViewSet(ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer


def map_view(request):
    return render(request, 'maps/maps.html')

def region_view(request):
    return render(request, 'maps/regions.html')

def regions_api(request):
    regions = Regions.objects.all()
    data = [
        {
            'id': region.id,
            'region_name': region.region_name,
            'boundary': region.boundary,
        }
        for region in regions
    ]
    return JsonResponse(data, safe=False)

def locations_api(request, region_id):
    locations = Locations.objects.filter(regions__id=region_id)
    data = [
        {
            'name': location.name,
            'latitude': location.latitude,
            'longitude': location.longitude,
        }
        for location in locations
    ]
    return JsonResponse(data, safe=False)
