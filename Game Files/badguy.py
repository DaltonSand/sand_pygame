import pygame
from gun import Gun
from math import atan2, pi, degrees
clock = pygame.time.Clock()

flag = 0
class BadGuy():
    #initilize bad guy 
    def __init__ (self,x,y,level=1):
        self.x = x
        self.cx = x
        self.y = y
        self.cy = y
        #set time for rove_rev
        self.time_x = x
        self.time_y = y
        self.double_tap_timer = 0
        #set level for more intense looking bad guy
        self.level = level
        #set basic atributes
        self.angle = 0
        self.shot_flag = 0
        self.time = 0
        self.dead = 0
        self.roving = 0
        #higher level = cooler skin (set image/rect)
        if self.level == 1:
            self.image = pygame.image.load('PNG/Soldier 1/soldier1_machine.png')
        elif self.level == 2:
            self.image = pygame.image.load('PNG/Robot 1/robot1_gun.png')
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = pygame.Rect(self.x,self.y,(self.w),(self.h))

    def rove(self, max_x,max_y):
        #set a time variable to control movement
        self.time += 1
        if self.level ==1:
            speed = 0.8
        if self.level ==2:
            speed = 1.4
        self.max_x = max_x
        self.max_y = max_y
        self.vision_x = -100
        self.vision_y = -100
        if self.roving == 0:
            if self.dead ==0:
                if self.time < (self.max_x-self.cx):
                    self.x += speed
                    self.angle = 0
                    if self.level ==1:
                        self.vision_x = (self.rect.centerx)
                        self.vision_y = (self.rect.centery-50)
                    if self.level ==2:
                        self.vision_x = (self.rect.centerx)
                        self.vision_y = (self.rect.centery-88)

                elif self.time < ((self.max_x-self.cx)+(self.max_y-self.cy)):
                    self.y += speed
                    self.angle = 270
                    if self.level ==1:
                        self.vision_x = (self.rect.centerx-50)
                        self.vision_y = (self.rect.centery)
                    if self.level ==2:
                        self.vision_x = (self.rect.centerx-88)
                        self.vision_y = (self.rect.centery)
                elif self.time < ((self.max_x-self.cx)+(self.max_y-self.cy))+ (self.max_x-self.cx):
                    self.x -= speed
                    self.angle = 180
                    if self.level ==1:
                        self.vision_x = (self.rect.centerx-100)
                        self.vision_y = (self.rect.centery-50)
                    if self.level ==2:
                        self.vision_x = (self.rect.centerx-175)
                        self.vision_y = (self.rect.centery-88)
                elif self.time < (((self.max_x-self.cx)+(self.max_y-self.cy))+ (self.max_x-self.cx))+(self.max_y-self.cy):
                    self.y -= speed
                    self.angle = 90
                    if self.level ==1:
                        self.vision_x = (self.rect.centerx-50)
                        self.vision_y = (self.rect.centery-100)
                    if self.level ==2:
                        self.vision_x = (self.rect.centerx-88)
                        self.vision_y = (self.rect.centery-175)
                else:
                    self.time = 0
                self.rect = pygame.Rect(self.x,self.y,(self.w),(self.h)) 
            else:
                self.rect = pygame.Rect(-50,-50,(self.w),(self.h))
        else:
            self.rect = pygame.Rect(self.x,self.y,(self.w),(self.h))


        if self.level == 1:
            self.vision = pygame.Surface((100,100))
            self.vision.fill((0,0,0))
            self.vision_rect = pygame.Rect(self.vision_x,self.vision_y,(100),(100))
        if self.level == 2:
            self.vision = pygame.Surface((175,175))
            self.vision.fill((0,0,0))
            self.vision_rect = pygame.Rect(self.vision_x,self.vision_y,(175),(175))

    def rove_rev (self, min_x,max_y):
        #set a time variable to control movement
        self.time_x += 1
        self.time_y += 1
        speed = 1.4
        self.min_x = min_x
        self.max_y = max_y
        self.vision_x = -100
        self.vision_y = -100
        if self.roving == 0:
            if self.dead == 0:
                if self.time_x < (self.min_x+self.cx):
                    self.x -= speed
                    self.angle = 180
                    if self.level == 1:
                        self.vision_x = (self.rect.centerx-100)
                        self.vision_y = (self.rect.centery-50)
                    if self.level ==2:
                        self.vision_x = (self.rect.centerx-175)
                        self.vision_y = (self.rect.centery-88)
                    self.time_y = 0
                elif self.time_y < (self.max_y-self.cy):
                    self.y += speed
                    self.angle = 270
                    if self.level == 1:
                        self.vision_x = (self.rect.centerx-50)
                        self.vision_y = (self.rect.centery)
                    if self.level == 2:
                        self.vision_x = (self.rect.centerx-88)
                        self.vision_y = (self.rect.centery)
                    self.time_x = 1000+self.cx
                elif self.time_x <(self.cx +self.min_x+1000):
                    self.x += speed
                    self.angle = 0
                    if self.level == 1:
                        self.vision_x = (self.rect.centerx)
                        self.vision_y = (self.rect.centery-50)
                    if self.level == 2:
                        self.vision_x = (self.rect.centerx)
                        self.vision_y = (self.rect.centery-88)
                    self.time_y = self.cy+1000
                elif self.time_y < self.max_y+1000:
                    self.y -= speed
                    self.angle = 90
                    if self.level == 1:
                        self.vision_x = (self.rect.centerx-50)
                        self.vision_y = (self.rect.centery-100)
                    if self.level == 2:
                        self.vision_x = (self.rect.centerx-88)
                        self.vision_y = (self.rect.centery-175)
                else:
                    self.time_x = self.cx
                self.rect = pygame.Rect(self.x,self.y,(self.w),(self.h)) 
            else:
                self.rect = pygame.Rect(-50,-50,(self.w),(self.h))
        else:
            self.rect = pygame.Rect(self.x,self.y,(self.w),(self.h))
        
        self.vision = pygame.Surface((175,175))
        self.vision.fill((0,0,0))
        self.vision_rect = pygame.Rect(self.vision_x,self.vision_y,(175),(175))
              
    
    def die(self,deadmen):
        self.image = pygame.image.load('PNG/Man Old/manOld_stand.png')
        self.rect = pygame.Rect(-50,-50,(self.w),(self.h))
        self.vision_rect = pygame.Rect(-100,-100,(175),(175))
        self.dead = 1
        deadmen.append(self.x)
    def shoot(self,bg,man,man_x, man_y,screen, badguys):
        self.roving =1
        self.shot_flag =1
        gun = Gun()
        man_x_relative = man_x-self.x
        man_y_relative = man_y-self.y
        self.angle = degrees(atan2(-man_y_relative,man_x_relative))
        flag = 1
        gun.shoot(self.x+15,self.y+15,self.angle,screen)
        while flag ==1 :
            bg.draw(screen)
            man.draw(screen)
            for dude in badguys:
                dude.draw(screen)
            gun.update(screen)
            for wall in bg.walls:
                if pygame.Rect.colliderect(gun.rect, wall):
                    flag = False
                    break
            if pygame.Rect.colliderect(gun.rect,man.rect):
                man.die()
                flag = False
                break

            pygame.display.flip()
            clock.tick(400)
        pygame.display.flip()
        clock.tick(400)
            
    def draw(self,screen):
        if self.shot_flag ==1:
            self.double_tap_timer += 1
        new_bad_guy = pygame.transform.rotozoom(self.image,self.angle,0.8)
        #screen.blit(self.vision,(self.vision_x,self.vision_y))
        screen.blit(new_bad_guy, (self.x,self.y))