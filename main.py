import pygame
from pygame.locals import K_ESCAPE, KEYDOWN
from models import Player, Wall


BOARD_WIDTH = 1000
BOARD_HEIGHT = 1000


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
    count = 0
    images = ["move_1.png", "move_2.png", "move_3.png"]
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    is_running = 0

        if count >= 3:
            count = 0
            player.set_surf_default()
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys, wall, images[count], BOARD_WIDTH,BOARD_HEIGHT)
        count += 1
        screen.fill((255, 255, 255))
        for sprite in all_sprites:
            screen.blit(sprite.surf, sprite.rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
