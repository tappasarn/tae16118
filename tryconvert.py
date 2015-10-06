import time
import serial
import pynmea2

msg = pynmea2.parse('$GNGGA,100220.00,,,,,0,06,2.79,,,,,,*43')
print(msg.lat)
print(msg.lon)

