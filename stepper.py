import RPi.GPIO as GPIO
import time

class Stepper:

  # Define the pin sequence for counter-clockwise motion, noting that
  # two adjacent phases must be actuated together before stepping to
  # a new phase so that the rotor is pulled in the right direction:
  sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
  [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

  state = 0 # current position in stator sequence

  led = 17 # led pin 

  def __init__(self, pins):
    self.pins = pins
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
      GPIO.setup(pin, GPIO.OUT, initial=0)

  def delay_us(tus): 
    # use microseconds to improve time resolution
    endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < endTime:
      pass

  def __halfstep(dir):
    # dir = +/- 1 (ccw/cw)
    state += dir # increment to go forward, decrement to go backward, thats why we use +/-1
    if state > 7:
      state = 0
    elif state < 0:
      state = 7
    for pin in range(4): # 4 pins that need to be energized
      GPIO.output(pins[pin], sequence[state][pin])
    delay_us(1000) # 1 ms, this will be changed for different speeds
  
  def __moveSteps(steps, dir):
    # move the actuation sequence a given number of halfsteps
    for step in range(steps):
      halfstep(dir)

  def goAngle(self, angle, currentangle):
    #convert angles to steps (0.703 deg/step)
    currentsteps = float(currentangle)/0.703
    steps = float(angle/0.703)
    if steps > currentsteps:
      dir = 1
    elif steps < currentsteps:
      dir = -1
    __moveSteps(steps, dir)
    currentangle = angle

  #def zero():
    # halfstep until led is blocked
    #while read(0) > 10:
      #GPIO.output(led, 1)
      #halfstep(1)
      