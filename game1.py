import pgzrun
from random import randint

HEIGHT = 700
WIDTH = 1200

w , h = WIDTH, HEIGHT

music.play('remix')

p = Actor('ironman', (w//2,h//2))
e = Actor('alien', (w//2, 200))
c = Actor('coin', (w//2, h-100))
score = 0
game_state = 0


def draw():
    if game_state == 0:
        screen.fill('white')
        p.draw()
        e.draw()
        c.draw()
        screen.draw.text(f"Score: {score}", (10,10), color = 'black')
    elif game_state == 1:
        screen.draw.text(f"Game Over", (w//2, h//2), color = 'red')
    elif game_state == 2:
        screen.draw.text(f"You Win", (w//2, h//2), color = 'green')

def player_update():
    if keyboard.left:
        p.x -= 5
    if keyboard.right:
        p.x += 5
    if keyboard.up:
        p.y -= 5
    if keyboard.down:
        p.y += 5
    
    #player moment
    if p.x > w:
        p.x = 0
    if p.y > h:
        p.y = 0
    if p.x < 0:
        p.x = w
    if p.y < 0:
        p.y = h

def enemy_update():
    if c.x > e.x:
        e.x += 3
    if c.x < e.x:
        e.x -= 3
    if c.y > e.y:
        e.y += 3
    if c.y < e.y:
        e.y -= 3

# def player_move_update():
#     if c.x > p.x:
#         p.x += 3
#     if c.x < p.x:
#         p.x -= 3
#     if c.y > p.y:
#         p.y += 3
#     if c.y < p.y:
#         p.y -= 3

def score_update():
    global score, game_state
    if p.colliderect(c):
        score = score + 10
        c.x = randint(0,w)
        c.y = randint(0, h)
        sounds.action.play()
    if e.colliderect(c):
        score = score - 10
        c.x = randint(0,w)
        c.y = randint(0, h)
        sounds.action.play()
    if score <= -50:
        game_state = 1
    if score >= 50:
        game_state = 2

def update():
    if game_state == 0:
        enemy_update()
        player_update()
        score_update()
        # player_move_update()

pgzrun.go()

