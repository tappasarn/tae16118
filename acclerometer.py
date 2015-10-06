from i2clibraries import i2c_adxl345
from time import *
import os
os.system("export QUICK2WIRE_API_HOME=~/myproject/quick2wire-python-api")

os.system("export PYTHONPATH=$PYTHONPATH:$QUICK2WIRE_API_HOME")

adxl345 = i2c_adxl345.i2c_adxl345(port = 1)

while True:
        print(adxl345)
        sleep(1.2)
