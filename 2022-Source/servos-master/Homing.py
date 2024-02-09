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
import keyboard
import time 
from smbus2 import SMBus, i2c_msg




def button_callback(channel): # function for physical push button '''prints ["Button was pushed"} 
    print("Button was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 37 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(37,GPIO.RISING,callback=button_callback)


class TicI2C(object):
  def __init__(self, bus, address):
    self.bus = bus
    self.address = address
 
  # Sends the "Exit safe start" command.
  def exit_safe_start(self):
    command = [0x83]
    write = i2c_msg.write(self.address, command)
    self.bus.i2c_rdwr(write)
 
  # Sets the target position.
  #
  # For more information about what this command does, see the
  # "Set target position" command in the "Command reference" section of the
  # Tic user's guide.
  
  
  def set_target_position(self, target):
    command = [0xE0,
      target >> 0 & 0xFF,
      target >> 8 & 0xFF,
      target >> 16 & 0xFF,
      target >> 24 & 0xFF]
    write = i2c_msg.write(self.address, command)
    self.bus.i2c_rdwr(write)


  def haltAndHold(self):
    command = [0x89]
    write = i2c_msg.write(self.address, command)
    self.bus.i2c_rdwr(write)



  # Gets one or more variables from the Tic.
  def get_variables(self, offset, length):
    write = i2c_msg.write(self.address, [0xA1, offset])
    read = i2c_msg.read(self.address, length)
    self.bus.i2c_rdwr(write, read)
    return list(read)
 
  # Gets the "Current position" variable from the Tic.
  def get_current_position(self):
    b = self.get_variables(0x22, 4)
    position = b[0] + (b[1] << 8) + (b[2] << 16) + (b[3] << 24)
    if position >= (1 << 31):
      position -= (1 << 32)
    return position
 
# Open a handle to "/dev/i2c-3", representing the I2C bus.
bus = SMBus(1)
 
# Select the I2C address of the Tic (the device number).

address2 = 16  


tic2 = TicI2C(bus,address2)





 # Represents /dev/i2c-3
#
#
#
#
#
# below is a function for pressing a key to give 10 steps 
# "w" for up & "s" for down





def main():
   print("Current postion is: ",tic2.get_current_position(),"\n")
   des = input("Enter (h) for Homing, (d) for Dumping, (m) for Mining: ")
   if(des == 'h'):
      
      tic2.set_target_position(1)
   elif(des == 'd'):
      tic2.set_target_position(100)
   elif(des == 'm'):
      tic2.set_target_position(100)
   else:
      print("Error!")

   while True:
      userInput = input("Enter (w) for up and (s) for down: ")
      print(tic2.get_current_position())
      user_input = 50
      if (userInput == 'w'):
          x = tic2.get_current_position()
          b = x + 100
          tic2.set_target_position(b)
 	
      elif(userInput == 's'):
         x = tic2.get_current_position()
         b = x - 100
         tic2.set_target_position(b)

     
      else:
         print("Error!")   
 
 
 
 
 
 
  #pos = tic2.get_current_position()
  #print("Current position is: {}.".format(pos))
  #user_input = input("Enter desired position: ") # this asks the user for the number of steps, for the motor to take 
  #while pos != int(user_input): # Run till the steps are equal to the user's input 
    #tic.exit_safe_start()
    #tic.set_target_position(int(user_input))

    #tic2.exit_safe_start()
    #tic2.set_target_position(int(user_input))
    
    #real_position = tic.get_current_position() # checks and updates the position/number of steps 'aka counter'
    
    #real_pos = tic2.get_current_position()
    
    #upd_value = GPIO.input(37)
    
    #if int(user_input) == real_pos or upd_value==GPIO.HIGH : # if push-button is pressed stop the stepper motor 
      #tic.haltAndHold() 
      
   #   tic2.haltAndHold()
      
  #    time.sleep(1.5)
      #status_upd= tic.get_current_position() #this updates the number of steps/position, after the push button switch is pressed
      
 #     status_u= tic2.get_current_position()

      #print("Current position is:",status_upd)
#      print("Current position is:",status_u)
     #break
    
    
    #else:
      #continue
       
  
  

main()
