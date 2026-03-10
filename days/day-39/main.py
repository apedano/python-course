#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
import flight_data as fd
from data_manager import *



dm = DataManager()


def initialise_data():
    origin_cities = ["eindhoven", "weeze", "brussels"]
    init_data_list = [("palermo", 50), ("paris", 100), ("london", 150), ("new york", 400)]
    iata_dict = {"weeze":"NRN"} #I cannot find the city to be used as input in the iata code method
    data_list = []
    for origin_city in origin_cities:
        if origin_city not in iata_dict:
            iata_dict[origin_city] = flight_search.search_iata_by_city(origin_city)
        for init_data in init_data_list:
            if init_data[0] not in iata_dict:
                iata_dict[init_data[0]] = flight_search.search_iata_by_city(init_data[0])
        data_list = data_list + (list(
            map(
                lambda data: fd.FlightSearchData(origin_city, iata_dict[origin_city], data[0], iata_dict[data[0]], data[1]), init_data_list
            )
        ))
    dm.init_database(data_list)






flight_search = FlightSearch()
#initialise_data()
flight_search_data = dm.get_all_flight_search_data()
# for data in flight_search_data:
#
#     print(data)
# for flight_data in flight_search_data:
#     print(f"Searching flights from {flight_data.origin} to {flight_data.destination}...")
#     print(f"Found {flight_search.search_flight(flight_data)} flights.")

import json
with open("response.json", "r") as data_json_file:
    data_json = json.load(data_json_file)

data = data_json["data"]

sorted_data = sorted(data, key=lambda single_data: float(single_data["price"]["grandTotal"]))
first_three_data = sorted_data[:3]

for sorted_flight in first_three_data:
    print(sorted_flight["price"]["grandTotal"])

