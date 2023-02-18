import pygame
from constant import *

class Gan(pygame.sprite.Sprite):

    def __init__(self, size):
        super().__init__()
        self.size = size
        self.image = pygame.Surface((size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (W//2, H)
        self.speed = 15
        self.hp = 3
    
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect[0] -= self.speed
        elif keystate[pygame.K_RIGHT]:
            self.rect[0] += self.speed
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > W:
            self.rect.right = W
    
    def gamve_over(self):
        ...
        
    def short(self): # TODO - добавить возможность стрелять
        ...

class Shell(pygame.sprite.Sprite):
    
    def __init__(self, positions):
        super().__init__()
        self.image = pygame.Surface((10, 30))
        self.rect = self.image.get_rect()
        self.rect.center = positions
        self.speed = 30
    
    def update(self):
        if self.rect.bottom > 0:
            self.rect.x += self.speed
        else:
            ...
