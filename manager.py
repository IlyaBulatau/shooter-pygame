import pygame 

import sys

from mob import Mob
from gan import Gan

class Maneger:

    def __init__(self):
        self
    
    def game_over(self, mobs_sprite, gan):
        for mobs in mobs_sprite:
            if gan.rect.collidepoint(mobs.rect.center):
                sys.exit() # TODO - поменять функцию выхода на анимацию проигрыша или минус жизни
