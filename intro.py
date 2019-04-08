alien = Actor('skull')
hero = Actor('spaceship')
bullet = Actor('bullet')

alien.bottomright = 100, 0
hero.bottomleft = 90, 290
bullet.bottomleft = hero.bottomleft
WIDTH = 200
HEIGHT = 300

def draw():
    screen.clear()
    alien.draw()
    hero.draw()
    bullet.draw()

def update():
    alien.bottom += 1
    if alien.top > HEIGHT:
        alien.bottom = 0
    if keyboard.left:
        hero.x -= 5
        bullet.x -= 5
    elif keyboard.right:
        hero.x += 5
        bullet.x += 5

    if keyboard.space:
        animate(bullet, tween='linear', duration=0.3, on_finished=None, pos=(hero.left,0))
        clock.schedule_unique(set_bullet_normal, 0.3)

    if alien.bottom > bullet.top:
        set_alien_hurt()
        alien.bottom += 0
        set_bullet_normal()
        alien.bottom = 0


def set_alien_hurt():
    alien.image = 'boom'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 0.2)

def set_alien_normal():
    alien.image = 'skull'

def set_bullet_normal():
    bullet.bottomleft = hero.bottomleft
