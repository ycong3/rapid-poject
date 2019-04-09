alien = Actor('skull')
hero = Actor('spaceship')
bullet = Actor('bullet')


import random

alien.bottomright = random.randint(20, 200), 0
hero.bottomleft = 90, 290
bullet.bottomleft = hero.bottomleft
WIDTH = 200
HEIGHT = 300
score = 0

def draw():
    screen.clear()
    alien.draw()
    hero.draw()
    bullet.draw()
    screen.draw.text(str(score), topright=(195,5), owidth=0.5, ocolor=(0,0,0), color=(255,255,255), fontsize=20)

def eliminate():
    score += 1

def update():

    alien.bottom += 1
    if alien.top > HEIGHT:
        alien.bottomright = random.randint(20, 200), 0
    if keyboard.left:
        hero.x -= 5
        bullet.x -= 5
    elif keyboard.right:
        hero.x += 5
        bullet.x += 5

    if hero.left == 200:
        bullet.right = 5
        hero.right = 5
    elif hero.right == 0:
        hero.left = 195
        bullet.left = 195
    if bullet.bottomleft == hero.bottomleft:
        if keyboard.space:
            animate(bullet, tween='linear', duration=0.3, on_finished=None, x=hero.x, y=0)
            clock.schedule_unique(set_bullet_normal, 0.3)

    if alien.bottom > bullet.top and alien.right >= bullet.left and alien.left <= bullet.right:
        set_alien_hurt()

        set_bullet_normal()


def set_alien_hurt():

    alien.image = 'boom'
    # sounds.eep.play()
    alien.bottom -= 1


    clock.schedule_unique(set_alien_normal, 0.1)

def set_alien_normal():
    alien.image = 'skull'
    alien.bottomright = random.randint(20, 200), 0
    global score
    score += 1

def set_bullet_normal():
    bullet.bottomleft = hero.bottomleft