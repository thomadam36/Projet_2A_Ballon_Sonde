import adafruit_dht
import board

def Initialisation():
	dht_device = adafruit_dht.DHT22(board.D4)
	return dht_device

def Temperature(sensor2):
	return (sensor2.temperature)

def Humidite(sensor2):
	return (sensor2.humidity)
