from django.contrib import admin
from .models import Aircrafts, Destinations, Cargos, Pilots, PilotsInformations


@admin.register(Pilots)
class PilotsAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
    )


@admin.register(PilotsInformations)
class PilotsInformationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Aircrafts)
class AircraftsAdmin(admin.ModelAdmin):
    pass


@admin.register(Destinations)
class DestinationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    pass
