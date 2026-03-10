import subprocess
import datetime as dt
import requests
import flight_data as fd



class AccessToken:

    def __init__(self, access_token, expires_in_seconds):
        self.access_token = access_token
        self.expire = dt.datetime.now() + dt.timedelta(seconds=expires_in_seconds)

    def is_expired(self):
        return dt.datetime.now() > self.expire


class FlightSearch:
    BASE_API_URL = "https://test.api.amadeus.com/"
    TOKEN_ENDPOINT = f"{BASE_API_URL}v1/security/oauth2/token"
    SEARCH_BY_CITY_ENDPOINT = f"{BASE_API_URL}v1/reference-data/locations/cities"
    SEARCH_FLIGHT_ENDPOINT = f"{BASE_API_URL}v2/shopping/flight-offers"
    API_KEY = client_secret_json = subprocess.check_output(
        ["gopass", "show", "-o", "gopass/websites/amadeus.com", "API_KEY"],
        text=True)
    API_SECRET = client_secret_json = subprocess.check_output(
        ["gopass", "show", "-o", "gopass/websites/amadeus.com", "API_SECRET"],
        text=True)
    DAYS_FOR_FLIGHT_SEARCH = 15
    NUMBER_OF_ADULTS = 2


    def __init__(self):
        self.__access_token = self.__get_bearer_token()
        print(f"Access token:{self.__access_token.access_token}")

    def make_call(self):
        print(self.__check_access_token())

    def search_iata_by_city(self, city:str):
        header = self.__get_auth_header()
        params = {
            "keyword": city.upper(),
        }
        response = requests.get(url=self.SEARCH_BY_CITY_ENDPOINT, headers=header, params=params)
        response.raise_for_status()
        response_json = response.json()
        return response_json["data"][0]["iataCode"]

    def search_flight(self, flightSearchData: fd.FlightSearchData):
        # curl '?originLocationCode=PAR&destinationLocationCode=ICN&departureDate=&returnDate=&adults=2&max=5' \
        #       -H 'Authorization: Bearer ABCDEFGH12345'
        header = self.__get_auth_header()
        date = dt.datetime.now() + dt.timedelta(days=self.DAYS_FOR_FLIGHT_SEARCH)

        params = {
            "originLocationCode": flightSearchData.iata_code_origin,
            "destinationLocationCode": flightSearchData.iata_code_destination,
            "departureDate": date.strftime("%Y-%m-%d"),
            "adults": self.NUMBER_OF_ADULTS
        }
        response = requests.get(url=self.SEARCH_FLIGHT_ENDPOINT, headers=header, params=params)
        response.raise_for_status()
        response_json = response.json()
        count = response_json["meta"]["count"]

        return count


    def __get_auth_header(self) -> dict[str, str]:
        headers = {
            "Authorization": f"Bearer {self.__access_token.access_token}",
        }
        return headers

    def __check_access_token(self):
        if self.__access_token is None or self.__access_token.is_expired():
            self.__access_token = self.__get_bearer_token()

    def __get_bearer_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.API_KEY,
            'client_secret': self.API_SECRET
        }
        # curl
        # "https://test.api.amadeus.com/v1/security/oauth2/token" \
        # - H
        # "Content-Type: application/x-www-form-urlencoded" \
        # - d
        # "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

        response = requests.post(url=self.TOKEN_ENDPOINT, headers=header, data=body)
        response.raise_for_status()
        response_json = response.json()
        return AccessToken(response_json["access_token"], response_json["expires_in"])



