from rest_framework.views import APIView
from rest_framework.response import Response

from route.serializers import RouteSerializer
from route.service import OptimalFuelStationsService


class OptimalFuelStationsView(APIView):

    def get(self, request):
        start = request.query_params.get("start")
        end = request.query_params.get("end")
        service = OptimalFuelStationsService()
        optimal_route = service.get_optimal_fuel_stations(start, end)
        serializer_data = RouteSerializer(optimal_route).data
        return Response(serializer_data)
