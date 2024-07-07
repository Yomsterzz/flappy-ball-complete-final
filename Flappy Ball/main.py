import pgzrun
import random

WIDTH = 800
HEIGHT = 600
TITLE = "Flappy Ball!"

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

r2 = random.randint(0,255)
g2 = random.randint(0,255)
b2 = random.randint(0,255)

r3 = random.randint(0,255)
g3 = random.randint(0,255)
b3 = random.randint(0,255)

r4 = random.randint(0,255)
g4 = random.randint(0,255)
b4 = random.randint(0,255)

color1 = (r,g,b)
color2 = (r2,g2,b2)
color3 = (r3,g3,b3)
color4 = (r4,g4,b4)
radius1 = random.randint(25,100)
radius2 = random.randint(25,100)
radius3 = random.randint(25,100)
radius4 = random.randint(25,100)
gravity = 4000.0

class Ball:
    def __init__(self, color, radius, x, y, xvel):
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = 0

    
    def draw_ball(self):
        self.pos = (self.x, self.y)
        screen.draw.filled_circle(self.pos, self.radius, self.color)
    
ball1 = Ball(color1, radius1, 50, 50, 100)
ball2 = Ball(color2, radius2, 150, 150, 200)
ball3 = Ball(color3, radius3, 250, 250, 300)
ball4 = Ball(color4, radius4, 350, 350, 400)

balls = [ball1, ball2, ball3, ball4]

def draw():
    screen.clear()
    for ball in balls:
        ball.draw_ball()

def update(c):
    #applying gravity
    for ball in balls:
        bally = ball.yvel
        ball.yvel += gravity * c
        ball.y += (bally + ball.yvel) * 0.5 * c

    #adding bounce
    for ball in balls: 
        if ball.y > HEIGHT - ball.radius:
            ball.y = HEIGHT - ball.radius
            ball.yvel = -ball.yvel * 0.9
    
    #changing x-axis movement
    for ball in balls:
        ball.x += ball.xvel * c
        if ball.x > WIDTH - ball1.radius or ball.x < ball.radius:
            ball.xvel = -ball.xvel



def on_key_down(key):
    if key == keys.SPACE:
        ball1.yvel = -2000
        ball2.yvel = -1000
        ball3.yvel = -1500
        ball4.yvel = -2500

pgzrun.go()