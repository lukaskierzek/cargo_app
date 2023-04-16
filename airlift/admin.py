from django.contrib import admin

from .models import Aircrafts, Destinations, Cargos, Pilots, PilotsInformations


class PilotsInformationsInline(admin.StackedInline):
    model = PilotsInformations
    extra = 0
    fields = [
        "position",
        "rank",
        "age",
        "country",
        "comment"
    ]


class AircraftsInline(admin.TabularInline):
    model = Aircrafts
    extra = 0
    fields = [
        "name",
        "country",
        "destination",
        "cargo",
        "comment"
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
        "comment"
    )

    search_help_text = "Serach for information by first name, last name, aircraft name, aircraft country or comment."

    inlines = (PilotsInformationsInline,)


@admin.register(PilotsInformations)
class PilotsInformationsAdmin(admin.ModelAdmin):
    list_display = (
        "pilot",
        "position",
        "rank",
        "age",
        "country",
        "comment"
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
        "country",
        "comment"
    )

    search_help_text = "Serach for information by pilot, aircraft name or comment."


@admin.register(Aircrafts)
class AircraftsAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "country",
        "destination",
        "get_cargos",
        "get_pilots",
        "comment"
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
        "cargo__quantity",
        "comment"
    )

    search_help_text = "Serach for information by country, destination, cargo or comment."

    inlines = (CargosAircraftsInline,)
    exclude = ('cargo',)


@admin.register(Destinations)
class DestinationsAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "from_airport",
        "to_airport",
        "get_aircrafts",
        "comment"
    )

    list_filter = (
        "from_airport",
        "to_airport"
    )

    search_fields = (
        "from_airport",
        "to_airport",
        "comment"
    )

    search_help_text = "Serach for information by from airport, to airport or comment."

    inlines = (AircraftsInline,)


@admin.register(Cargos)
class CargosAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "name",
        "quantity",
        "get_aircrafts",
        "comment"
    )

    list_filter = (
        "name",
    )

    search_fields = (
        "name",
        "quantity",
        "comment"
    )

    search_help_text = "Serach for information by name, quantity or comment."

    inlines = (CargosAircraftsInline,)
