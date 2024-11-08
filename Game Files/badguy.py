import pygame
from gun import Gun
from math import atan, pi
clock = pygame.time.Clock()

flag = 0
class BadGuy():
    def __init__ (self,x,y):
        self.x = x
        self.cx = x
        self.y = y
        self.cy = y
        self.angle = 0
        self.time = 0
        self.dead = 0
        
        self.image = pygame.image.load('PNG/Soldier 1/soldier1_machine.png')
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = pygame.Rect(self.x,self.y,(self.w),(self.h))

    def rove(self, max_x,max_y):
        self.time += 1
        speed = 0.8
        self.max_x = max_x
        self.max_y = max_y
        self.the_x = -100
        self.the_y = -100
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


        self.vision = pygame.Surface((100,100))
        self.vision.fill((0,0,0))
        self.vison_rect = pygame.Rect(self.the_x,self.the_y,(100),(100))


    
    def die(self,deadmen):
        self.image = pygame.image.load('PNG/Man Old/manOld_stand.png')
        self.rect = pygame.Rect(-50,-50,(self.w),(self.h))

        self.dead = 1
        deadmen.append(self.x)
    def shoot(self,bg,man,man_x, man_y,screen, badguy_1, badguy_2, badguy_3,badguy_4,badguy_5,badguy_6):
        self.dead =1
        gun = Gun()
        man_x_relative = man_x-self.x
        man_y_relative = man_y-self.y
        if self.angle == 0:
            man_angle = atan((man_y_relative/man_x_relative))
            self.angle = -man_angle*180/pi
        if self.angle == 90:
            man_angle = atan((man_x_relative/man_y_relative))
            self.angle = man_angle*180/pi+90
        if self.angle == 180:
            man_angle = atan((man_y_relative/man_x_relative))
            self.angle = -man_angle*180/pi+180
        if self.angle == 270:
            man_angle = atan((man_x_relative/man_y_relative))
            self.angle = man_angle*180/pi+270
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