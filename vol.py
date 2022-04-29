from AllumeCamera import AllumeCamera
from ajouter import ajouter
from retourALaLigne import retourALaLigne
from EteintCamera import EteintCamera
import capteurMPL3115A2
import capteurDHT22
import picamera
from time import sleep
import os

sleep(1800)
sensor1=capteurMPL3115A2.Initialisation()
sensor2=capteurDHT22.Initialisation()
camera=picamera.PiCamera()
f=open('donnees.txt','w')
f.write('Pression,Altitude,TemperatureMPL,TemperatureDHT,Humidité')
f.close()
a2=-1000
a1=capteurMPL3115A2.Altitude(sensor1)
AllumeCamera(camera)

while (a2<a1 or a1>5000):
	try:
		tdht=capteurDHT22.Temperature(sensor2)
		hdht=capteurDHT22.Humidite(sensor2)
	except RuntimeError:
		continue
	retourALaLigne()
	a2=a1
	ajouter(capteurMPL3115A2.Pression(sensor1))
	ajouter(capteurMPL3115A2.Altitude(sensor1))
	a1=capteurMPL3115A2.Altitude(sensor1)
	ajouter(capteurMPL3115A2.Temperature(sensor1))
	ajouter(tdht)
	ajouter(hdht)
	sleep(30)

EteintCamera(camera)

while (a2>a1):
	try:
		tdht=str(capteurDHT22.Temperature(sensor2))
		hdht=str(capteurDHT22.Humidite(sensor2))
	except RuntimeError:
		continue
	retourALaLigne()
	a2=a1
	ajouter(str(capteurMPL3115A2.Pression(sensor1)))
	ajouter(str(capteurMPL3115A2.Altitude(sensor1)))
	a1=capteurMPL3115A2.Altitude(sensor1)
	ajouter(str(capteurMPL3115A2.Temperature(sensor1)))
	ajouter(tdht)
	ajouter(hdht)
	sleep(30)

os.system('sudo shutdown -h now')
