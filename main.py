import pygame

import sys

from constant import FPS, W, H
from gan import Gan, Shell
from mob import Mob

# TODO - сделать разные цели за которые будут начилсятсься разщное колво очков
# TODO - сделать что бы задний фон двигался, что бы был эффект полета впред
class Manager:

    def __init__(self):
        self.window = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load('Gan/image/bmw.jpg')
        self.rect = self.bg.get_rect()
        self.rect.midtop = (W//2, 0)
        self.score = 0
    
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
        font = pygame.font.SysFont('arial', 28)
        show_text = font.render(f'Kill score {self.score}', 3, (0, 255, 0))
        rect_text = show_text.get_rect()
        rect_text.midleft = 30, 30
        self.window.blit(show_text, rect_text)
        pygame.display.flip()

    
    def game_over(self, mobs_sprite, gan):
        for mobs in mobs_sprite:
            if gan.rect.collidepoint(mobs.rect.center):
                sys.exit() # TODO - поменять функцию выхода на анимацию проигрыша или минус жизни

    def show(self): # TODO - сделать отображения жизни, меню с инструкцией и меню для начала игры 
        ...
    
    def run_game(self):
        self.init_window()
        self.init_sprite()
        self.show_score()
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

def run_game():
    manager.show_score()
    manager.init_window()
    manager.init_sprite()

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

