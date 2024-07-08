from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, map_view, region_view, regions_api, locations_api

router = DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('regions/', region_view, name='regions_map'),
    path('api/regions/<int:region_id>/locations/', locations_api, name='locations_api'),
    path('api/regions/', regions_api),
    path('', map_view, name='map'),
    path('regions/', region_view, name='regions_map')
]