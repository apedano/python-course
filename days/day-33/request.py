import requests

# def extract_position(json_data: dict[str, dict[str, str]]) -> tuple[str, str]:
#     position = (json_data["iss_position"]["latitude"], json_data["iss_position"]["longitude"])
#     return position
#
# response = requests.get("http://api.open-notify.org/iss-now.json")
#
# #Equivalent of raise an Exception in case of non 200 response status code
# response.raise_for_status()
#
# #{'message': 'success', 'iss_position': {'latitude': '0.6096', 'longitude': '-51.1002'}, 'timestamp': 1772537380}
# response_data = response.json()
#
# iss_position = extract_position(response_data)
#
# print(iss_position)


parameters = {
    "lat": 51.468137,
    "lng": 5.551218
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()
response_json = response.json()
sunrise = response_json["results"]["sunrise"]
sunset = response_json["results"]["sunset"]
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")