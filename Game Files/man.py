import pygame

class Man():
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.alive = 0
        self.angle = 0
        self.speed = 2
        self.reloading = False
        self.image = pygame.image.load('PNG/Survivor 1/survivor1_gun.png')
        self.w = self.image.get_width()
        self.h = (self.image.get_height()-5)
        self.rect = pygame.Rect(int(self.x),int(self.y),(self.h),(self.h))

    def check_keys(self):
        keys = pygame.key.get_pressed()
        # Move the man w keys
        if self.alive == 0:
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_d]:
                self.x += self.speed
            if keys[pygame.K_LEFT]:
                self.angle += 4
            if keys[pygame.K_RIGHT]:
                self.angle -= 4
        
        self.rect = pygame.Rect(self.x,self.y,self.h,self.h)

    def draw(self,screen):
        new_man = pygame.transform.rotozoom(self.image,self.angle,0.8)
        self.rect.center = (self.x,self.y)
        screen.blit(new_man, self.rect.center)
        #pygame.draw.rect(screen, (225,0,0), (self.x, self.y, self.h, self.h))

    def reload(self,screen):
        self.reloading = True
        # make sure man is still alive
        if self.alive == 0:
            # create reloading image
            reload_man = pygame.image.load('PNG/Survivor 1/survivor1_reload.png')
            # make the image the right size
            new_reload_man = pygame.transform.rotozoom(reload_man,self.angle,0.8)
            # blit the new image
            screen.blit(new_reload_man,(self.x,self.y))
        # if man not alive then blit dead man
        else:
            self.image = pygame.image.load('PNG/Survivor 1/survivor1_stand.png')
            new_dead_man = pygame.transform.rotozoom(self.image,self.angle,0.8)
            screen.blit(new_dead_man,(self.x,self.y))

        
    
    def die(self):
        self.alive =1
        self.image = pygame.image.load('PNG/Survivor 1/survivor1_stand.png')


