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

    def update(self, keys, collided, img):
        if keys[K_UP]:
            if self.rect.colliderect(collided):
                self.rect.move_ip(0, 2)
            self.rect.move_ip(0, -1)

        if keys[K_DOWN]:
            if self.rect.colliderect(collided):
                self.rect.move_ip(0, -2)
            self.rect.move_ip(0, 1)

        if keys[K_LEFT]:
            if self.rect.colliderect(collided):
                self.rect.move_ip(2, 0)
            self.rect.move_ip(-1, 0)

        if keys[K_RIGHT]:
            if self.rect.colliderect(collided):
                self.rect.move_ip(-2, 0)
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= BOARD_WIDTH:
            self.rect.right = BOARD_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >= BOARD_HEIGHT:
            self.rect.bottom = BOARD_HEIGHT


def main():
    pygame.init()

    is_running = 1
    screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    player = Player()
    wall = Wall(500, 500)
    walls = pygame.sprite.Group()
    walls.add(wall)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(wall)
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    is_running = 0

        screen.fill((255, 255, 255))
        for sprite in all_sprites:
            screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
