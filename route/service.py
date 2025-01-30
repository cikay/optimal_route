from route.find_optimal_route import find_optimal_stations
from route.client import FuelStationsClient


class OptimalFuelStationsService:
    def __init__(self):
        self.client = FuelStationsClient("")

    def get_optimal_fuel_stations(self, start, end):
        fuel_stations = self.client.get_fuel_stations(start, end)
        return find_optimal_stations(fuel_stations)
