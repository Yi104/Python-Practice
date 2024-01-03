# day 33 API application programming interface intro


import requests
from datetime import datetime

# response = requests.get(url= "http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data =response.json()
# print(data)
#
# longitude = data["iss_position"]["longtitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position =(longitude,latitude)

LAT =37.7749
LNG= 122.4194

parameters= {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json")
response.raise_for_status()
data= response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunrise.split("T")[1].split(":")[0])

time_now= datetime.now()
print(time_now)