import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([400,300])
pygame.display.set_caption("Mickey")
bg = pygame.image.load("mickyimage.png")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg,[0,0])
    pygame.display.flip()