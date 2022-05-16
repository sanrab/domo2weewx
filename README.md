# domo2weewx
python script to transfer domoticz data to weewx

Weather data collected by HIDEKI TS04 (433 MHz) and BMP180 sensors (I2C), Raspberry 3B, RfLink USB Gateway 433 MHz
domo2weewx.py genera ogni 5 minuti file /var/tmp/datafile

outTemp=78.62
outHumidity=52
barometer=30.008386
rain=0.0
windSpeed=0.3107520198881293
windDir=349.0
inTemp=76.64

Il file viene letto da weewx con driver Fileparse
