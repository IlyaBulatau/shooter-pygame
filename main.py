import pygame
import random
import sys
import time
from constant import FPS, W, H, path_to_image
from gan import Gan, Shell
from mob import Mob
from menu import Menu

# TODO - сделать уровни
#TODO - добавить кнопку во время игры для выхода в главное меню
#TODO - рендеринг
#TODO - сделать шрифты отдельной константой
class Manager:
    '''
    Класс отвечающий за процесс игры
    '''
    def __init__(self):
        self.window = pygame.display.set_mode((W, H))  # окно игры
        self.clock = pygame.time.Clock() # таймер для фпс
        self.image = pygame.image.load(path_to_image.joinpath('kosmos.jpg')) # 1 половина фона
        self.rect = self.image.get_rect()
        self.rect.center = W//2, H//2
        self.img2 = pygame.image.load(path_to_image.joinpath('kosmos2.jpg')) # 2 половина фона
        self.rect2 = self.img2.get_rect()
        self.rect2.center = W//2, 0 - H//2
        self.score = 0 # счет убийств
        self.hitpoint = 3 # жизни
        self.game_state = 'main' # состояние игры
        self.timer = pygame.time.get_ticks() # таймер отслеживания времени для увеличения скорости мобов
    
    def up_speed_mobs(self, x, y):
        '''
        Увеличивает скорость мобов в пределах от х до у
        '''
        for mob in mobs_sprite:
            mob.speed = random.randint(x, y)


    def game_timer(self):
        #TODO - сделать таймер времязависимым и отображать его во время игры
        '''
        Функция увеличивает скорость мобов со временем игры
        '''
        
        self.timer += 1
        if 500 < self.timer < 900:
           self.up_speed_mobs(11, 14)
        elif 900 < self.timer < 1300:
            self.up_speed_mobs(13, 16)
        elif 1300 < self.timer < 1600:
            self.up_speed_mobs(15, 19)
        elif 1600 < self.timer < 2000:
            self.up_speed_mobs(18, 22)
        elif 2000 < self.timer:
            self.up_speed_mobs(21, 25)
        return self.timer
    
    def show_timer(self):
        font = pygame.font.SysFont('arial', 18)
        text = font.render(f'Game Time - {round(self.timer//30-4)}', 1, (0, 255, 0))
        rect = text.get_rect()
        rect.center = W//2, 30
        self.window.blit(text, rect)
        
    def game_cycle(self):
        '''
        цикл отслеживающий события
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gan.short(shell, shell_sprite)
                elif event.key == pygame.K_q and self.game_state != 'pause' and self.game_state != 'main':
                    self.game_state = 'pause'
                elif event.key == pygame.K_q and self.game_state != 'run' and self.game_state != 'main':
                    self.game_state = 'run'

            elif event.type == pygame.MOUSEBUTTONDOWN and self.game_state != 'run':
                if menu.show_start_game().collidepoint(event.pos) and self.game_state != 'instruction' and self.game_state != 'change-model':
                    self.game_state = 'run'
                elif menu.buttom_back_menu().collidepoint(event.pos):
                    self.game_state = 'main' 
                elif menu.show_instruction().collidepoint(event.pos) and self.game_state != 'change-model':
                    self.game_state = 'instruction'
                elif menu.show_change_gun_model().collidepoint(event.pos) and self.game_state != 'instruction':
                    self.game_state = 'change-model'
                self.model_gun(event)  
                                
    def model_gun(self, event):
        '''
        Отвечает за выбор модели пушки при нажатии мышкой по ней
        '''
        if menu.change_model()[0].collidepoint(event.pos) and self.game_state == 'change-model':
            gan.first_model()

        elif menu.change_model()[1].collidepoint(event.pos) and self.game_state == 'change-model':
            gan.second_model()     

        elif menu.change_model()[2].collidepoint(event.pos) and self.game_state == 'change-model':
            gan.third_model()     

        elif menu.change_model()[3].collidepoint(event.pos) and self.game_state == 'change-model':
            gan.fourth_model()     


    def game_pause(self):
        '''
        отображения паузы в игре
        '''
        surf = pygame.Surface((W, H))
        surf.fill((127, 127, 127))
        surf.set_alpha(3)
        font = pygame.font.SysFont('arial', 44)
        text = font.render('Pause', True, (255, 0, 0))
        rect = text.get_rect()
        rect.center = W//2, H//2
        self.window.blit(surf, (0, 0))
        self.window.blit(text, rect)
        pygame.display.flip()
    
    def bg_run(self):
        '''
        Передвижение фона 
        '''
        self.rect.bottom += 8
        self.rect2.bottom += 8
        if self.rect.top > H:
            self.rect.center = W//2, 0 - H//2
        if self.rect2.top > H:
             self.rect2.center = W//2, 0 - H//2
         
    def window_init(self):
        self.window.blit(self.image, self.rect)
        self.window.blit(self.img2, self.rect2)
        gan_sprite.draw(self.window)
        mobs_sprite.draw(self.window)
        shell_sprite.draw(self.window)
        
    def window_update(self):
        pygame.display.update()
        self.clock.tick(FPS)
        
    def init_sprite(self):
        '''
        Отслеживает убийства мобов
        '''
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
        '''
        Отслеживает столкновение мобов с пушкой
        '''
        hits = pygame.sprite.spritecollide(gan, mobs_sprite, True)
        for hit in hits:
            self.hitpoint -= 1
            if self.hitpoint < 1:
                self.game_state = 'stop'
            mob = Mob()
            mobs_sprite.add(mob)         

    def show_hitpoint(self):
        font = pygame.font.SysFont('arial', 18)
        show_text = font.render(f'You hitpoint {self.hitpoint}', 3, (0, 255, 0))
        rect_text = show_text.get_rect()
        rect_text.midleft = W-100, 30
        self.window.blit(show_text, rect_text)

    
    def run_game(self):
        if self.game_state == 'run':
            self.game_timer()
            self.game_cycle()
            self.window_init()
            self.init_sprite()
            self.bg_run()
            self.show_score()
            self.show_hitpoint()
            self.show_timer()
            self.window_update()
        elif self.game_state == 'pause':
            self.game_cycle()
            self.game_pause()
        elif self.game_state == 'main':
            self.game_cycle()
            menu.show_start_game()
            menu.show_instruction()
            menu.show_change_gun_model()
            self.window_update()
        elif self.game_state == 'instruction':
            self.game_cycle()
            menu.instructions()
            self.window_update()
        elif self.game_state == 'change-model':
            self.game_cycle()
            menu.change_model()
            self.window_update()
        elif self.game_state == 'stop': # если игра закончилась
            self.game_state = 'main' # статус игры изменяется для отправки на главное меню
            self.score = 0 # счет становиться 0
            self.hitpoint = 3 # обновляется ХП
            self.timer = 120 # обнуляеться таймер
            for mob in mobs_sprite: # обновляется позиция мобов
                mob.rect.topleft = (random.randint(0, W - 40),
                                 random.randint(-120, -60))
            self.up_speed_mobs(9, 12) # при запуске новой игры если отсались мобы с прошлой их скорость скидывается

            



manager = Manager()

gan_sprite = pygame.sprite.Group()
gan = Gan()
gan_sprite.add(gan)

mobs_sprite = pygame.sprite.Group()
for _ in range(12):
    mob = Mob()
    mobs_sprite.add(mob)
shell = Shell(gan.rect.centerx, gan.rect.bottom)
shell_sprite = pygame.sprite.Group()
menu = Menu(manager.window)

pygame.init()

def main():
    while True:
     manager.run_game()
            
if __name__ == '__main__':
    main()
