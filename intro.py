alien = Actor('skull')
hero = Actor('spaceship')
bullet = Actor('bullet')

import random

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
    alien.draw()
    hero.draw()
    bullet.draw()
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
    if alien.top > (HEIGHT - 20):
        alien.image = 'boom'
        game = 0
    elif hurt == 1:
        alien.bottom += 0
        # alien.bottomright = random.randint(20, 200), 0
    else:
        alien.bottom += 2
    if keyboard.left and hero.left >= 5 and game == 1:
        hero.x -= 5
        bullet.x -= 5
    elif keyboard.right and hero.right <= (WIDTH - 5) and game == 1:
        hero.x += 5
        bullet.x += 5

    if game == 0 and keyboard.a:
        game = 1
        init()
        set_alien_normal()
        set_bullet_normal()

    if bullet.bottomleft == hero.bottomleft and keyboard.space and game == 1:
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
