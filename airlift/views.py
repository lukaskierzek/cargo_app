from django.db.models import QuerySet
from django.shortcuts import render
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
