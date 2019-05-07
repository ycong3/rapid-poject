


The project is composed of a 2.8-inch portable monitor, a Micro:bit, a Raspberry Pi, a portable power bank, and a sound sensor(microphone). 

**Game Name:** Earth Guardian

**Background Story:** In 20xx, a group of aliens start to invade Earth. A hero drives the spaceship to protect the earth, Although it is impossible to keep alive in such chaos, the hero must try to kill as many aliens as possible before dying.

**How to play:**

To set up the device, plug the Micro:bit to raspberry pi and flash mbControl.py to it. Connect pin0, pin1, and pin2 on Micro:bit to GPIO 27, 17 and 22 on raspberry pi. Connect the pin on the microphone to GPIO 26 on raspberry pi and make sure it’s connected to the power(use 5v pin and ground pin on raspberry pi). For the monitor, the 2.8 inch monitor that has extended pins is preferred so you can use minimum space to plug sensors and the monitor at the same time. Then connect raspberry pi with any battery. After setting up the hardware above, open game.py in any python editor and run the module. 

To play the game, the player uses the accelerometer on Micro: bit to control the position of the spaceship and constantly make sounds to activate the sound sensor and shoot the aliens falling down from the top of the screen. Each kill scores 1 point. The game is over when the alien touches the city. The goal is to kill more enemies in a row to get a higher score.



[![N|Solid](https://github.com/ycong3/rapid-project/blob/master/Earth%20Guardian.png?raw=true)](https://github.com/ycong3/rapid-project/blob/master/Earth%20Guardian.png?raw=true)
