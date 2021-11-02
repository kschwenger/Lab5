#!/usr/bin/python37all

import cgi
import json
from urllib.request import urlopen # use to send/receive data
from urllib.parse import urlencode # use to structure a GET string

# get data from html form
dataFromhtml = cgi.FieldStorage()
Selection = dataFromhtml.getvalue('stepper_submit')
StepperAngle = dataFromhtml.getvalue('slider')

# save data to text file
data2send = {"stepper_submit":Selection, "slider":StepperAngle}
with open('Lab5.txt', 'w') as f:
  json.dump(data2send,f)

# send data to thingspeak
GETparams = {"api_key":"R4BNKNSZSPTZ7IXD", key1:102}
GETparams = urlencode(GETparams) # format dict as GET string
url = "https://api.thingspeak.com/update"
response = urlopen(url + "?" + GETparams) # send GET request
status = response.status # display request response
reason = response.reason # display response reason

# display user interface (same as html) updated with most recent selection
print('Content-type:text/html\n\n')
print('<html>')

print('Previous selection: ' + Selection + ' ' + StepperAngle + '<br>')
print('<br>')
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