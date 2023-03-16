from grid import Grid
import pygame
from sys import exit

# pygame setup stuff
pygame.init()
srn = pygame.display.set_mode((1600, 900))
pygame.display.set_caption('LandMineLottery')
clock = pygame.time.Clock()

#surface for the bomb, a red square basically
bomb_surface = pygame.Surface((50,50))
bomb_surface.fill('Red')

# grid setup stuff
x = Grid(10, 10)

while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()

        srn.blit(bomb_surface, (200 , 100))
        pygame.display.update()
        clock.tick(30)