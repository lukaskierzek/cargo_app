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


class AircraftsInline(admin.TabularInline):
    model = Aircrafts
    extra = 0
    fields = [
        "name",
        "country",
        "destination",
        "cargo"
    ]


class CargosAircraftsInline(admin.TabularInline):
    model = Aircrafts.cargo.through
    extra = 0


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
    list_display = (
        "__str__",
        "country",
        "destination",
        "get_cargos",
        "get_pilots"
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

    inlines = (CargosAircraftsInline,)
    exclude = ('cargo',)


@admin.register(Destinations)
class DestinationsAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "from_airport",
        "to_airport",
        "get_aircrafts",
    )

    list_filter = (
        "from_airport",
        "to_airport"
    )

    search_fields = (
        "from_airport",
        "to_airport"
    )

    search_help_text = "Serach for information by from airport or to airport."

    inlines = (AircraftsInline,)


@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "name",
        "quantity",
        "get_aircrafts"
    )

    list_filter = (
        "name",
    )

    search_fields = (
        "name",
        "quantity"
    )

    search_help_text = "Serach for information by name or quantity."

    inlines = (CargosAircraftsInline,)
