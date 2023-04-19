from django import forms

from .models import Destinations, Aircrafts, Cargos, PilotsInformations


class DestinationUpdateForm(forms.ModelForm):
    class Meta:
        model = Destinations
        fields = (
            'from_airport',
            'to_airport',
            'scheduled_take_off',
            'scheduled_landing',
            'comment'
        )
        widgets = {
            'from_airport': forms.TextInput(attrs={'size': 60}),
            'to_airport': forms.TextInput(attrs={'size': 60}),
            'scheduled_take_off': forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '1'}),
            'scheduled_landing': forms.DateTimeInput(attrs={'type': 'datetime-local', 'step': '1'}),
            'comment': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }


class AircraftUpdateForm(forms.ModelForm):
    class Meta:
        model = Aircrafts
        fields = (
            'name',
            'country',
            'destination',
            'cargo',
            'comment'
        )
        widgets = {
            'name': forms.TextInput(attrs={'size': 60}),
            'country': forms.TextInput(attrs={'size': 60}),
            'cargo': forms.SelectMultiple(attrs={'size': 10, }),
            'comment': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class CargoUpdateForm(forms.ModelForm):
    class Meta:
        model = Cargos
        fields = (
            'name',
            'quantity',
            'comment',
        )
        widgets = {
            'name': forms.TextInput(attrs={'size': 60}),
            'comment': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }


class PilotsInformationsUpdateForm(forms.ModelForm):
    class Meta:
        model = PilotsInformations
        fields = (
            'pilot',
            'position',
            'rank',
            'age',
            'country',
            'comment',
        )
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
