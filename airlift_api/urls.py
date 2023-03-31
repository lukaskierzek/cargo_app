from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'cargos', views.CargosViewSet, basename='cargos')
router.register(r'destinations', views.DestinationsViewSet, basename='destinations')
router.register(r'aircrafts', views.AircraftsViewSet, basename='aircrafts')
router.register(r'pilots', views.PilotsViewSet, basename='pilots')

urlpatterns = [
    path('', include(router.urls)),
]
