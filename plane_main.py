"""
@project: plane_war
@author: Leon
@file: plane_main.py
@ide: PyCharm
"""


import pygame
from plane_sprite import *
pygame.init()


class PlaneGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)

    def __create_sprites(self):

        # background sprites
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        while True:
            # 1. set refresh frequency
            self.clock.tick(FRAME_PER_SEC)
            # 2. set event listener
            self.__event_handler()
            # 3. collision detection
            self.__check_collide()
            # 4. update sprites group
            self.__update_sprites()
            # 5. show the updates
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 4
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -4
        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()