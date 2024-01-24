import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

BOARD_WIDTH = 1000
BOARD_HEIGHT = 1000


def main():
    pygame.init()

    is_running = 1
    screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    is_running = 0

        screen.fill((255, 255, 255))
        pygame.display.flip()


if __name__ == "__main__":
    main()
