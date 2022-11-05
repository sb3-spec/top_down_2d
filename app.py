import pygame
import sys

from settings import *



def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Top Down Kingdom Game")
    clock = pygame.time.Clock()
    
      
    
    while True:
        # main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()