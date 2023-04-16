from rest_framework import serializers

from airlift.models import Cargos, Destinations, Aircrafts, Pilots, PilotsInformations


class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = [
            'name',
            'quantity',
            'comment'
        ]


class DestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinations
        fields = [
            'from_airport',
            'to_airport',
            'comment'
        ]


class AircraftsForPilotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircrafts
        fields = [
            'name'
        ]


class PilotsSerializer(serializers.ModelSerializer):
    aircraft = AircraftsForPilotsSerializer()

    class Meta:
        model = Pilots
        fields = [
            'first_name',
            'last_name',
            'aircraft'
        ]


class PilotsInformationsSerializer(serializers.ModelSerializer):
    pilot = PilotsSerializer()

    class Meta:
        model = PilotsInformations
        fields = '__all__'


class PilotsSerializerForAircrafts(serializers.ModelSerializer):
    class Meta:
        model = Pilots
        fields = [
            'first_name',
            'last_name'
        ]


class AircraftsSerializer(serializers.ModelSerializer):
    cargo = CargosSerializer(read_only=True, many=True)
    destination = DestinationsSerializer(read_only=True)
    pilots = PilotsSerializerForAircrafts(source='pilots_set', many=True)

    class Meta:
        model = Aircrafts
        fields = [
            'name',
            'destination',
            'cargo',
            'pilots',
            'comment'
        ]
