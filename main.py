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


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((50, 20))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        # self.rect.x = BOARD_WIDTH / 2
        # self.rect.y = BOARD_WIDTH / 2
        self.rect.centerx = x
        self.rect.centery = y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("space_soldier.png").convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()


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
