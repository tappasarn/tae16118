import accelerometer
import compass
import gyro
from time import sleep

threadOneAccelero = accelerometer.Accelerometer()
threadOneGyro = gyro.Gyro()
threadOneCompass = compass.Compass()

while True:
	print(threadOneAccelero.getCurrentAcceleroValue())
	sleep(1)
	print(threadOneGyro.getCurrentGyroValue())
	sleep(1)
	print(threadOneCompass.getCurrentCompassValue())
	sleep(1)
