import requests

API_KEY = "pzvcImW8yNW4jr7S4gdO0***"


url = "https://api.nasa.gov/planetary/apod"

params = {
    "api_key": API_KEY,
}


response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
    print(response.text)