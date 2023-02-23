import pygame

from constant import *

class Menu:

    def __init__(self, window):
        self.window = window
    
    def buttom_back_menu(self):
        '''
        Кнопка Возвращает на главную страницу меню
        '''
        surf = pygame.Surface((20, 40))
        surf.fill((255, 0, 0))
        rect = surf.get_rect()
        rect.topleft = 30, 30
        self.window.blit(surf, rect)
        return rect
    
    def show_start_game(self):
        '''
        Предлашает начать игру
        '''
        self.window.fill((0, 0, 0))
        self.buttom_back_menu()
        font = pygame.font.SysFont('arial', 30)
        text = font.render('Start Game', 1, (255, 0, 0))
        rect = text.get_rect()
        rect.center = W//2, H//4
        self.window.blit(text, rect)
        
        return rect
    
    def show_instruction(self):
        '''
        Предлагает просмотреть инструкцию
        '''
        font = pygame.font.SysFont('arial', 30)
        text = font.render('Show Instruction', 30, (255, 0, 0))
        rect = text.get_rect()
        rect.center = W//2, H//3
        self.window.blit(text, rect)
        return rect
    
    def instructions(self):
        '''
        Выводит инструкцию на экран
        '''
        self.window.fill((0, 0, 0))
        self.buttom_back_menu()
        text = '''Your goal is to destroy the enemies on your way
        You have 3 lives
        You can dodge enemies with the arrows on your keyboard
        When you press the spacebar you can shoot
        To pause press - q
        To return to the main menu, click in the upper left corner
        '''.splitlines()
        space_line = 0
        for line in text:
            font = pygame.font.SysFont('arial', 20)
            show = font.render(line, 1, (255, 0, 0))
            rect = show.get_rect()
            rect.center = W//2, H//3 + space_line
            self.window.blit(show, rect)
            space_line += 50
            
            
    
    def show_best_result(self):
        '''
        Предлагает просмотреть результаты
        '''
        ...
    
    def show_change_gun_model(self):
        '''
        Предлагает поменять модельку пушки
        '''
        ...