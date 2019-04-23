import pgzrun
from gpiozero import *
from time import sleep



alien = Actor('skull')
hero = Actor('spaceship')
bullet = Actor('bullet')
# bullet_2 = Actor('bullet')
# bullet_3 = Actor('bullet')

import random

pin0 = DigitalInputDevice(27)
pin1 = DigitalInputDevice(17)
pin2 = DigitalInputDevice(22)

ultrasonic = DistanceSensor(echo = 18, trigger = 4, max_distance = 5)


# DigitalInputDevice(18)
# reading = port.read(12)
# reading = DigitalInputDevice(18)

alien.bottomright = random.randint(20, 200), 0 # set alien positoin on the top of the screen, the image start with bottom rgiht
hero.bottomleft = 90, 290 # set space ship position on the bottom of the screen, the image start with bottom right
bullet.bottomleft = hero.bottomleft # set bullet position same as the space ship
WIDTH = 200 # set display size 200*300
HEIGHT = 300
score = 0 # set score
hurt = 0
game = 1 # game running > 1; game over > 0

def draw():
    screen.clear()
    screen.blit('background', (0, 0))
    alien.draw()
    bullet.draw()
    hero.draw()
    screen.draw.text(str(ultrasonic.distance), center=(100,30), owidth=0.5, ocolor=(0,0,0), color=(255,255,255), fontsize=20)
    if game == 1:
        screen.draw.text(str(score), topright=(195,5), owidth=0.5, ocolor=(0,0,0), color=(255,255,255), fontsize=20)
        
    if game == 0:
        
        screen.draw.text("SCORE", center=(100,100), owidth=0.5, ocolor=(0,0,0), color=(255,255,255), fontsize=24)
        screen.draw.text(str(score), center=(100,130), owidth=0.5, ocolor=(0,0,0), color=(255,255,255), fontsize=30)
        screen.draw.text("GAME OVER", center=(100,170), owidth=0.5, ocolor=(0,0,0), color=(255,255,255), fontsize=20)
        screen.draw.text("PRESS A TO RESTART", center=(100,190), owidth=0.5, ocolor=(0,0,0), color=(255,255,255), fontsize=20)

def eliminate(): # every time an alien is killed score + 1
    score += 1

def update():
    global hurt
    global game

     # set alien speed
    if alien.bottom > hero.top:
        alien.image = 'boom'
        game = 0
    elif hurt == 1:
        alien.bottom += 0
        # alien.bottomright = random.randint(20, 200), 0
    else:
        alien.bottom += 4
    if keyboard.left and hero.left >= 5 and game == 1:
        hero.x -= 5
        bullet.x -= 5
    elif keyboard.right and hero.right <= (WIDTH - 5) and game == 1:
        hero.x += 5
        bullet.x += 5
    if pin0.value == 1 and hero.left >= 5 and game == 1: # microbit control, if button A is pressed, move left
        hero.x -= 4 
        bullet.x -= 4
    elif pin1.value == 1 and hero.right <= (WIDTH - 5) and game == 1: # microbit control, if button B is pressed, move right
        hero.x += 4
        bullet.x += 4

    if game == 0 and pin2.value == 1:
        game = 1
        init()
        set_alien_normal()
        set_bullet_normal()

    if bullet.bottomleft == hero.bottomleft and game == 1:
        animate(bullet, tween='linear', duration=0.3, on_finished=None, x=hero.x, y=0)
        clock.schedule_unique(set_bullet_normal, 0.3)

    if alien.bottom > bullet.top and alien.right >= bullet.left and alien.left <= bullet.right:
        hurt = 1
        set_alien_hurt()

        set_bullet_normal()


def set_alien_hurt():
    alien.image = 'boom'
    # sounds.eep.play()

    clock.schedule_unique(set_alien_normal, 0.1)

def set_alien_normal():
    alien.image = 'skull'
    alien.bottomright = random.randint(20, 200), 0
    global hurt
    hurt = 0
    global score
    score += 1

def set_bullet_normal():
    bullet.bottomleft = hero.bottomleft

def init():
    global score
    score = -1


pgzrun.go()
