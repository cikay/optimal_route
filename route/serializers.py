from rest_framework import serializers


class StationSerializer(serializers.Serializer):
    address = serializers.CharField()
    price = serializers.DecimalField(decimal_places=2, max_digits=10)
    distance = serializers.FloatField()


class RouteSerializer(serializers.Serializer):
    stations = StationSerializer(many=True)
    distance = serializers.FloatField()
    cost = serializers.DecimalField(decimal_places=2, max_digits=10)
