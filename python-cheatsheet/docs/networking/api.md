# 🐍 API implementation

## Mame API calls

```python
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

#Equivalent of raise an Exception in case of non 200 response status code
response.raise_for_status()

#dictionary from the JSON response
response_data = response.json() 

print(response_data) 
```

## Using parameters

Example of API requiring parameters: https://sunrise-sunset.org/api

```python
import requests

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
```

