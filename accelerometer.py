from i2clibraries import i2c_adxl345
from time import *

class Accelerometer:
	def __init__(self): 
		self.adxl345 = i2c_adxl345.i2c_adxl345(1)
	def getCurrentAcceleroValue(self):
		return self.adxl345.getAxes()
