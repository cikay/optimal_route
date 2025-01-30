from route.find_optimal_route import find_optimal_stops
from route.client import FuelStationsClient


class OptimalFuelStopsService:
    def __init__(self):
        self.client = FuelStationsClient("")

    def get_optimal_fuel_stops(self, start, end):
        fuel_stations =  self.client.get_fuel_stations(start, end)
        return find_optimal_stops(fuel_stations)
