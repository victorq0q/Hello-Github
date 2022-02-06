import time
import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

while 1:
    time.sleep(3)
    screen = pygame.display.set_mode(size)

