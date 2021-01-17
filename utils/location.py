import requests
import numpy as np
from .firebase import pathsdict

default = "I am still learning all possible routes, Sorry I dont know in detail about how to travel from {} to IIT MANDI as of now, The best I can suggest is:\n"

def guess(lat, lng):

    user = np.array((lat, lng))
    chandi = np.array((30.741482, 76.768066))
    delhi = np.array((28.644800, 77.216721))
    mumbai = np.array((19.076090, 72.877426))

    chd = np.linalg.norm(chandi - user)
    ded = np.linalg.norm(delhi - user)
    mumd = np.linalg.norm(mumbai - user)

    if (mumd < ded and mumd < chd):
        return "Maharashtra"
    elif (chd < mumd and chd < ded):
        return "Chandigarh"
    else:
        return "Delhi"


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")


def suggest_path(lat, lng):

    location = geolocator.reverse(str(lat) + "," + str(lng))
    print(location)
    address = location.raw['address']
    state = address.get('state', '')
    print('State:', state)

    if state in pathsdict:
        print("i am in if condition")
        print(pathsdict[state])
        return pathsdict[state]
    else:
        st = guess(lat, lng)
        print("st: ", st)
        ns = "Firstly Travel to " + st + " 🙂 \t"
        reply = default.format(state) + ns + pathsdict[st]
        print(reply)
        return reply


# 26.752396 88.445706 - Sweety
# 26.913448 80.972128 - Prakhar
# 29.989417 75.399699 -Tushar
# 23.174034 75.801618
# 32.27275 75.659703

lat = 26.752396
lng = 88.445706

# suggest_path(lat,lng)