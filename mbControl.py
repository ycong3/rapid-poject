# source: https://microbit-micropython.readthedocs.io/en/latest/accelerometer.html
from microbit import *
import time

while True:

    # movement control
    if accelerometer.get_x() < 0:
        display.show("A")
        pin1.write_digital(1)
        pin0.write_digital(0)
    elif accelerometer.get_x() > 0:
        display.show("B")
        pin0.write_digital(1)
        pin1.write_digital(0)

    if button_a.is_pressed(): 
        display.show("C")
        pin2.write_digital(1)
        sleep(10)
        pin2.write_digital(0)
        
    elif button_b.is_pressed():
        display.show("D")
        pin2.write_digital(0)
    # check if the microbit is working    

    
    # control bullet strength by volumn
    
    