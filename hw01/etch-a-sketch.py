#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500))

x = 250
y = 250

clock = pygame.time.Clock()
screen.fill((255,255,255))

while 1:
    clock.tick(60)
    pygame.draw.circle(screen, (0,0,0), (x,y), 2)
    pygame.display.update()
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]: x+=1
    if key[pygame.K_LEFT]: x-=1
    if key[pygame.K_UP]: y-=1
    if key[pygame.K_DOWN]: y+=1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill((255, 255, 255))
