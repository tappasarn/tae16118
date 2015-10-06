import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.out)

pwm = GPIO.PMW(12,50)
pwm.start(5)
pwm.ChangeDutyCycle(7.5)
pwm.ChangeDutyCycle(10)

