# 🐍 API implementation


https://httpbin.org/

## GET calls

```python
import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

#Equivalent of raise an Exception in case of non 200 response status code
response.raise_for_status()

#dictionary from the JSON response
response_data = response.json() 

print(response_data) 
```

### Using parameters

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

## POST calls

### Posting json data

```python
import requests
import json

person_dict = {"person": {
        "name": "Alessandro",
        "surname": "Pedano",
        "birth" : {
            "city": "Palermo",
            "date": "1980-07-27"
        }
    }
}

url = "https://httpbin.org/post"
response = requests.post(url, json=person_dict)


print(response.json()["data"])
print(json.loads(response.json()["data"])["person"]["name"])
```

### Posting binary data

```python
import requests
with open('./true.png', 'rb') as f:
    data = f.read()
res = requests.post(url='http://httpbin.org/post',
                    data=data,
                    headers={'Content-Type': 'application/octet-stream'})

print(res.json()['data']) #the posted body
```

