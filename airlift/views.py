from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Destinations, Cargos, Pilots, Aircrafts


# Create your views here.

@login_required
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


class DestinationsDetailView(LoginRequiredMixin, DetailView):
    model = Destinations
    template_name = 'airlift/destinations_detail.html'
    context_object_name = 'flights'


class DestinationsListViews(LoginRequiredMixin, ListView):
    model = Destinations
    template_name = 'airlift/destinations.html'
    context_object_name = 'flights'


class AircraftsDetailView(LoginRequiredMixin, DetailView):
    model = Aircrafts
    template_name = 'airlift/aircrafts_detail.html'
    context_object_name = 'aircraft'


class AircraftsListViews(LoginRequiredMixin, ListView):
    model = Aircrafts
    template_name = 'airlift/aircrafts.html'
    context_object_name = 'aircrafts'


class PilotsDetailView(LoginRequiredMixin, DetailView):
    model = Pilots
    template_name = 'airlift/pilots_detail.html'
    context_object_name = 'pilot'


class PilotsListViews(LoginRequiredMixin, ListView):
    model = Pilots
    template_name = 'airlift/pilots.html'
    context_object_name = 'pilots'


class CargosDetailViews(LoginRequiredMixin, DetailView):
    model = Cargos
    template_name = 'airlift/cargos_detail.html'
    context_object_name = 'cargo'


class CargosListViews(LoginRequiredMixin, ListView):
    model = Cargos
    template_name = 'airlift/cargos.html'
    context_object_name = 'cargos'
