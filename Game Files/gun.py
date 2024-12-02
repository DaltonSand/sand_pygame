import pygame
from man import Man
from math import cos, sin, pi


class Gun():
    def __init__ (self):
        self.surface = pygame.Surface((10,10))
        self.surface.fill((0,0,0))
    def shoot(self,x,y,angle, screen):
        self.x = x
        self.y = y
        self.angle = angle
        self.angle = -((self.angle/180)*(pi))
        self.x += (5*cos(self.angle))
        self.y += (5*sin(self.angle))
        screen.blit(self.surface, (self.x,self.y))
    def update(self, screen):
        self.x += (5*cos(self.angle))
        self.y += (5*sin(self.angle))
        screen.blit(self.surface, (self.x,self.y))
        self.rect = pygame.Rect(self.x,self.y,10,10)


class Reload():
    def __init__ (self, x,y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.shell = pygame.Surface((20,10))
        self.shell.fill((0,0,0))
    def fill(self):
        self.screen.blit(self.shell,(self.x,self.y))
    def box(self):
        self.upper_line = pygame.Surface((120,2))
        self.upper_line.fill((0,0,0))
        self.lower_line = pygame.Surface((120,2))
        self.lower_line.fill((0,0,0))
        self.right_line = pygame.Surface((2,12))
        self.right_line.fill((0,0,0))
        self.left_line = pygame.Surface((2,10))
        self.left_line.fill((0,0,0))

        self.screen.blit(self.upper_line, (20,50))
        self.screen.blit(self.lower_line, (20,60))
        self.screen.blit(self.right_line, (140,50))
        self.screen.blit(self.left_line, (20,50))

def reload(man,reload_num,shot_num,shot_max,screen,time):
    if shot_num <shot_max:
        reload_0 = Reload(20,30,screen)
        reload_0.box()
        if reload_num <10:
            man.reload(screen)
        if reload_num >time/6:
            reload_1 = Reload(20,50,screen)
            reload_1.fill()
        if reload_num >2*time/6:
            reload_2 = Reload(40,50,screen)
            reload_2.fill()
        if reload_num >3*time/6:
            reload_3 = Reload(60,50,screen)
            reload_3.fill()
        if reload_num >4*time/6:
            reload_4 = Reload(80,50,screen)
            reload_4.fill()
        if reload_num >5*time/6:
            reload_5 = Reload(100,50,screen)
            reload_5.fill()
        if reload_num >time:
            reload_6 = Reload(120,50,screen)
            reload_6.fill()
            man.reloading = False
            
            
            




