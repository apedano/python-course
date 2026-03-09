from dataclasses import dataclass


class FlightData:
    #This class is responsible for structuring the flight data.
    pass

@dataclass
class FlightSearchData:
    origin: str
    iata_code_origin: str
    destination: str
    iata_code_destination: str
    lowe_price: float

    def __init__(self, origin:str, iata_code_origin:str, destination:str, iata_code_destination:str, lowe_price:float, **kwargs):
        self.origin = origin
        self.iata_code_origin = iata_code_origin
        self.destination = destination
        self.iata_code_destination = iata_code_destination
        self.lowe_price = lowe_price









