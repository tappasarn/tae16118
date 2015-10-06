import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18,50)
pwm.start(0)

def update(angle):
	duty = float(angle)/10.0+2.5
	pwm.ChangeDutyCycle(8.5)
	time.sleep(1)
	pwm.ChangeDutyCycle(12)
	time.sleep(1)
	pwm.ChangeDutyCycle(5)
	time.sleep(1)
while True:
	update(180)
