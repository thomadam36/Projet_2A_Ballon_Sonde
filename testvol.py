from AllumeCamera import AllumeCamera
from ajouter import ajouter
from retourALaLigne import retourALaLigne
from EteintCamera import EteintCamera
import capteurMPL3115A2
import capteurDHT22
import picamera
from time import sleep
import os

sleep(10)
sensor1=capteurMPL3115A2.Initialisation()
sensor2=capteurDHT22.Initialisation()
camera=picamera.PiCamera()
f=open('donnees.txt','w')
f.write('Pression,Altitude,TemperatureMPL,TemperatureDHT,Humidité,Temps(s)')
f.close()
a2=10
AllumeCamera(camera)

while (a2<50):
	try:
		tdht=capteurDHT22.Temperature(sensor2)
		hdht=capteurDHT22.Humidite(sensor2)
	except RuntimeError:
		continue
	retourALaLigne()
	ajouter(capteurMPL3115A2.Pression(sensor1))
	ajouter(capteurMPL3115A2.Altitude(sensor1))
	ajouter(capteurMPL3115A2.Temperature(sensor1))
	ajouter(tdht)
	ajouter(hdht)
	ajouter(str(a2))
	a2=a2+10
	sleep(10)

EteintCamera(camera)

while (a2<100):
	try:
		tdht=capteurDHT22.Temperature(sensor2)
		hdht=capteurDHT22.Humidite(sensor2)
	except RuntimeError:
		continue
	retourALaLigne()
	ajouter(capteurMPL3115A2.Pression(sensor1))
	ajouter(capteurMPL3115A2.Altitude(sensor1))
	ajouter(capteurMPL3115A2.Temperature(sensor1))
	ajouter(tdht)
	ajouter(hdht)
	ajouter(str(a2))
	a2=a2+10
	sleep(10)

#os.system('sudo shutdown -h now')
