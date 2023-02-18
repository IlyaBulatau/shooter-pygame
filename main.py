import pygame

import sys

from constant import FPS, W, H
from gan import Gan
from mob import Mob
from manager import Maneger

window = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
bg = pygame.image.load('Gan/image/bmw.jpg')
rect = bg.get_rect()
rect.midtop = (W//2, 0)         

manager = Maneger()

gan_sprite = pygame.sprite.Group()
gan = Gan((50, 50))
gan_sprite.add(gan)

mobs_sprite = pygame.sprite.Group()
for _ in range(8):
    mob = Mob()
    mobs_sprite.add(mob)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        window.blit(bg, rect)
        gan_sprite.draw(window)
        mobs_sprite.draw(window)
        pygame.display.update()
        clock.tick(FPS)
        gan_sprite.update()
        mobs_sprite.update()
        manager.game_over(mobs_sprite, gan)

if __name__ == '__main__':
    main()
