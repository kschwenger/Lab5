import sys
from stepper import Stepper
import json
import time

# create stepper object from Stepper class with specified pins
pins = [12,16,20,21]
myStepper = Stepper(pins)

while True: # run continually
  # read saved data from CGI code
  with open('Lab5.txt', 'r') as f:
    data = json.load(f)

  if data['stepper_submit'] == "Apply_Angle": # if user changes angle
    print("Turning to angle " + data['slider']) 
    myStepper.goAngle(int(data['slider']))  # use class method to go to specified angle
  
  elif data['stepper_submit'] == "Zero_Stepper":  # if user selects zero
    # turn stepper until led is blocked using class methods
    myStepper.zero()
    print("Stepper Zeroed")
  
  # send empty line to text file so it doesn't keep spinning
  data2send = {"stepper_submit":" ", "slider":" "}
  with open('Lab5.txt', 'w') as f:
    json.dump(data2send,f)
  
  # sleep to give time to read txt file
  time.sleep(.1)

GPIO.cleanup() 