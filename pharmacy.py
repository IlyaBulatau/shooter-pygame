import pygame

from constant import W, H

import random

class Pharma(pygame.sprite.Sprite):
    '''
    Класс аптечки
    '''

    def __init__(self):
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 123))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, W-30),
                            random.randint(-2000, -1300))
        self.speed = 15

    def update(self):
        if self.rect.y < H:
            self.rect.centery += self.speed
        else:
            self.rect.center = (random.randint(100, W-100),
                                random.randint(-2000, -1300))