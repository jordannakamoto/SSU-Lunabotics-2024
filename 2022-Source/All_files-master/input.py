from __future__ import print_function
import time
import string
import sys
from dual_g2_hpmd_rpi import motors, MAX_SPEED
#import keyboard
# Define a custom exception to raise if a fault is detected.
class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if motors.motor1.getFault():
        raise DriverFault(1)
   # if motors.motor2.getFault():
   #     raise DriverFault(2)

# Set up sequences of motor speeds.
test_forward_speeds = list(range(0, MAX_SPEED, 1)) + \
 [MAX_SPEED] * 300 + list(range(MAX_SPEED, 0, -1)) + [0]

test_reverse_speeds = list(range(0, -MAX_SPEED, -1)) + \
  [-MAX_SPEED] * 300 + list(range(-MAX_SPEED, 0, 1)) + [0]

#try:
motion = 0
motion = int(input('Enter 1 for Forward or 2 for Reverse:')
#motors.setSpeeds(0)

#enter = 1
#enter2 = 3
#while enter == 1:
while motion == 1:
   motors.enable()
   motors.motor1.setSpeed(MAX_SPEED/10)
   motors.motor1.setSpeed(MAX_SPEED/9)
   motors.motor1.setSpeed(MAX_SPEED/8)
   motors.motor1.setSpeed(MAX_SPEED/7)
   motors.motor1.setSpeed(MAX_SPEED/6)
   motors.motor1.setSpeed(MAX_SPEED/5)
   motors.motor1.setSpeed(MAX_SPEED/4)
   motors.motor1.setSpeed(MAX_SPEED/3)
   motors.motor1.setSpeed(MAX_SPEED/2)
   motors.motor1.setSpeed(MAX_SPEED)
   print("Motor Forward")
   enter = input('Stop?:')
   if enter == ('Yes'):
              motors.disable()
              break
print("Motor Stopped")
motors.disable()
time.sleep(0.5)

motors.setSpeeds(-1,-1)

#while enter2 == 3:
while motion == 2:
   motors.enable()
   #enter2 = 2
   motors.motor1.setSpeed(-MAX_SPEED/10)
   motors.motor1.setSpeed(-MAX_SPEED/9)
   motors.motor1.setSpeed(-MAX_SPEED/8)

   motors.motor1.setSpeed(-MAX_SPEED/7)
   motors.motor1.setSpeed(-MAX_SPEED/6)
   motors.motor1.setSpeed(-MAX_SPEED/5)
   motors.motor1.setSpeed(-MAX_SPEED/4)
   motors.motor1.setSpeed(-MAX_SPEED/3)
   motors.motor1.setSpeed(-MAX_SPEED/2)
   motors.motor1.setSpeed(-MAX_SPEED)
   print("Motor Reverse")
   enter2 = input('Stop?:')
   if enter2 == ('Yes'):
              break
   time.sleep(0.002)
   motors.forceStop()
print("Motor Stopped")
motors.disable()
time.sleep(0.5)
#finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
#    motors.forceStop()

