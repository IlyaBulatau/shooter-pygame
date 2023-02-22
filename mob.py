import pygame
import random
from constant import W, H, path_to_image

class Mob(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path_to_image.joinpath('ship.png'))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0, W - self.rect[0]),
                             random.randint(-120, -60))
        self.speed = random.randint(5, 6)
    
    def update(self):
        if self.rect[1] < H:
            self.rect[1] += self.speed
        else:
            self.speed = random.randint(5, 6)
            self.rect[0] = random.randint(0, W - 20)
            self.rect[1] = random.randint(-120, -60)
        


