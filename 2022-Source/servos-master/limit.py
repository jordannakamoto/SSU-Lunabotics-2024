# Uses the smbus2 library to send and receive data from a Tic.
# Works on Linux with either Python 2 or Python 3.
#
# NOTE: The Tic's control mode must be "Serial / I2C / USB".
# NOTE: For reliable operation on a Raspberry Pi, enable the i2c-gpio
#   overlay and use the I2C device it provides (usually /dev/i2c-3).
# NOTE: You might nee to change the 'SMBus(3)' line below to specify the
#   correct I2C device.
# NOTE: You might need to change the 'address = 11' line below to match
#   the device number of your Tic.

import RPi.GPIO as GPIO
import time 
import subprocess
import yaml

def button_callback(channel):
    print("Button was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(7,GPIO.RISING,callback=button_callback)

def ticcmd(*args):
  return subprocess.check_output(['ticcmd'] + list(args))

def main():

  #GPIO.setwarnings(False) # Ignore warning for now
  #GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
  #GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  #PIO.add_event_detect(17,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
  #button_state = False 
  #pressed = True
  #GPIO.setmode(GPIO.BCM)
  #a =1
  #GPIO.setup(4,GPIO.IN)
  inputValue = GPIO.input(7)

  status = yaml.safe_load(ticcmd('-s', '--full'))
 
  position = status['Current position']
  print("Current position is at: {}.\n".format(position))
  user_input = input("Enter desired position: ")
  print(" ")
  
  while position != int(user_input):
    ticcmd('--exit-safe-start','--position', str(user_input))
    real_time_status = yaml.safe_load(ticcmd('-s', '--full'))
    real_time_steps = real_time_status['Current position']
    upd_value = GPIO.input(7)
  
        
    
    if real_time_steps == int(user_input) or upd_value==GPIO.HIGH :
      print("Current position is:",real_time_steps)
      break

    else:
      continue

    
          
    
       
  
  

main()