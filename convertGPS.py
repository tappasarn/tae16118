import time
import serial
import pynmea2


def read(filename):
	f = open(filename)
	line = f.readline()
	if line not in ['\n', '\r\n']:
		print("LINEEE ori")
		print(line)
		print("LEN")
		print(len(line))
		msg = pynmea2.parse(line)
		print("after parse")
		print(msg)
	
while True:
	read('/dev/ttyAMA0')
