#!/usr/bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode((width, height))

x = width/2
y = height/2

clock = pygame.time.Clock()
screen.fill((255,255,255))

speed = 10

while 1:
    clock.tick(60)
    pygame.draw.circle(screen, (0,0,0), (x,y), 2)
    pygame.display.update()
    key = pygame.key.get_pressed()

    # Moving Cursor
    if key[pygame.K_RIGHT]: x+=(speed/10)
    if key[pygame.K_LEFT]: x-=(speed/10)
    if key[pygame.K_UP]: y-=(speed/10)
    if key[pygame.K_DOWN]: y+=(speed/10)

    # Speed Change
    if key[pygame.K_w]: speed-=1
    if key[pygame.K_s]: speed+=1
    
    # Speed Check
    if speed > 100:
        speed = 100
    elif speed < 10:
        speed = 10

    # Overlap
    if x > width:
        x = 0
    if x < 0:
        x = width
    if y > height:
        y = 0
    if y < 0:
        y = height
    
    # Special Keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill((255, 255, 255))
