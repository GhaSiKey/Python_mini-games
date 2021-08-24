from turtle import *
from gamebase import square
from COLOR import COLORS
from random import randrange, choice

##########定义变量###########
ballons = []
size = 50

###########定义函数##########
def distance(x,y,a,b):
    return ((a-x)**2 + (b-y)**2)**0.5

def tap(x,y):
    for n in range(len(ballons)):
        if distance(x, y, ballons[n][0], ballons[n][1])<(size/2):
            ballons.pop(n)
            return
def delete():
    for n in range(len(ballons)):      
        if ballons[n][1] >= (200+size):
            ballons.pop(n)
            return

def draw():
    clear()
    for n in range(1,len(ballons)+1):
        up()
        goto(ballons[-n][0],ballons[-n][1])
        dot(size, ballons[-n][3])
        ballons[-n][1] += ballons[-n][2]
    delete()
    update()

def gameLoop():
    if randrange(0,50)==1:
        x = randrange(-200+size, 200-size)
        step = randrange(5,15)/10
        c = choice(COLORS)
        ballons.append([x,-200-size,step,c])
    draw()
    ontimer(gameLoop, 10)

############主程序##############
setup(420, 420, 0, 0)
hideturtle()
tracer(False)
listen()
onscreenclick(tap)
gameLoop()
done()