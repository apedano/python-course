from tinydb import TinyDB, Query
import flight_data as fd


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.db = TinyDB("db.json")

    def init_database(self, initial_data:list[fd.FlightSearchData]):
        self.db.truncate()
        for item in initial_data:
            self.db.insert(self.__to_dict(item))

    def get_all_flight_search_data(self) -> list[fd.FlightSearchData]:
        Item = Query()
        # Get all users
        all_flight_search_data = self.db.search(Item._type == "FlightSearchData")
        all_data_list = []
        for data in all_flight_search_data:
            all_data_list.append(fd.FlightSearchData(**data))
        return all_data_list

    # Convert objects to dictionaries
    @staticmethod
    def __to_dict(obj):
        return {"_type": obj.__class__.__name__, **obj.__dict__}




