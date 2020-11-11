import pygame, sys
from Classes import Player
pygame.init()
screen_width = 1300
screen_height = 900
pygame.display.set_caption("Platform Game")
pygame.display.set_mode((screen_width, screen_height))

screen = pygame.display.set_mode((800, 600))
Yours = Player(200, 200, 0, 0, 2, True)
ground = pygame.Rect(0, 570, 800, 30)
color = (255, 0, 0)
color2 = (0,120,0)
falling = False
count = 0

def jump(y, jumpcount):
    if jumpcount >= 0:
        y -= (jumpcount ** 2) * -0.5
        jumpcount -= 1

def fall(y, jumpcount):
        y -= jumpcount
        fall(y, jumpcount + 1)
