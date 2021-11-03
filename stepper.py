import RPi.GPIO as GPIO
import time
from PCF8591 import PCF8591

# create ADC object from PCF class with specified address 
myADC = PCF8591(0x48)

class Stepper:

  def __init__(self, pins):
    self.pins = pins  # stepper motor pins

    self.led = 17 # led pin
    
    GPIO.setmode(GPIO.BCM)  # gpio setup
    GPIO.setwarnings(False)
    GPIO.setup(self.led, GPIO.OUT, initial=0)
    for pin in pins:
      GPIO.setup(pin, GPIO.OUT, initial=0)
    
    self.currentangle = 0 # store current angular position

    self.state = 0  # current position in stator sequence
    
    # Define the pin sequence for counter-clockwise motion, noting that
    # two adjacent phases must be actuated together before stepping to
    # a new phase so that the rotor is pulled in the right direction:
    self.sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

  def __delay_us(self, tus): 
    # use microseconds to improve time resolution
    endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < endTime:
      pass

  def __halfstep(self, dir):
    # dir = +/- 1 (ccw/cw)
    self.state += dir # increment to go forward, decrement to go backward, thats why we use +/-1
    if self.state > 7:
      self.state = 0
    elif self.state < 0:
      self.state = 7
    for pin in range(4): # 4 pins that need to be energized
      GPIO.output(self.pins[pin], self.sequence[self.state][pin])
    self.__delay_us(1000) # 1 ms, this can be changed for different speeds
  
  def __moveSteps(self, steps, dir):
    # move the actuation sequence a specified number of halfsteps in a direction
    for step in range(int(steps)):
      self.__halfstep(dir)

  def goAngle(self, angle):

    # find difference in angles, convert to steps (512*8 = 4096 halfsteps per 360 deg rotation)    
    # determine direction for shortest path with if statements
    if angle > self.currentangle:
      if ((self.currentangle - 0) + (360 - angle)) <= (angle - self.currentangle):
        dir = -1
        steps = 4096 - int(4096*abs(angle - self.currentangle)/360)
      else:
        dir = 1
        steps = int(4096*abs(angle - self.currentangle)/360)
    else:
      if ((360 - self.currentangle) + (angle - 0)) <= (self.currentangle - angle):
        dir = 1
        steps = 4096 - int(4096*abs(angle - self.currentangle)/360)
      else:
        dir = -1
        steps = int(4096*abs(angle - self.currentangle)/360)

    # move given number of steps and in specified direction
    self.__moveSteps(steps, dir)
    
    # reset current angle
    self.currentangle = angle

  def zero(self): # halfstep until led is blocked
    GPIO.output(self.led, 1)  # turn on led
    time.sleep(.5)  # give time for PCF to read
    while myADC.read(0) < 220:  # move 100 steps forward until led is blocked
      self.__moveSteps(100,1)
    GPIO.output(self.led, 0)  # turn off led
    self.currentangle = 0 # set current angle to 0
      