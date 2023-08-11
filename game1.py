import pgzrun

HEIGHT = 700
WIDTH = 1200

w , h = WIDTH, HEIGHT

music.play('remix')

p = Actor('ironman', (w//2,h//2))
e = Actor('alien', (w//2, 200))
c = Actor('coin', (w//2, h-100))


def draw():
    screen.fill('white')
    p.draw()
    e.draw()
    c.draw()

def player_update():
    if keyboard.left:
        p.x -= 5
    if keyboard.right:
        p.x += 5
    if keyboard.up:
        p.y -= 5
    if keyboard.down:
        p.y += 5

def enemy_update():
    e.x += 5
    if e.x > w:
        e.x = 0

def update():
    enemy_update()
    player_update()

pgzrun.go()

