import pygame, sys
from pygame.locals import *

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Pygame Title")

def close():
    sys.exit()
    pygame.quit()

while True:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
               close()