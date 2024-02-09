# Works with either Python 2 or Python 3.
#
# NOTE: The Tic's: control mode must be "Serial / I2C / USB".
 
import subprocess
import yaml
 

def ticcmd(*args):
  return subprocess.check_output(['ticcmd'] + list(args))

def main():
  
  
  status = yaml.safe_load(ticcmd('-s', '--full'))
 
  position = status['Current position']
  print("Current position is at: {}.\n".format(position))
  user_input = input("Enter desired position: ")
  print(" ")
  
  while position != int(user_input):
    ticcmd('--exit-safe-start','--position', str(user_input))
    real_time_status = yaml.safe_load(ticcmd('-s', '--full'))
    real_time_steps = real_time_status['Current position']
    
    if real_time_steps == int(user_input):
      print("Current position is:",real_time_steps)
      break
    
    
    else:
      continue
       
  
  

main()
