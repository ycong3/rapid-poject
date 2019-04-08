from microbit import *
import time

while True:
    # Read analog value, attached to pin2
    # moisture sensor: ~520 value max (submerged) to 1 min
    # water sensor: ~700 value max (submerged)to 1 min
    time.sleep(0.5)
    reading = pin0.read_analog()
    print((reading,))
