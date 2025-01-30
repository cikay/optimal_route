from dataclasses import dataclass
from typing import List, Dict, Tuple

VEHICLE_RANGE = 500
FUEL_EFFICIENCY = 10


@dataclass
class Station:
    address: str
    distance: float
    price: float


@dataclass
class Stations:
    station_list: list[Station]
    distance: float


def find_optimal_stations(route: Stations) -> dict:
    num_stations = len(route.station_list)
    dp = initialize_dp(num_stations)

    for current_station_index in range(num_stations):
        curr_station = route.station_list[current_station_index]
        update_dp_entry(
            curr_station, route.station_list, dp, current_station_index, route.distance
        )

    # Optimized: Final cost is in the last entry of dp
    final_cost = dp[num_stations][0]  # Directly access from the table.

    final_station_index = num_stations - 1
    optimal_stations = reconstruct_path(route.station_list, dp, final_station_index)
    return {
        "cost": final_cost,
        "stations": optimal_stations,
        "distance": route.distance,
    }


def calculate_fuel_cost(distance: float, price: float) -> float:
    """Calculate the fuel cost for a given distance and price."""
    fuel_needed = distance / FUEL_EFFICIENCY
    return fuel_needed * price


def calculate_segment_cost(
    start_distance: float, end_distance: float, price: float
) -> float:
    """Calculate fuel cost for a segment of the route."""
    distance = end_distance - start_distance
    fuel_needed = distance / FUEL_EFFICIENCY
    return fuel_needed * price


def initialize_dp(num_stations: int) -> List[Tuple[float, int]]:
    """Initialize the dynamic programming table."""
    dp = [(float("inf"), -1) for _ in range(num_stations + 1)]
    dp[0] = (0, -1)  # Base case: starting point
    return dp


"""
start -> A(150) -> B(180) -> C(200) -> D(320) -> E(350) -> F(380) -> G(480) -> H(510) -> I(530) -> J(650) -> K(670) -> L(690) -> stop(800)

      150 < 500
      min cost calculated
start --------------A
                      800 - 150 > 500
                    A ------- stop (cant react) do not update min_cost

    180 < 500
    min cost calculated
B ------------------A
                      800 - 180 > 500 
                    B ------- stop (cant react)  do not update min_cost

   200 - 180 < 500
   min cost calculated
C ------------------B
    200 - 150 < 500
    min cost calculated
C ------------------A
                     800 - 200 > 500
                    C ------ stop (cant react)  do not update min_cost
"""


def update_dp_entry(
    curr_station: Station,
    stations: list[Station],
    dp: list[Tuple[float, int]],
    current_station_index: int,
    total_distance: float,  # Add total_distance as a parameter
) -> None:
    """Update dp entry, including cost to destination."""
    min_cost = float("inf")
    best_prev_index = -1

    # Check direct reach from the start
    if curr_station.distance <= VEHICLE_RANGE:
        min_cost = calculate_fuel_cost(curr_station.distance, curr_station.price)

    # Check reach from previous stations
    for prev_station_index in range(current_station_index):
        prev_station = stations[prev_station_index]
        distance = curr_station.distance - prev_station.distance
        if distance <= VEHICLE_RANGE:
            segment_cost = calculate_segment_cost(
                prev_station.distance,  # Correct start distance
                curr_station.distance,  # Correct end distance
                prev_station.price,  # Price at the refueling station
            )
            cost = dp[prev_station_index + 1][0] + segment_cost
            if cost < min_cost:
                min_cost = cost
                best_prev_index = prev_station_index

    # Calculate cost to destination from the current station
    remaining_distance = total_distance - curr_station.distance
    if remaining_distance <= VEHICLE_RANGE:
        cost_to_destination = calculate_fuel_cost(
            remaining_distance, curr_station.price
        )
        min_cost += cost_to_destination  # Add cost to destination

    dp[current_station_index + 1] = (min_cost, best_prev_index)


def reconstruct_path(
    stations: list[Station], dp: List[Tuple[float, int]], final_station_index: int
) -> List[Dict]:
    """Reconstruct the optimal path from the dp table."""
    optimal_stations = []
    current_index = final_station_index

    while current_index != -1:
        optimal_stations.append(stations[current_index])
        current_index = dp[current_index + 1][1]

    optimal_stations.reverse()
    return optimal_stations


# Example usage:
stations = [
    {"address": "A", "distance": 150, "price": 3.50},  # First cluster
    {"address": "B", "distance": 180, "price": 3.20},  # of stations
    {"address": "C", "distance": 200, "price": 3.80},  # around mile 150-200
    {"address": "D", "distance": 320, "price": 3.90},  # Second cluster
    {"address": "E", "distance": 350, "price": 3.30},  # of stations
    {"address": "F", "distance": 380, "price": 3.60},  # around mile 320-380
    {"address": "G", "distance": 480, "price": 3.40},  # Third cluster
    {"address": "H", "distance": 510, "price": 3.70},  # of stations
    {"address": "I", "distance": 530, "price": 3.20},  # around mile 480-530
    {"address": "J", "distance": 650, "price": 3.80},  # Final cluster
    {"address": "K", "distance": 670, "price": 3.50},  # of stations
    {"address": "L", "distance": 690, "price": 3.90},  # around mile 650-690
]
