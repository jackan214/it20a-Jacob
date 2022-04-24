import pygame
import time
import random

pygame.init() 
diswidth = 1000
dis=pygame.display.set_mode((diswidth, diswidth)) 


pygame.display.set_caption('Snake')

blue=(0,150,255) 
red=(255,0,0) 

width = 20 
height = 20

ychange = 0
xchange = 0

font = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [150, diswidth/2])

clock = pygame.time.Clock()

def gameLoop():
    game_over = False
    game_close = False

    x = 200
    y = 200

    x += xchange    
    y += ychange

    applex = round(random.randrange(0, diswidth - snake_block) / 10.0) * 10.0
    appley = round(random.randrange(0, diswidth - snake_block) / 10.0) * 10.0

    game_over=False
    while not game_over :
            for event in pygame.event.get():
                keys = pygame.key.get_pressed() 
                if event.type==pygame.QUIT:
                    game_over=True
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_LEFT] and x>0:
                        xchange = -10
                        ychange = 0
                    elif keys[pygame.K_UP] and y>0:
                        ychange = -10
                        xchange = 0
                    elif keys[pygame.K_DOWN] and y>0:
                        ychange = 10
                        xchange = 0
                    elif keys[pygame.K_RIGHT] and y>0:
                        xchange = 10
                        ychange = 0


            if x >= diswidth or x < 0 or y >= diswidth or y < 0:
                game_over = True

           
            dis.fill((blue))
            square1 = pygame.draw.rect(dis,red,[x,y,width,height])
            pygame.display.update()
            clock.tick(30)

message("YOU FUCKING SUCK HAHAHAHAHHHAHAH",red)
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()