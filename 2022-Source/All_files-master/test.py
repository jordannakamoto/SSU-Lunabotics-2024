from __future__ import print_function
import time
from dual_g2_hpmd_rpi import motors, MAX_SPEED

# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if motors.motor1.getFault():
        raise DriverFault(1)
    if motors.motor2.getFault():
        raise DriverFault(2)

# Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
  [MAX_SPEED] * 200 + list(range(MAX_SPEED, 0, -1)) + [0]

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 200 + list(range(-MAX_SPEED, 0, 1)) + [0]

#try:
motors.setSpeeds(0, 0)
motors.enable()
val = int(input('Enter 1 for fowards or 0 for reverse....crtl c to stop:'))
val2 = int(input('Enter speed value 0-1:'))

if (val == 1):
   motors.enable()
   motors.motor1.setSpeed(MAX_SPEED/val2)
   print("Motor Forward")
   enter = input('ENTER:')
   if enter == 1:
        motors.disable()
        print("Motor Stopped")
elif (val == 0):
   motors.enable()
   motors.motor1.setSpeed(-MAX_SPEED/val2)
   print("Motor Reverse")
   enter2 = input('ENTER:')
   if enter2 == 2:
        motors.disable()
        print("Motor Stopped")


