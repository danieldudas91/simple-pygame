import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((50, 20))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.centerx = x
        self.rect.centery = y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("space_soldier.png").convert()
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect()

    def set_surf_default(self):
        self.surf = pygame.image.load("space_soldier.png").convert()
        self.surf.set_colorkey((0, 0, 0))

    def set_surf_image(self, img):
        self.surf = pygame.image.load(img).convert()
        self.surf.set_colorkey((0, 0, 0))

    def update(self, keys, collided, img, board_width, board_height):

        if keys[K_UP]:
            if self.rect.colliderect(collided):
                self.rect.move_ip(0, 2)
            self.set_surf_image(img)
            self.rect.move_ip(0, -1)

        if keys[K_DOWN]:
            if self.rect.colliderect(collided):
                self.rect.move_ip(0, -2)
            self.set_surf_image(img)
            self.rect.move_ip(0, 1)

        if keys[K_LEFT]:
            if self.rect.colliderect(collided):
                self.rect.move_ip(2, 0)
            self.set_surf_image(img)
            self.rect.move_ip(-1, 0)

        if keys[K_RIGHT]:
            if self.rect.colliderect(collided):
                self.rect.move_ip(-2, 0)
            self.set_surf_image(img)
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >= board_width:
            self.rect.right = board_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >= board_height:
            self.rect.bottom = board_height
