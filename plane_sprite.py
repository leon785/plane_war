"""
@project: plane_war
@author: Leon
@file: plane_sprite.py
@ide: PyCharm
"""


import pygame
import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 650)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackGround(GameSprite):
    """BG sprite"""
    def __init__(self, is_alt=False):
        super().__init__('./images/background.png')

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """enemy sprite"""
    def __init__(self):
        super().__init__('./images/enemy1.png')

        # set random speed
        self.speed = random.randint(1, 3)

        # set x and y
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        self.image = pygame.image.load('./images/enemy1_down1.png')
        self.image = pygame.image.load('./images/enemy1_down2.png')
        self.image = pygame.image.load('./images/enemy1_down3.png')
        self.image = pygame.image.load('./images/enemy1_down4.png')
        pygame.display.update()


class Hero(GameSprite):
    """hero sprite"""
    __flag = True

    def __init__(self):
        super().__init__('./images/me1.png', speed=0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()

    def update(self):

        if self.__flag:
            self.image = pygame.image.load('./images/me2.png')
            self.__flag = not self.__flag
        else:
            self.image = pygame.image.load('./images/me1.png')
            self.__flag = not self.__flag

        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        bullet = Bullet()

        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx

        self.bullets.add(bullet)

    def __del__(self):
        self.image = pygame.image.load('./images/me_destroy_1.png')
        self.image = pygame.image.load('./images/me_destroy_2.png')
        self.image = pygame.image.load('./images/me_destroy_3.png')
        self.image = pygame.image.load('./images/me_destroy_4.png')
        pygame.display.update()


class Bullet(GameSprite):
    """bullet sprite"""
    def __init__(self):
        super().__init__('./images/bullet1.png', speed=-2)

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        # print('bullet destroyed...')
        pass
