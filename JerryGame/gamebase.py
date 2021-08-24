from turtle import *

def square(x, y, size, color_name):
    up()         #挂起海龟
    goto(x, y)
    down()      #放下海龟，目的是隐藏海龟移动路线
    color(color_name)
    begin_fill()
    
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    
    end_fill()
    
# setup(420,420,0,0)
# hideturtle()    #隐藏海龟身体
# tracer(False)    #隐藏海龟作画的过程
# square(50, 50, 10, 'red')
# done()
