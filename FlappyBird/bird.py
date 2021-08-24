import pygame
from random import randrange
pygame.init()

##########定义变量######
map_width = 284
map_height = 512
frame = 0  #当前帧
FPS = 60   #屏幕刷新
pipes = [[200,4]]

gameScreen = pygame.display.set_mode((map_width, map_height))
clock = pygame.time.Clock()    #时间函数

background = pygame.image.load("FlappyBird\\images\\background.png")
bird_wing_up = pygame.image.load("FlappyBird\\images\\bird_wing_up.png")
bird_wing_down = pygame.image.load("FlappyBird\\images\\bird_wing_down.png")
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
    

def gameLoop():
    while True:
        gameScreen.blit(background,(0,0))
        draw_bird(20,map_height//2)  #整除2
        if len(pipes)<4:
            x = pipes[-1][0]+200
            open_pos = randrange(1,9)
            pipes.append([x,open_pos])
        if pipes[0][0]<-100:
            pipes.pop(0)
        draw_pipe()
        pygame.display.update()
        
        for event in pygame.event.get():   #获取用户的所有行动
            if event.type == pygame.QUIT:  #关闭按钮退出游戏
                pygame.quit()
                return  
        clock.tick(FPS)    #每秒60帧刷新屏幕
##########定义主程序##########
gameLoop()