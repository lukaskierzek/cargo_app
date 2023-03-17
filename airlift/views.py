from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Destinations, Cargos, Pilots, Aircrafts


# Create your views here.

def index_view(request):
    flights = Destinations.objects.all()[:5]
    aircrafts = Aircrafts.objects.all()[:5]
    cargos = Cargos.objects.all()[:5]
    pilots = Pilots.objects.all()[:5]

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
    context_object_name = 'destination'


class DestinationsListViews(ListView):
    model = Destinations
    template_name = 'airlift/destinations.html'
    context_object_name = 'destinations'


class AircraftsListViews(ListView):
    model = Aircrafts
    template_name = 'airlift/aircrafts.html'
    context_object_name = 'aircrafts'
