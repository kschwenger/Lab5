#!/usr/bin/python37all
import cgi
import json

# get data from html form
dataFromhtml = cgi.FieldStorage()
Selection = dataFromhtml.getvalue('stepper_submit')
StepperAngle = dataFromhtml.getvalue('slider')

# consider sending both selection and angle no matter what, and doing if in the background code
if Selection == Apply_Angle:
  #save StepperAngle to text file
  data2send = {"slider":StepperAngle}
elif Selection == Zero_Stepper:
  #save zero function to txt file, not angle 
  data2send = {"selection":Selection}

with open('Lab5.txt', 'w') as f:
  json.dump(data2send,f)