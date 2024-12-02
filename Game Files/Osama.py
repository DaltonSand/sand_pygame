import pygame
from gun import Gun
from math import atan2, pi, degrees
from badguy import Badguy
clock = pygame.time.Clock()

class Osama(Badguy):
    def __init__ (self,x,y):
        self.y = y
        self.x = x