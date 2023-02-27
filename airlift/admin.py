from django.contrib import admin
from .models import Aircrafts, Destinations, Cargos, Pilots, PilotsInformations


class PilotsInformationsInline(admin.StackedInline):
    model = PilotsInformations
    extra = 0
    fields = [
        "position",
        "rank",
        "age",
        "country"
    ]


@admin.register(Pilots)
class PilotsAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "first_name",
        "last_name",
        "aircraft"
    )

    list_filter = (
        "aircraft",
    )

    search_fields = (
        "first_name",
        "last_name",
        "aircraft__name",
        "aircraft__country",
    )

    search_help_text = "Serach for information by first name, last name, aircraft name or aircraft country."

    inlines = (PilotsInformationsInline,)


@admin.register(PilotsInformations)
class PilotsInformationsAdmin(admin.ModelAdmin):
    list_display = (
        "pilot",
        "position",
        "rank",
        "age",
        "country"
    )

    list_filter = (
        "position",
        "rank",
        "country"
    )

    search_fields = (
        "pilot__first_name",
        "pilot__last_name",
        "pilot__aircraft__name",
        "pilot__age",
        "position",
        "rank",
        "age",
        "country"
    )

    search_help_text = "Serach for information by pilot or aircraft name."


@admin.register(Aircrafts)
class AircraftsAdmin(admin.ModelAdmin):
    @staticmethod
    def gets_cargo(obj):
        return [cargo.__str__() for cargo in obj.cargo.all()]

    list_display = (
        "__str__",
        "country",
        "destination",
        "gets_cargo"
    )

    list_filter = (
        "country",
        "destination",
        "destination__from_airport",
        "destination__to_airport",
        "cargo__name"
    )

    search_fields = (
        "country",
        "destination__from_airport",
        "destination__to_airport",
        "cargo__name",
        "cargo__quantity"
    )

    search_help_text = "Serach for information by country, destination or cargo."


@admin.register(Destinations)
class DestinationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    pass
