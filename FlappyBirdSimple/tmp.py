from turtle import *
from random import randrange
from time import sleep
###########定义变量##########
bird = [-100,80]
ball = [[240,0]]
bird_size = 50
ball_size = 80
###########定义函数##########
def reset():
    global bird,ball,bird_size,ball_size
    bird = [-100,80]
    ball = [[240,0]]
    bird_size = 50
    ball_size = 80

def change():
    bird[1] += bird_size

def distance(x,y,a,b):
    return ((a-x)**2 + (b-y)**2)**0.5

def hit():
    for n in range(len(ball)):
        if distance(ball[n][0], ball[n][1], bird[0], bird[1])<(bird_size+ball_size)/2:
            return True
    return False

def inside():
    if bird[1]<-300+bird_size/2 or bird[1]>300-bird_size/2:
        return False
    return True

def draw():
    clear()
    for n in range(len(ball)):
        up()
        goto(ball[n][0],ball[n][1])
        dot(ball_size,"dark green")
        ball[n][0] -= 3
    up()
    goto(bird[0],bird[1])
    dot(bird_size,"yellow")
    bird[1] -= 5
    update()

def gameLoop():
    if randrange(40) == 1:
        x = 240
        y = randrange(-300,300)
        ball.append([x,y])
    if len(ball) != 0:
        if ball[0][0] < -220:
            ball.pop(0)
    draw()
    if (not inside()) or hit():
        sleep(3)
        reset()
    
    ontimer(gameLoop,30)
    
##########主程序########
setup(420,620,0,0)
hideturtle()
tracer(False)
bgcolor("light blue")
listen()
onkey(lambda: change(), " ")
gameLoop()
done()