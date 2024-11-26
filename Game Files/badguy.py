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
        #set level for more intense looking bad guy
        self.level = level
        #set basic atributes
        self.angle = 0
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
        speed = 0.8
        self.max_x = max_x
        self.max_y = max_y
        self.the_x = -100
        self.the_y = -100
        if self.roving == 0:
            if self.dead ==0:
                if self.time < (self.max_x-self.cx):
                    self.x += speed
                    self.angle = 0
                    self.the_x = (self.rect.centerx)
                    self.the_y = (self.rect.centery-50)

                elif self.time < ((self.max_x-self.cx)+(self.max_y-self.cy)):
                    self.y += speed
                    self.angle = 270
                    self.the_x = (self.rect.centerx-50)
                    self.the_y = (self.rect.centery)
                elif self.time < ((self.max_x-self.cx)+(self.max_y-self.cy))+ (self.max_x-self.cx):
                    self.x -= speed
                    self.angle = 180
                    self.the_x = (self.rect.centerx-100)
                    self.the_y = (self.rect.centery-50)
                elif self.time < (((self.max_x-self.cx)+(self.max_y-self.cy))+ (self.max_x-self.cx))+(self.max_y-self.cy):
                    self.y -= speed
                    self.angle = 90
                    self.the_x = (self.rect.centerx-50)
                    self.the_y = (self.rect.centery-100)
                else:
                    self.time = 0
                self.rect = pygame.Rect(self.x,self.y,(self.w),(self.h)) 
            else:
                self.rect = pygame.Rect(-50,-50,(self.w),(self.h))
        else:
            self.rect = pygame.Rect(self.x,self.y,(self.w),(self.h))



        self.vision = pygame.Surface((100,100))
        self.vision.fill((0,0,0))
        self.vison_rect = pygame.Rect(self.the_x,self.the_y,(100),(100))

    def rove_rev (self, min_x,max_y):
        #set a time variable to control movement
        self.time_x += 1
        self.time_y += 1
        speed = 0.8
        self.min_x = min_x
        self.max_y = max_y
        self.the_x = -100
        self.the_y = -100
        if self.time_x < (self.min_x+self.cx):
            self.x -= speed
            self.angle = 180
            self.the_x = (self.rect.centerx-100)
            self.the_y = (self.rect.centery-50)
            self.time_y = 0
        elif self.time_y < (self.max_y-self.cy):
            self.y += speed
            self.angle = 270
            self.the_x = (self.rect.centerx-50)
            self.the_y = (self.rect.centery)
            self.time_x = 1000+self.cx
        elif self.time_x <(self.cx +self.min_x+1000):
            self.x += speed
            self.angle = 0
            self.the_x = (self.rect.centerx)
            self.the_y = (self.rect.centery-50)
            self.time_y = self.cy+1000
        elif self.time_y < self.max_y+1000:
            self.y -= speed
            self.angle = 90
            self.the_x = (self.rect.centerx-50)
            self.the_y = (self.rect.centery-100)
        else:
            self.time_x = self.cx

              
    
    def die(self,deadmen):
        self.image = pygame.image.load('PNG/Man Old/manOld_stand.png')
        self.rect = pygame.Rect(-50,-50,(self.w),(self.h))

        self.dead = 1
        deadmen.append(self.x)
    def shoot(self,bg,man,man_x, man_y,screen, badguy_1, badguy_2, badguy_3,badguy_4,badguy_5,badguy_6):
        self.roving =1
        gun = Gun()
        man_x_relative = man_x-self.x
        man_y_relative = man_y-self.y
        self.angle = degrees(atan2(-man_y_relative,man_x_relative))
        flag = 1
        gun.shoot(self.x+15,self.y+15,self.angle,screen)
        while flag ==1 :
            bg.draw(screen)
            man.draw(screen)
            badguy_1.draw(screen)
            badguy_2.draw(screen)
            badguy_3.draw(screen)
            badguy_4.draw(screen)
            badguy_5.draw(screen)
            badguy_6.draw(screen)
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
        new_bad_guy = pygame.transform.rotozoom(self.image,self.angle,0.8)
        #screen.blit(self.vision,(self.the_x,self.the_y))
        screen.blit(new_bad_guy, (self.x,self.y))