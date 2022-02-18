import pygame
from plane_sprite import *

pygame.init()

screen = pygame.display.set_mode((480, 650))

# initialize the game
bg = pygame.image.load('./images/background.png')
screen.blit(bg, (0, 0))

hero = pygame.image.load('./images/me1.png')
screen.blit(hero, (150, 300))

pygame.display.update()

# set clock
clock = pygame.time.Clock()

# set hero rect
hero_rect = pygame.Rect(150, 300, 102, 126)

# create sprites
enemy = GameSprite('./images/enemy1.png')
enemy1 = GameSprite('./images/enemy1.png', speed=2)

# create sprite group
enemy_group = pygame.sprite.Group(enemy, enemy1)

while True:
    clock.tick(60)
    hero_rect.y -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if hero_rect.y <= -126:
        hero_rect.y = 650

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()

pygame.quit()


