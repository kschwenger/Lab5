#!/usr/bin/python37all

import cgi
import json
from urllib.request import urlopen # use to send/receive data
from urllib.parse import urlencode # use to structure a GET string

# get data from html form
dataFromhtml = cgi.FieldStorage()
Selection = dataFromhtml.getvalue('stepper_submit')

if Selection == "Zero_Stepper": # if user selects zero stepper, set angle as 0
  StepperAngle = 0
elif Selection == "Apply_Angle":  # if user changes angle, set set angle as whatever they picked
  StepperAngle = dataFromhtml.getvalue('slider')

# save data to text file for background code to perform GPIO actions
data2send = {"stepper_submit":Selection, "slider":StepperAngle}
with open('Lab5.txt', 'w') as f:
  json.dump(data2send,f)

# send data to thingspeak
GETparams = {"api_key":"R4BNKNSZSPTZ7IXD", 1:StepperAngle}
GETparams = urlencode(GETparams) # format dict as GET string
url = "https://api.thingspeak.com/update"
response = urlopen(url + "?" + GETparams) # send GET request
status = response.status # display request response
reason = response.reason # display response reason

# display updated user interface (same as html)
print('Content-type:text/html\n\n')
print('<html>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1556318/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&title=Motor+Angle+vs.+Time&type=line&xaxis=Time&yaxis=Motor+Angle"></iframe>')
print('<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/1556318/widgets/375188"></iframe>')
print('<br>')
print('<br>')
print('Select Stepper Angle <br>')
print('<form action="/cgi-bin/stepper_control.cgi" method="POST">')
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