__author__ = 'Amal G Jose'

import time
import serial
import string
from pynmea import nmea

#location where gps sending all the info from satellite
ser = open('/dev/ttyAMA0')
#object from nmea
gpgga = nmea.GPGGA()
while True:
	data = ser.readline()
	if data[0:6] == '$GNGGA':
		#parse only if the header tag is GNGGA which is the one that contain lat and lon information
		gpgga.parse(data)
		#get latitude 
        	lats = gpgga.latitude
        	print "Latitude values : " + str(lats)
		#get longitude
       		longitude = gpgga.longitude
       		print "Longitude values : " + str(longitude)
      
