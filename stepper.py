class Stepper:

  def __init__(self, pins):
    self.pins = pins

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

  def goAngle(self, angle):
    #convert angle to steps (0.703 deg/step)
    steps = angle/0.703
    moveSteps(steps, dir)