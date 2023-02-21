import pygame

import sys

from constant import FPS, W, H
from gan import Gan, Shell
from mob import Mob

# TODO - сделать разные цели за которые будут начилсятсься разщное колво очков
# TODO - сделать что бы задний фон двигался, что бы был эффект полета впред
# TODO - сделать наконец то главное меню
class Manager:

    def __init__(self):
        self.window = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load('Gan/image/bmw.jpg')
        self.rect = self.bg.get_rect()
        self.rect.midtop = (W//2, 0)
        self.score = 0
        self.hitpoint = 3
        self.mobs_sprite = pygame.sprite.Group()
    
    def up_mob(self):
        for _ in range(12):
            mob = Mob()
            mobs_sprite.add(mob)

    
    def init_window(self):
        self.window.blit(self.bg, self.rect)
        gan_sprite.draw(self.window)
        mobs_sprite.draw(self.window)
        shell_sprite.draw(self.window)
        
    def window_update(self):
        pygame.display.update()
        self.clock.tick(FPS)

        
    def init_sprite(self):
        gan_sprite.update()
        mobs_sprite.update()
        shell_sprite.update()
        self.game_over(mobs_sprite, gan)
        hits = pygame.sprite.groupcollide(mobs_sprite, shell_sprite, True, True)
        for hit in hits:
            self.score += 1
            m = Mob()
            mobs_sprite.add(m)
        return self.score
    
    def show_score(self):
        font = pygame.font.SysFont('arial', 18)
        show_text = font.render(f'Kill score {self.score}', 3, (0, 255, 0))
        rect_text = show_text.get_rect()
        rect_text.midleft = 30, 30
        self.window.blit(show_text, rect_text)

    
    def game_over(self, mobs_sprite, gan):
        hits = pygame.sprite.spritecollide(gan, mobs_sprite, True)
        for hit in hits:
            self.hitpoint -= 1
            if self.hitpoint < 1:
                sys.exit()
            mob = Mob()
            mobs_sprite.add(mob)
         

    def show_hitpoint(self): # TODO - сделать отображения жизни, меню с инструкцией и меню для начала игры 
        font = pygame.font.SysFont('arial', 18)
        show_text = font.render(f'You hitpoint {self.hitpoint}', 3, (0, 255, 0))
        rect_text = show_text.get_rect()
        rect_text.midleft = W-100, 30
        self.window.blit(show_text, rect_text)

    
    def run_game(self):
        self.init_window()
        self.init_sprite()
        self.show_score()
        self.show_hitpoint()
        self.window_update()

manager = Manager()

gan_sprite = pygame.sprite.Group()
gan = Gan((50, 50))
gan_sprite.add(gan)

mobs_sprite = pygame.sprite.Group()
for _ in range(12):
    mob = Mob()
    mobs_sprite.add(mob)
shell = Shell(gan.rect.centerx, gan.rect.bottom)
shell_sprite = pygame.sprite.Group()

pygame.init()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gan.short(shell, shell_sprite)
 

        manager.run_game()
            
if __name__ == '__main__':
    main()

