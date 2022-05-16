
#!/usr/bin/python

# vedi https://www.domoticz.com/wiki/Domoticz_API/JSON_URL%27s

import urllib.request
import json
import time

#read domoticz data

f = open("/var/tmp/datafile","w")

url="http://meteo-ve.local:8080/json.htm?type=devices&used=true&filter=all&favorite=1"

data = json.load(urllib.request.urlopen(url))

#print(json.dumps(data, indent=4, sort_keys=True))

parsed_json = data['result'][1]
temp= parsed_json['Temp']
temp = ((temp/5)*9)+32 # Fahrenheit

parsed_json = data['result'][1]
hum = parsed_json['Humidity']

parsed_json = data['result'][2]
dir = parsed_json['Direction']

parsed_json = data['result'][2]
speed = parsed_json['Speed']
speed = float(speed)/1.609 # miles/h

parsed_json = data['result'][3]
rain = parsed_json['Rain']
rain = float(rain) * 0.393701 # inch/h

parsed_json = data['result'][0]
bar = parsed_json['Barometer']
bar = float(bar) * 0.02953 # inHg

parsed_json = data['result'][0]
intemp= parsed_json['Temp']
intemp= ((intemp/5)*9)+32 # Fahrenheit


print ('Temp: ',temp,'Hum: ',hum,'Wind dir: ',dir,'Wind speed: ',speed,'Bar: ',bar,'Rain: ',rain,'inTemp: ',intemp)

f.write("outTemp="+str(temp)+"\n")
f.write("outHumidity="+str(hum)+"\n")
f.write("barometer="+str(bar)+"\n")
f.write("rain="+str(rain)+"\n")
f.write("windSpeed="+str(speed)+"\n")
f.write("windDir="+str(dir)+"\n")
f.write("inTemp="+str(intemp)+"\n")

f.close()
