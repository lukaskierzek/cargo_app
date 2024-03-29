from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView

from .forms import DestinationUpdateForm, AircraftUpdateForm, CargoUpdateForm, PilotsInformationsUpdateForm
from .models import Destinations, Cargos, Pilots, Aircrafts, PilotsInformations


# Create your views here.

@login_required
def index_view(request):
    rows_limit: int = 4

    flights = Destinations.objects.all()[:rows_limit]
    aircrafts = Aircrafts.objects.all()[:rows_limit]
    cargos = Cargos.objects.all()[:rows_limit]
    pilots = Pilots.objects.all()[:rows_limit]

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
    template_name = 'airlift/destinations/destinations_detail.html'
    context_object_name = 'flight'


class DestinationsListViews(LoginRequiredMixin, ListView):
    model = Destinations
    template_name = 'airlift/destinations/destinations.html'
    context_object_name = 'flights'


class DestinationsUpdate(LoginRequiredMixin, UpdateView):
    model = Destinations
    template_name = 'airlift/destinations/destinations_form.html'
    context_object_name = 'flight'
    form_class = DestinationUpdateForm


class AircraftsDetailView(LoginRequiredMixin, DetailView):
    model = Aircrafts
    template_name = 'airlift/aircrafts/aircrafts_detail.html'
    context_object_name = 'aircraft'


class AircraftsListViews(LoginRequiredMixin, ListView):
    model = Aircrafts
    template_name = 'airlift/aircrafts/aircrafts.html'
    context_object_name = 'aircrafts'


class AircraftsUpdate(LoginRequiredMixin, UpdateView):
    model = Aircrafts
    template_name = 'airlift/aircrafts/aircrafts_form.html'
    context_object_name = 'aircraft'
    form_class = AircraftUpdateForm


class PilotsDetailView(LoginRequiredMixin, DetailView):
    model = Pilots
    template_name = 'airlift/pilots/pilots_detail.html'
    context_object_name = 'pilot'


class PilotsListViews(LoginRequiredMixin, ListView):
    model = Pilots
    template_name = 'airlift/pilots/pilots.html'
    context_object_name = 'pilots'


class PilotsUpdate(LoginRequiredMixin, UpdateView):
    model = Pilots
    fields = '__all__'
    template_name = 'airlift/pilots/pilots_form.html'
    context_object_name = 'pilot'


class PilotsInformationsUpdate(LoginRequiredMixin, UpdateView):
    model = PilotsInformations
    template_name = 'airlift/pilots/pilots_informations_form.html'
    context_object_name = 'pilots_informations'
    form_class = PilotsInformationsUpdateForm


class CargosDetailViews(LoginRequiredMixin, DetailView):
    model = Cargos
    template_name = 'airlift/cargos/cargos_detail.html'
    context_object_name = 'cargo'


class CargosListViews(LoginRequiredMixin, ListView):
    model = Cargos
    template_name = 'airlift/cargos/cargos.html'
    context_object_name = 'cargos'


class CargosUpdate(LoginRequiredMixin, UpdateView):
    model = Cargos
    template_name = 'airlift/cargos/cargos_form.html'
    context_object_name = 'cargo'
    form_class = CargoUpdateForm
