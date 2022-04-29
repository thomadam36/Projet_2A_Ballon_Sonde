import board
import adafruit_mpl3115a2

def Initialisation():
	i2c=board.I2C()
	sensor1=adafruit_mpl3115a2.MPL3115A2(i2c)
	sensor1.sealevel_pressure=101325
	return sensor1

def Altitude(sensor1):
	return (sensor1.altitude)

def Pression(sensor1):
	return (sensor1.pressure)

def Temperature(sensor1):
	return (sensor1.temperature)
