import requests

from route.find_optimal_route import Stations, Station


class FuelStationsClient:
    def __init__(self, url):
        self.host = "https://router.hereapi.com"

    def get_fuel_stations(self, start, end):
        # url = (
        #     self.host
        #     + "/v8/routes?origin={start}&transportMode=truck&apiKey={api_key}".format(
        #         start=start,
        #         api_key=self._get_api_key(),
        #     )
        # )

        # response = requests.get(url)
        # data = response.json()
        data = {
            "stations": [
                {"address": "A", "distance": 150, "price": 3.50},
                {"address": "B", "distance": 180, "price": 3.20},
                {"address": "C", "distance": 200, "price": 3.80},
                {"address": "D", "distance": 320, "price": 3.90},
                {"address": "E", "distance": 350, "price": 3.30},
                {"address": "F", "distance": 380, "price": 3.60},
                {"address": "G", "distance": 480, "price": 3.40},
                {"address": "H", "distance": 510, "price": 3.70},
                {"address": "I", "distance": 530, "price": 3.20},
                {"address": "J", "distance": 650, "price": 3.80},
                {"address": "K", "distance": 670, "price": 3.50},
                {"address": "L", "distance": 690, "price": 3.90},
            ],
            "distance": 800,
        }
        return self.normalize(data)

    def normalize(self, data):
        stations = []
        for station in data["stations"]:
            stations.append(
                Station(
                    address=station["address"],
                    distance=station["distance"],
                    price=station["price"],
                )
            )

        return Stations(station_list=stations, distance=data["distance"])

    def _get_api_key(self):
        return "4jeGHyijieYTqzcseLXwEAE46w-pC--etN8AypA-N54"
