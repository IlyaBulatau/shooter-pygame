import pygame

import random
import sys

from constant import FPS, W, H, path_to_image
from gan import Gan, Shell
from mob import Mob
from menu import Menu

#TODO
# - первый уровень обычная игра
# - второй меньше мобов, добавить мобов которые могут стрелять добавить аптечку  
#TODO - рендеринг


pygame.init()
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
        self.font = pygame.font.SysFont('arial', 18)
        self.level = 2
        

    def show_menu_exit_button(self):
        '''
        Отображает кнопку для выхода в главное меню из игры
        '''
        surf = pygame.Surface((50, 50))
        surf.fill((127, 127, 127))
        surf.set_alpha(150)
        rect = surf.get_rect()
        rect.bottomleft = 30, H - 20
        self.window.blit(surf, rect)
        return rect

    def up_speed_mobs(self, x, y):
        '''
        Увеличивает скорость мобов в пределах от х до у
        '''
        for mob in mobs_sprite:
            mob.speed = random.randint(x, y)

    def game_timer(self):
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
        font = self.font
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
            # события мыши не во время игры
            elif event.type == pygame.MOUSEBUTTONDOWN and self.game_state != 'run' and self.game_state != 'pause':
                if menu.show_start_game().collidepoint(event.pos) and self.game_state != 'instruction' and self.game_state != 'change-model':
                    self.game_state = 'run'
                elif menu.buttom_back_menu().collidepoint(event.pos):
                    self.game_state = 'main' 
                elif menu.show_instruction().collidepoint(event.pos) and self.game_state != 'change-model' and self.game_state != 'level-select':
                    self.game_state = 'instruction'
                elif menu.show_change_gun_model().collidepoint(event.pos) and self.game_state != 'instruction' and self.game_state != 'level-select':
                    self.game_state = 'change-model'
                elif menu.show_level_select().collidepoint(event.pos) and self.game_state != 'change-model' and self.game_state != 'instruction':
                    self.game_state = 'level-select'
                self.model_gun(event)
                self.choose_level(event)  
            # события мыши во время игры
            elif event.type == pygame.MOUSEBUTTONDOWN and self.game_state == 'run' and self.show_menu_exit_button().collidepoint(event.pos):
                    self.game_state = 'stop'
    
    def choose_level(self, event):
        '''
        Отвечает за выбор уровня при нажатии мышкой
        '''
        if menu.level_selected()[0].collidepoint(event.pos) and self.game_state == 'level-select':
            self.level = 1
        elif menu.level_selected()[1].collidepoint(event.pos) and self.game_state == 'level-select':
            self.level = 2
        elif menu.level_selected()[2].collidepoint(event.pos) and self.game_state == 'level-select':
            self.level = 3
        elif menu.level_selected()[3].collidepoint(event.pos) and self.game_state == 'level-select':
            self.level = 4
                                
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
        '''
        Функция рисует все обьекты во время игры когда game_state = run
        '''
        self.window.blit(self.image, self.rect)
        self.window.blit(self.img2, self.rect2)
        gan_sprite.draw(self.window)
        mobs_sprite.draw(self.window)
        shell_sprite.draw(self.window)
        self.show_menu_exit_button()
        self.show_score()
        self.show_hitpoint()
        self.show_timer()

        
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
        font = self.font
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
        font = self.font
        show_text = font.render(f'You hitpoint {self.hitpoint}', 3, (0, 255, 0))
        rect_text = show_text.get_rect()
        rect_text.midleft = W-100, 30
        self.window.blit(show_text, rect_text)
    
    def new_game(self):
        '''
        Функция обновляет все характеристики для новой игры(скорость мобов, их появления, HP, счетчик киллов, и время)
        '''
        self.game_state = 'main' # статус игры изменяется для отправки на главное меню
        self.score = 0 # счет становиться 0
        self.hitpoint = 3 # обновляется ХП
        self.timer = 120 # обнуляеться таймер
        for mob in mobs_sprite: # обновляется позиция мобов
            mob.rect.topleft = (random.randint(0, W - 40),
                                 random.randint(-120, -60))
        self.up_speed_mobs(9, 12) # при запуске новой игры если отсались мобы с прошлой их скорость скидывается
    
    def run_game(self):
        if self.game_state == 'run':
            if self.level == 1:
                self.game_timer()
                self.game_cycle()
                self.window_init()
                self.init_sprite()
                self.bg_run()
                self.window_update()
            elif self.level == 2:
                leve2.game_timer()
                leve2.hit_the_mobs_shell_in_gan()
                self.game_cycle()
                leve2.window_init()
                leve2.create_mobs_shell()
                self.init_sprite()
                self.bg_run()
                self.window_update()
            elif self.level == 3:
                ...
            elif self.level == 4:
                ...
        elif self.game_state == 'pause':
            self.game_cycle()
            self.game_pause()
        elif self.game_state == 'main':
            self.game_cycle()
            menu.show_start_game()
            menu.show_instruction()
            menu.show_change_gun_model()
            menu.show_level_select()
            self.window_update()
        elif self.game_state == 'instruction':
            self.game_cycle()
            menu.instructions()
            self.window_update()
        elif self.game_state == 'change-model':
            self.game_cycle()
            menu.change_model()
            self.window_update()
        elif self.game_state == 'level-select':
            self.game_cycle()
            menu.level_selected()
            self.window_update()
        elif self.game_state == 'stop': # если игра закончилась
            self.new_game()


class LevelTwo():

    def __init__(self):
        self.image = pygame.image.load(path_to_image.joinpath('shiplevel2.png')) 


    def new_image(self):
        '''
        Меняет картинку мобов
        '''
        for mob in mobs_sprite:
            mob.image = self.image
            
    def create_mobs_shell(self):
        '''
        Рисует пули мобов
        '''
        for mob in mobs_sprite:
            mob.shooting(manager.window)

    def hit_the_mobs_shell_in_gan(self):
        '''
        Отслеживает попадания пулей мобов в пушку и отнимает жизнь если это произошло
        '''
        for mob in mobs_sprite:
            if gan.rect.collidepoint(mob.rect_shell.center):
                mob.rect_shell.topleft = mob.rect.bottomleft
                manager.hitpoint -= 1
            if manager.hitpoint < 1:
                manager.game_state = 'stop'

    def window_init(self):
        '''
        Функция рисует все обьекты во время игры когда game_state = run
        '''
        manager.window.blit(manager.image, manager.rect)
        manager.window.blit(manager.img2, manager.rect2)
        gan_sprite.draw(manager.window)
        self.new_image()
        mobs_sprite.draw(manager.window)
        shell_sprite.draw(manager.window)
        manager.show_menu_exit_button()
        manager.show_score()
        manager.show_hitpoint()
        manager.show_timer()

    def up_speed_mobs(self, x, y):
        '''
        Увеличивает скорость мобов в пределах от х до у
        '''
        for mob in mobs_sprite:
            mob.speed = random.randint(x, y)

    def mobs_move(self):
        # TODO - сделать что бы мобы двигались по х оси
        for mob in mobs_sprite:
            if 0 < mob.rect.y < H:
                mob.rect.x += random.randint(-2, 2)
        

    def game_timer(self):
        '''
        Функция увеличивает скорость мобов со временем игры
        '''
        manager.timer += 1
        if manager.timer < 500:
            self.up_speed_mobs(5, 6)
        elif 500 < manager.timer < 900:
           self.up_speed_mobs(7, 8)
        elif 900 < manager.timer < 1300:
            self.up_speed_mobs(9, 12)
        elif 1300 < manager.timer < 1600:
            self.up_speed_mobs(13, 15)
        elif 1600 < manager.timer < 2000:
            self.up_speed_mobs(16, 19)
        elif 2000 < manager.timer:
            self.up_speed_mobs(20, 23)
        return manager.timer


manager = Manager()

gan_sprite = pygame.sprite.Group()
gan = Gan()
gan_sprite.add(gan)

mobs_sprite = pygame.sprite.Group()

for _ in range(8):
    mob = Mob()
    mobs_sprite.add(mob)


shell = Shell(gan.rect.centerx, gan.rect.bottom)
shell_sprite = pygame.sprite.Group()

menu = Menu(manager.window)
leve2 = LevelTwo()

def main():

    while True:
        manager.run_game()
            
if __name__ == '__main__':
    main()
