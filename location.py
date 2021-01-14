pathsdict ={

'Bihar':
"""
You can reach IIT Mandi basically in 2 ways ->\n

• Either reach New Delhi and get a bus of Mandi (U can hop on buses going to Manali as well). You will get the buses at ISBT and can reach ISBT via metro\n
• Other option for you is to go to Chandigarh via train/flight and then take a bus from Chandigarh to Mandi. You have to be a bit careful if which bus station are you going in Chandigarh (cuz there are two in the city , as in Sector 17  and other in Sector 43).
You are supposed to go to Sector 43 for catching the bus for Mandi or Manali

Happy Journey, Will meet you soon :)
"""
,

'Punjab':
"""
Travel from your hometown to <b>Chandigarh</b>\n
From Chandigarh the Buses to Mandi are available at <u>Sector 43</u> bus stand. The other choice from Chandigarh to Mandi is to travel by taxi. The distance between Chandigarh and Mandi is ~200 kms. This distance can be covered in approximately 6 hrs by bus. By taxi, it usually takes around 5 hrs\n
Happy Journey, Will meet you soon 🙂
"""
,

'Uttar Pradesh':
"""

• If travelling via Chandigarh you can take the LKO-CDG express from Lucknow and then reach Mandi through a taxi or bus from Chandigarh. However, the buses available at a time close to train's arrival in Chandigarh are non-AC public buses and can only be taken from the ISBT 43 bus stand which is farther from the railway station\n
• If travelling via Delhi you can take any train to Delhi that has an arrival time in afternoon between 3 to 6 and then travel to Kashmiri Gate Bus Stand. There you can find many buses for Mandi with departure times ranging from 8 to 11\n

<b>Happy Journey, Will meet you soon</b> :)

""",

'Himachal Pradesh':
    """
    I personally suggest to travel from HRTC as on sudden cancellation, they will provide alternative of that but private just do refund.

	<b>Happy Journey, Will meet you soon</b> :)
    """
,


'Madhya Pradesh':
"""
Minimum 15hrs, via flight (1.5hrs, IDR to DEL) and then a semi sleeper bus (11hrs, Delhi to Mandi), rest for intermediate travel. This is the lower limit given your layoff is minimum.

It can take one whole day (or more) if you take a train (to Delhi or Chandigarh) and then a bus (to Mandi)
Preferred way,
If you're traveling with some significant luggage (excessive luggage not recommended even for the first time) - Train, via Chandigarh (or Delhi).
Afterwards, flight via Delhi. Why? Because,
• Costs almost same (with flight bookings done on time)
• Much quicker
• More comfortable
• More reliable (Trains often get delayed on these routes)
You will have to take a bus (or a taxi) to Mandi in any case.
From Mandi, there are institute buses running every 2hrs, so that should not be an issue.
"""
,

'Rajasthan':
"""
Two options you can go for to reach mandi from Jaipur/Rajasthan\n
1) Jaipur- Delhi ISBT via any roadways bus or train and then Delhi- Mandi via Volvo. Volvo buses are regular during night hours, you can book the same on hrtc website. This is the medium of transportation for majority of IIT Mandi students\n
2) Jaipur- Chandigarh via Garib Rath AC or Intercity and then CDG -Mandi through any bus\n
• Duration is almost same for both the options, around 20 hours.
• Train route is cheaper and more convenient.
Suggestion- If you're visiting IIT Mandi for the first time I would suggest you to go for train option. This way you'll be able to see the mesmerizing beauty of Himachal and IIT Mandi aerial view because you'll be travelling to mandi during morning-noon hours from CDG. You may use volvos for forthcoming trips.
"""
,


'Telangana':
"""
• Most of the <b>Flights</b> will be connected flights (Hyd to Delhi and then Delhi to Chandigarh). And bus timings from Delhi to Mandi are more convenient than from Chandigarh to mandi ! If you can find some convenient timings you can go via Chandigarh too. I(although I am a bot lol) always go via Delhi and everyone who travel from South India travel via Delhi
• If you have enough time then <b>Train</b> is also a Good option, Take Telangana Express from secunderabad to New Delhi NDLS timings are quite convenient.

Happy Journey, Will meet you soon 🙂

"""
,
'Chandigarh':
"""
From Chandigarh the buses to Mandi are available at Sector 43 bus stand. The other choice from Chandigarh to Mandi is to travel by taxi. The distance between Chandigarh and Mandi is ~200 kms. This distance can be covered in approximately 6 hrs by bus. By taxi, it usually takes around 5 hrs\n
Happy Journey, Will meet you soon 🙂
"""
,

'Delhi':
"""
I personally suggest to travel from HRTC as on sudden cancellation, they will provide alternative of that but private just do refund.
You will get the buses to Mandi at ISBT Delhi and can reach ISBT via metro\n
Happy Journey, Will meet you soon 🙂
""",

'Maharashtra':
"""
The best way to travel from Pune/Mumbai is to board a flight from Pune International Airport to Chandigarh International Airport\n
The flight is usually of 2.5 hrs and hence I recommend a morning flight as one has to catch a bus from Chandigarh to Mandi which is of 7 hours.The first HRTC bus departs at 12 pm from Chandigarh sector 43 bus stand and reaches Mandi around 7 pm in the evening.Then you have to take a bus to Kamand campus from the Old campus bus stand.You will reach the campus by 8pm\n
Happy Journey, Will meet you soon 🙂
"""
}

default = "I am still learning all possible routes, Sorry I dont know in detail about how to travel from {} to IIT MANDI as of now, The best I can suggest is:\n"

import requests
import numpy as np

def guess(lat,lng):

	user = np.array((lat,lng))
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


def suggest_path(lat,lng):

	parameters = {
	    "latlng": str(lat)+ "," + str(lng),
	    "key": "AIzaSyCcch7hB-Li7LLL-CdjSt0m7wAEYeJbjkU"
	}

	response=requests.get('https://maps.googleapis.com/maps/api/geocode/json',params = parameters )
	print(type(response))
	print(response.content.decode('UTF-8'))
	resp_json_payload = response.json()

	print("------------------")

	hier = resp_json_payload['results'][0]['address_components'] #hierarchy
	address = resp_json_payload['results'][0]["formatted_address"]
	
	for d in hier:
		if("administrative_area_level_1" in d['types']):
			state = d['long_name']
			break	

	print(state)
	f = open('users_adress.txt', 'a')
	f.write(address+'\n')
	f.close()

	if state in pathsdict:
		print("i am in if condition")
		print(pathsdict[state])
		return pathsdict[state]
	else:
		st = guess(lat,lng)
		print("st: ",st)
		ns = "Firstly Travel to " + st + " 🙂 \t"
		reply = default.format(state) + ns + pathsdict[st]
		print(reply)
		return reply

# 26.752396 88.445706 - Sweety
# 26.913448 80.972128 - Prakhar
# 29.989417 75.399699 -Tushar
# 23.174034 75.801618
# 32.27275 75.659703


# lt = 23.174034
# ln = 75.801618

# suggest_path(lt,ln)