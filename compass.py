from i2clibraries import i2c_hmc5883l
import os

#set environment variable
os.system("export QUICK2WIRE_API_HOME=~/myproject/quick2wire-python-api")
os.system("export PYTHONPATH=$PYTHONPATH:$QUICK2WIRE_API_HOME")

class Compass:
	def __init__(self):
		self.hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
		self.hmc5883l.setContinuousMode()
		self.hmc5883l.setDeclination(9,54)
	def getCurrentCompassValue(self):
		return self.hmc5883l
