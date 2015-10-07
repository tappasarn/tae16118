import RPi.GPIO as GPIO
import time

# same command set as nut's module
COMMAND_NONE = 0
COMMAND_UP = 1
COMMAND_UPRIGHT = 2
COMMAND_RIGHT = 3
COMMAND_DOWNRIGHT = 4
COMMAND_DOWN = 5
COMMAND_DOWNLEFT = 6
COMMAND_LEFT = 7
COMMAND_UPLEFT = 8

# set up gpio variable here

servo = 18
motor = 13
motor_control_a = 17
motor_control_b = 27

pwm = None
motor_pwm = None

# Below here are top level method


# call this method to init gpio port that we need to use
def init_gpio():

    global pwm
    global motor_pwm
    GPIO.setmode(GPIO.BCM)

    # set up servo
    GPIO.setup(servo, GPIO.OUT)
    pwm = GPIO.PWM(servo, 50)
    pwm.start(0)

    # set up enable for motor
    GPIO.setup(motor, GPIO.OUT)
    motor_pwm = GPIO.PWM(motor, 100)
    motor_pwm.start(0)

    # set up control for motor
    GPIO.setup(motor_control_a, GPIO.OUT)
    GPIO.setup(motor_control_b, GPIO.OUT)


# command set for robot to move forward
def move_forward(value):
    servo_direction(2)
    motor_direction(1)
    motor_pwm.ChangeDutyCycle(value)


def move_forward_servo_left(value):
    servo_direction(1)
    motor_direction(1)
    motor_pwm.ChangeDutyCycle(value)


def move_forward_servo_right(value):
    servo_direction(3)
    motor_direction(1)
    motor_pwm.ChangeDutyCycle(value)


# command set for robot to move backward
def move_backward(value):
    servo_direction(2)
    motor_direction(2)
    motor_pwm.ChangeDutyCycle(value)


def move_backward_servo_left(value):
    servo_direction(1)
    motor_direction(2)
    motor_pwm.ChangeDutyCycle(value)


def move_backward_servo_right(value):
    servo_direction(3)
    motor_direction(2)
    motor_pwm.ChangeDutyCycle(value)


# command set for controlling servo
def turn_servo_left():
    servo_direction(1)


def turn_servo_right():
    servo_direction(3)


def turn_servo_middle():
    servo_direction(2)


# stop
def stop():
    motor_pwm.ChangeDutyCycle(0)


# below here will not be top level method
# set degree of servo
def servo_direction(direction):
    # 1 is left, 2 is middle, 3 is right
    if direction == 1:
        pwm.ChangeDutyCycle(5)

    elif direction == 2:
        pwm.ChangeDutyCycle(8.5)

    elif direction == 3:
        pwm.ChangeDutyCycle(12)


# method to switch the direction of motor
def motor_direction(direction):
    if direction == 1:
        GPIO.output(motor_control_a, GPIO.HIGH)
        GPIO.output(motor_control_b, GPIO.LOW)
    elif direction == 2:
        GPIO.output(motor_control_b, GPIO.HIGH)
        GPIO.output(motor_control_a, GPIO.LOW)



