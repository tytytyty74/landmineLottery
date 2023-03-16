from grid import Grid
import pygame
from sys import exit


pygame.int()
srn = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('LandMineLottery')
clock = pygame.time.Clock()
x = Grid(10, 10)

bomb_surface = pygame.Surface((50,50))
bomb_surface.fill('Red')

while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

        srn.blit(bomb_surface, (200 , 100))
        pygame.display.update()
        clock.tick(30)