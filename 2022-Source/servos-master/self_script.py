import yaml 
import subprocess

# Works with either Python 2 or Python 3.
#
# NOTE: The Tic's: control mode must be "Serial / I2C / USB".
 
import subprocess
import yaml
 
def ticcmd(*args):
  return subprocess.check_output(['ticcmd'] + list(args))
 
status = yaml.safe_load(ticcmd('-s', '--full'))

position = status['Current position']

print("Current position is {}.".format(position))
num_to_stop= 1000


ticcmd('--exit-safe-start','--position',str(num_to_stop))
print("Current position is {}.".format(position))

