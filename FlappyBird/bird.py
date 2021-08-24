import pygame
from random import randrange
from time import sleep
pygame.init()

##########定义变量######
map_width = 284
map_height = 512
frame = 0  #当前帧
FPS = 60   #屏幕刷新
pipes = [[200,4]]
bird = [40,map_height//2-50]
gravity = 0.2
velocity = 0  #小鸟当前速度

gameScreen = pygame.display.set_mode((map_width, map_height))
clock = pygame.time.Clock()    #时间函数

background = pygame.image.load("FlappyBird\\images\\background.png")
bird_wing_up = bird_wing_up_copy = pygame.image.load("FlappyBird\\images\\bird_wing_up.png")
bird_wing_down = bird_wing_down_copy = pygame.image.load("FlappyBird\\images\\bird_wing_down.png")
pipe_body = pygame.image.load("FlappyBird\\images\\pipe_body.png")
pipe_end = pygame.image.load("FlappyBird\\images\\pipe_end.png")
#############定义函数#############
def draw_pipe():
    global pipes
    for n in range(len(pipes)):
        for m in range(pipes[n][1]):
            gameScreen.blit(pipe_body, (pipes[n][0],m*32))
        for m in range(pipes[n][1]+6,16):
            gameScreen.blit(pipe_body, (pipes[n][0],m*32))
        gameScreen.blit(pipe_end, (pipes[n][0],(pipes[n][1]*32)))
        gameScreen.blit(pipe_end, (pipes[n][0],((pipes[n][1]+5)*32)))
        pipes[n][0] -= 1

def draw_bird(x,y):      #前30帧显示小鸟翅膀向上，后30帧翅膀向下
    global frame
    if 0<=frame<=30:
        gameScreen.blit(bird_wing_up, (x,y))
        frame += 1
    elif 30<frame<=60:
        gameScreen.blit(bird_wing_down, (x,y))
        frame += 1
        if frame==60: frame=0

def safe():
    if bird[1] > map_height-35:
        print("hit floor")
        return False
    if bird[1] < 30:
        print("hit ceiling")
        return False
    if pipes[0][0]-30 < bird[0] < pipes[0][0]+79:
        if bird[1]<(pipes[0][1]+1)*32 or bird[1]>(pipes[0][1]+4)*32:
            print("hit pipe")
            return False
    return True

def reset():
    global frame, map_width, map_height, FPS, pipes, bird, gravity, velocity
    map_width = 284
    map_height = 512
    frame = 0  #当前帧
    FPS = 60   #屏幕刷新
    pipes = [[200,4]]
    bird = [40,map_height//2-50]
    gravity = 0.2
    velocity = 0  #小鸟当前速度

def gameLoop():
    global bird,velocity,gravity,bird_wing_down,bird_wing_up
    while True:      
        if len(pipes)<4:     #自动生成管子
            x = pipes[-1][0]+200
            open_pos = randrange(1,9)
            pipes.append([x,open_pos]) 
        if pipes[0][0]<-100:   #删除多于管子
            pipes.pop(0)
        
        
        for event in pygame.event.get():   #获取用户的所有行动
            if event.type == pygame.MOUSEBUTTONDOWN:    #控制小鸟向上移动
                bird[1] -= 40
                velocity = -3.5
            if event.type == pygame.QUIT:  #关闭按钮退出游戏
                pygame.quit()
                return  
            
        velocity += gravity
        bird[1] += velocity
        bird_wing_down = pygame.transform.rotate(bird_wing_down_copy, -90*(velocity/15))
        bird_wing_up = pygame.transform.rotate(bird_wing_up_copy, -90*(velocity/15))
        gameScreen.blit(background,(0,0))
        draw_pipe()
        draw_bird(bird[0],bird[1])
        pygame.display.update()
        if not safe():
            sleep(3)
            reset()
        clock.tick(FPS)    #每秒60帧刷新屏幕
##########定义主程序##########
gameLoop()