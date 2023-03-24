from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Destinations, Cargos, Pilots, Aircrafts


# Create your views here.

def index_view(request):
    flights = Destinations.objects.all()[:4]
    aircrafts = Aircrafts.objects.all()[:4]
    cargos = Cargos.objects.all()[:4]
    pilots = Pilots.objects.all()[:4]

    context = {
        'flights': flights,
        'aircrafts': aircrafts,
        'cargos': cargos,
        'pilots': pilots,
    }

    return render(
        request=request,
        template_name='airlift/index.html',
        context=context
    )


class DestinationsDetailView(DetailView):
    model = Destinations
    template_name = 'airlift/destinations_detail.html'
    context_object_name = 'flights'


class DestinationsListViews(ListView):
    model = Destinations
    template_name = 'airlift/destinations.html'
    context_object_name = 'flights'


class AircraftsListViews(ListView):
    model = Aircrafts
    template_name = 'airlift/aircrafts.html'
    context_object_name = 'aircrafts'


class PilotsListViews(ListView):
    model = Pilots
    template_name = 'airlift/pilots.html'
    context_object_name = 'pilots'


class CargosListViews(ListView):
    model = Cargos
    template_name = 'airlift/cargos.html'
    context_object_name = 'cargos'
