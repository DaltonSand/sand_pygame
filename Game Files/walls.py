import pygame
from badguy import BadGuy
grass = pygame.image.load('PNG/Tiles/tile_01.png')
wood_floor = pygame.image.load('PNG/Tiles/tile_43.png')
box = pygame.image.load('PNG/crateMetal.png')
box_scale = (box.get_width()*2,box.get_height()*2)
bigger_box = pygame.transform.scale(box,box_scale)


class Background():
    def __init__ (self, WIDTH, HEIGHT, TILE_SIZE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TILE_SIZE = TILE_SIZE
        self.bg = pygame.Surface((WIDTH,HEIGHT))
        # RED (To see if there is a gap)
        self.bg.fill((255,0,0))
    def draw(self, screen):
        wallx= pygame.Surface((self.TILE_SIZE,15))
        wally= pygame.Surface((15,self.TILE_SIZE))
        wally.fill((60, 30, 10))
        wallx.fill((60, 30, 10))
        # Loop over X and Y to cover entire screen
        for x in range(0,self.WIDTH,self.TILE_SIZE):
            for y in range(0,self.HEIGHT, self.TILE_SIZE):

                # Grass
                self.bg.blit(grass,(x,y))

                # Wood floor
                if (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.bg.blit(wood_floor,(x,y))
                
                # Exterior X walls
                if (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y==self.TILE_SIZE):
                    self.bg.blit(wallx,(x,y))
                elif (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y==self.HEIGHT-self.TILE_SIZE):
                    self.bg.blit(wallx,(x,y))
                    
                # Exterior Y walls
                if (x==(3*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)) and (y!= 7*self.TILE_SIZE):
                    self.bg.blit(wally,(x,y))
                elif (x==(self.WIDTH-self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.bg.blit(wally,((x-15),y))
                    
                # Interior X walls
                if (x>(2*self.TILE_SIZE) and x<(9*self.TILE_SIZE)) and (x!=7*self.TILE_SIZE) and (y==self.HEIGHT-(4*self.TILE_SIZE)):
                    self.bg.blit(wallx,(x,y))
                if (x>(2*self.TILE_SIZE) and x<(8*self.TILE_SIZE)) and (x!=3*self.TILE_SIZE)and(y==self.HEIGHT-(7*self.TILE_SIZE)):
                    self.bg.blit(wallx,(x,y))
                if (x>(10*self.TILE_SIZE) and x<(15*self.TILE_SIZE)) and(y==self.HEIGHT-(8*self.TILE_SIZE)):
                    self.bg.blit(wallx,(x,y))
                if (x>(10*self.TILE_SIZE) and x<(18*self.TILE_SIZE)) and(y==self.HEIGHT-(5*self.TILE_SIZE)):
                    self.bg.blit(wallx,(x,y))
                    
                # Interior Y walls
                if (x==(9*self.TILE_SIZE)) and (y!=5*self.TILE_SIZE) and (y!=9*self.TILE_SIZE) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.bg.blit(wally,(x,y))
                if (x==(6*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-7*self.TILE_SIZE)):
                    self.bg.blit(wally,(x,y))
                if (x==(11*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)) and (y!= 7*self.TILE_SIZE) and (y!= 3*self.TILE_SIZE) and (y!= 4*self.TILE_SIZE):
                    self.bg.blit(wally,(x,y))
                if (x==(15*self.TILE_SIZE)) and (y>(2*self.TILE_SIZE) and y<(self.HEIGHT-6*self.TILE_SIZE)):
                    self.bg.blit(wally,(x,y))

        # Draw boxes
        self.bg.blit(bigger_box,(300,463))
        self.bg.blit(bigger_box,(400,584))
        self.bg.blit(bigger_box,(300,325))
        self.bg.blit(bigger_box,(800,500))

        
        screen.blit(self.bg,(0,0))
       

    # Wall collision rectangles
    def create_wall_collisions(self):
        self.walls = []
        for x in range(0,self.WIDTH,self.TILE_SIZE):
            for y in range(0,self.HEIGHT, self.TILE_SIZE):
                # Exterior X walls
                if (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y==self.TILE_SIZE):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                elif (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y==self.HEIGHT-self.TILE_SIZE):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    
                # Exterior Y walls
                if (x==(3*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)) and (y!= 7*self.TILE_SIZE):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                elif (x==(self.WIDTH-self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x-15, y, 15, self.TILE_SIZE))
                    
                # Interior X self.walls
                if (x>(2*self.TILE_SIZE) and x<(9*self.TILE_SIZE)) and (x!=7*self.TILE_SIZE) and (y==self.HEIGHT-(4*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                if (x>(2*self.TILE_SIZE) and x<(8*self.TILE_SIZE)) and (x!=3*self.TILE_SIZE)and(y==self.HEIGHT-(7*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                if (x>(10*self.TILE_SIZE) and x<(15*self.TILE_SIZE)) and(y==self.HEIGHT-(8*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                if (x>(10*self.TILE_SIZE) and x<(18*self.TILE_SIZE)) and(y==self.HEIGHT-(5*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    
                # Interior Y self.walls
                if (x==(9*self.TILE_SIZE)) and (y!=5*self.TILE_SIZE) and (y!=9*self.TILE_SIZE) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                if (x==(6*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-7*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                if (x==(11*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)) and (y!= 7*self.TILE_SIZE) and (y!= 3*self.TILE_SIZE) and (y!= 4*self.TILE_SIZE):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                if (x==(15*self.TILE_SIZE)) and (y>(2*self.TILE_SIZE) and y<(self.HEIGHT-6*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))

                #Boxes
                self.walls.append(pygame.Rect(300,463,bigger_box.get_width(),bigger_box.get_width()))
                self.walls.append(pygame.Rect(400,584,bigger_box.get_width(),bigger_box.get_width()))
                self.walls.append(pygame.Rect(300,325,bigger_box.get_width(),bigger_box.get_width()))
                self.walls.append(pygame.Rect(800,500,bigger_box.get_width(),bigger_box.get_width()))