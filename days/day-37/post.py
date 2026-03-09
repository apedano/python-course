# import requests
# with open('./true.png', 'rb') as f:
#     data = f.read()
# res = requests.post(url='http://httpbin.org/post',
#                     data=data,
#                     headers={'Content-Type': 'application/octet-stream'})
#
# print(res.json()['data']) #the posted body


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

