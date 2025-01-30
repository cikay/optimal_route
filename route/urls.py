from django.urls import path

from route.views import OptimalFuelStationsView


url_patterns = [
    path("stations/", OptimalFuelStationsView.as_view(), name="fuel_stations"),
]
