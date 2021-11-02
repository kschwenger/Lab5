import sys
from stepper import Stepper
from PCF8591 import PCF8591

import json
import RPi.GPIO as GPIO
import time

# create ADC object from PCF class with specified address 
myADC = PCF8591(0x48)

# create stepper object from Stepper class with specified pins
pins = [12,16,20,21]
myStepper = Stepper(pins)

currentangle = 0 # current angle (start at zero)

# read saved data from CGI code
with open('Lab5.txt', 'r') as f:
  data = json.load(f)

if data['selection'] == "Apply_Angle":
  # turn stepper to angle using class methods
  myStepper.goAngle(int(data['angle']), currentangle)
elif data['selection'] == "Zero_Stepper":
  # turn stepper until led is blocked using class methods (and reading ADC from PCF class method)
  pass
  