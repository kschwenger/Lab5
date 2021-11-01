import json
import RPi.GPIO as GPIO
import time

with open('Lab5.txt', 'r') as f:
  data = json.load(f)