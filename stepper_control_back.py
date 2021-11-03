import sys
from stepper import Stepper
from PCF8591 import PCF8591

import json
import RPi.GPIO as GPIO
import time

# create ADC object from PCF class with specified address 
#myADC = PCF8591(0x48)

# create stepper object from Stepper class with specified pins
pins = [12,16,20,21]

myStepper = Stepper(pins)

while True:
  # read saved data from CGI code
  with open('Lab5.txt', 'r') as f:
    data = json.load(f)

  if data['stepper_submit'] == "Apply_Angle":
    # turn stepper to angle using class methods
    print("Turning to angle " + data['slider'])
    myStepper.goAngle(int(data['slider']))
  elif data['stepper_submit'] == "Zero_Stepper":
    # turn stepper until led is blocked using class methods (and reading ADC from PCF class method)
    myStepper.zero()
    print("Stepper Zeroed")
  
  data2send = {"stepper_submit":" ", "slider":" "}
  with open('Lab5.txt', 'w') as f:
    json.dump(data2send,f)
  
  time.sleep(.1)

GPIO.cleanup() 