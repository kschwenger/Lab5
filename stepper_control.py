#!/usr/bin/python37all
import cgi
import json

# get data from html form
dataFromhtml = cgi.FieldStorage()
Selection = dataFromhtml.getvalue('stepper_submit')
StepperAngle = dataFromhtml.getvalue('slider')

data2send = {"stepper_submit":Selection, "slider":StepperAngle}
with open('Lab5.txt', 'w') as f:
  json.dump(data2send,f)

print('Content-type:text/html\n\n')
print('<html>') 
print('Select Stepper Angle <br>')
print('<form action="/cgi-bin/stepper_control.py" method="POST">')
print('<br>')
print('0 deg <input type="range" name="slider" min ="0" max="360" value ="180"/> 360 deg <br>')
print('<br>')
print('<input type="submit" name="stepper_submit" value="Apply_Angle">')
print('<br>')
print('<br>')
print('Or')
print('<br>')
print('<br>')
print('<input type="submit" name="stepper_submit" value="Zero_Stepper">')
print('</form>')
print('</html>')