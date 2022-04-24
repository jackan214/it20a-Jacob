from turtle import color
import pygame as pg
import random as rand

pg.init()

posX = rand.randint(0,599)
posY = rand.randint(0,599)


color = (200, 0, 0)
while True :
    screen = pg.display.set_mode((600, 600))
    screen.fill(color)

    pg.draw.line(screen, color, (posX, 15), (posX, 600 - 15), 15)
    pg.display.update()
