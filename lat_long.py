import serial
import time
import string
import pynmea2

port='/dev/ttyS0'
ser=serial.Serial(port,baudrate=9600,timeout=0.5)

while True: 
	newdata=ser.readline()
	if newdata[1:6]==b'GPRMC':
		newmsg=pynmea2.parse(newdata)
		lat=newmsg.latitude
		lng=newmsg.longitude
		gps='Latitude=' +str(lat) + 'and Longitude=' +str(lng)
		print(gps)