from rest_framework import viewsets

from airlift.models import Cargos, Destinations, Aircrafts, PilotsInformations
from .serializer import CargosSerializer, DestinationsSerializer, AircraftsSerializer, PilotsInformationsSerializer


class CargosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer


class DestinationsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Destinations.objects.all()
    serializer_class = DestinationsSerializer


class AircraftsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Aircrafts.objects.all()
    serializer_class = AircraftsSerializer


class PilotsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PilotsInformations.objects.all()
    serializer_class = PilotsInformationsSerializer
