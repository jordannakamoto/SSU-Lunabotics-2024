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

try:
   motors.setSpeeds(0, 0)

   #print("Motor 1 forward")
#    for s in test_forward_speeds:
 #       motors.motor1.setSpeed(s)
       # raiseIfFault()
      #  time.sleep(0.002)
#	x = ' '
  #  while != 'y': 
#	x = input("Enter:")

   enter = 1
   #enter2 = 2
   while enter == 1:	
	motors.enable()
	motors.motor1.setSpeed(MAX_SPEED/8)
	motors.motor1.setSpeed(MAX_SPEED/7)
	motors.motor1.setSpeed(MAX_SPEED/6)
	motors.motor1.setSpeed(MAX_SPEED/5)
	motors.motor1.setSpeed(MAX_SPEED/4)
	motors.motor1.setSpeed(MAX_SPEED/3)
	#motors.motor1.setSpeed(MAX_SPEED/2)
	#motors.motor1.setSpeed(MAX_SPEED)
	print("Motor Forward")
	enter = input('ENTER:')
	if enter == 2:
		break
	#print("Motor Forward")
	time.sleep(0.002)
#   motors.forcestop()
   print("Motor Stopped")
   motors.disable()

except DriverFault as e:
    print("Driver %s fault!" % e.driver_num)
#else:
#   motors.disable()
#   enter2 = 2
#   while enter2 == 2:
#        test_reverse_speeds
#        motors.enable()
#        motors.motor2.setSpeed(MAX_SPEED/2)

finally:
  # Stop the motors, even if there is an exception
  # or the user presses Ctrl+C to kill the process.
    motors.forceStop()
