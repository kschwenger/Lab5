#!/usr/bin/python37all
import cgi
import json

# get data from html form
#dataFromhtml = cgi.FieldStorage()
#Selection = dataFromhtml.getvalue('stepper_submit')
#StepperAngle = dataFromhtml.getvalue('slider')

"""
# consider sending both selection and angle no matter what, and doing if in the background code
if Selection == Apply_Angle:
  # save StepperAngle to text file
  data2send = {"slider":StepperAngle}
elif Selection == Zero_Stepper:
  # save zero function to txt file, not angle 
  data2send = {"selection":Selection}
with open('Lab5.txt', 'w') as f:
  json.dump(data2send,f)
"""
print("""

Content-type:text/html\n\n 
<html> 
Select Stepper Angle <br>
<form action="/cgi-bin/stepper_control.cgi" method="POST">
  <br>
  0 deg <input type="range" name="slider" min ="0" max="360" value ="180"/> 360 deg <br>
  <br>
  <input type="submit" name="stepper_submit" value="Apply_Angle">
  <br>
  <br>
  Or
  <br>
  <br>
  <input type="submit" name="stepper_submit" value="Zero_Stepper">
</form>
</html>

""")