from i2clibraries import i2c_itg3205
from time import *
import os
#set the environment variables
os.system("export QUICK2WIRE_API_HOME=~/myproject/quick2wire-python-api")
os.system("export PYTHONPATH=$PYTHONPATH:$QUICK2WIRE_API_HOME")

class Gyro:
	def __init__(self):
		self.itg3205 = i2c_itg3205.i2c_itg3205(port=1,addr=0x68)
	def getCurrentGyroValue(self):
		(itgready, dataready) = self.itg3205.getInterruptStatus()
		if dataready:
			return self.itg3205.getDegPerSecAxes()
