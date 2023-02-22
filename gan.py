import pygame
from constant import *


class Shell(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(path_to_image.joinpath('frame1.png'))
        self.rect = self.image.get_rect()
        self.rect.center = pos_x, pos_y
        self.speed = 30
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

class Gan(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path_to_image.joinpath('gun.jpg'))
        self.image.set_colorkey((0, 0, 0))
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
            
    def short(self, shell, shell_sprite):
        shell = Shell(self.rect.centerx, self.rect.bottom)
        shell_sprite.add(shell)
        
    def hitpoint(self): # TODO - сделать жизни
        ...

