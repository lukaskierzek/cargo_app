from rest_framework import serializers
from airlift.models import Cargos, Destinations, Aircrafts, Pilots, PilotsInformations


class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = '__all__'


class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = '__all__'


class PilotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilots
        fields = '__all__'


class PilotsInformationsSerializer(serializers.ModelSerializer):
    pilot = PilotsSerializer()

    class Meta:
        model = PilotsInformations
        fields = '__all__'


class AircraftsSerializer(serializers.ModelSerializer):
    cargo = CargosSerializer(read_only=True, many=True)
    destination = DestinationsSerializer(read_only=True)
    pilots = PilotsSerializer(source='pilots_set', many=True)

    class Meta:
        model = Aircrafts
        fields = [
            'id',
            'name',
            'destination',
            'cargo',
            'pilots'
        ]
