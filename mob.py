import pygame

import random

from constant import W, H, path_to_image

class Mob(pygame.sprite.Sprite):
    '''
    Класс мобов-противников
    '''
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path_to_image.joinpath('ship.png'))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, W - 40),
                             random.randint(-120, -60))
        self.speed = random.randint(9, 12)
        self.shell = pygame.Surface((10, 25))
        self.shell.fill((255, 255, 0))
        self.rect_shell = self.shell.get_rect()
        self.rect_shell.topleft = self.rect.bottomleft
    
    def update(self):
        if self.rect[1] < H:
            self.rect[1] += self.speed
        else:
            self.speed = random.randint(9, 12)
            self.rect[0] = random.randint(0, W - 40)
            self.rect[1] = random.randint(-120, -60)
    
    def shooting(self, window):
        if self.rect[1] < H-200:
            self.update_shell()
            window.blit(self.shell, self.rect_shell)
    
    def update_shell(self):
        if self.rect_shell[1] < H:
            self.rect_shell.y += 12
        else:
            self.rect_shell.topleft = self.rect.bottomleft
    
    


