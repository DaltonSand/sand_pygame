import pygame
from badguy import BadGuy
grass = pygame.image.load('PNG/Tiles/tile_01.png')
wood_floor = pygame.image.load('PNG/Tiles/tile_43.png')
box = pygame.image.load('PNG/crateMetal.png')
box_scale = (box.get_width()*2,box.get_height()*2)
bigger_box = pygame.transform.scale(box,box_scale)


class Background_2():
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
        wall_corner =pygame.Surface((15,15)) 
        stair= pygame.Surface((25,113))
        stair_b = pygame.Surface((5,113))
        stair_b.fill((0,0,0))
        stair.fill((113, 121, 126))
        wally.fill((60, 30, 10))
        wallx.fill((60, 30, 10))
        wall_corner.fill((60,30,10))
        self.walls = []
        # Loop over X and Y to cover entire screen
        for x in range(0,self.WIDTH,self.TILE_SIZE):
            for y in range(0,self.HEIGHT, int(self.TILE_SIZE)):

                # Grass
                self.bg.blit(grass,(x,y))

                # Wood floor
                if (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.bg.blit(wood_floor,(x,y))
                
                # Exterior X walls
                if (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y==self.TILE_SIZE):
                    self.bg.blit(wallx,(x,y))
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                elif (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y==self.HEIGHT-self.TILE_SIZE):
                    self.bg.blit(wallx,(x,y))
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    
                # Exterior Y walls
                if (x==(3*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.bg.blit(wally,(x,y))
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                elif (x==(self.WIDTH-self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-1.5*self.TILE_SIZE)):
                    self.bg.blit(wally,((x-15),y))
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                
                # Interior X walls
                if (x>(2*self.TILE_SIZE) and (x!=9*self.TILE_SIZE)) and x<(18*self.TILE_SIZE) and (x!=10*self.TILE_SIZE) and (x!=7*self.TILE_SIZE) and (x!=14*self.TILE_SIZE) and (y==self.HEIGHT-(4*self.TILE_SIZE)):
                    self.bg.blit(wallx,(x,y))
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))

                if (x>(10*self.TILE_SIZE) and x<(14*self.TILE_SIZE)) and(y==self.HEIGHT-(8*self.TILE_SIZE)):
                    self.bg.blit(wallx,(x,y))
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))

                if (x>(2*self.TILE_SIZE) and x<(18*self.TILE_SIZE))and (x!=4*self.TILE_SIZE)and(x!=10*self.TILE_SIZE) and (x!=9*self.TILE_SIZE)and (x!=16*self.TILE_SIZE)and(y==self.HEIGHT-(6*self.TILE_SIZE)):
                    self.bg.blit(wallx,(x,y))
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))

                    
                # Interior Y walls
                if (x==(9*self.TILE_SIZE)) and (y!=5*self.TILE_SIZE) and (y!=9*self.TILE_SIZE)and (y!=3*self.TILE_SIZE)and(y!=6*self.TILE_SIZE) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.bg.blit(wally,(x,y))
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))

                if (x==(6*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-7*self.TILE_SIZE)):
                    self.bg.blit(wally,(x,y))
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))

                if (x==(11*self.TILE_SIZE)) and (y>(2*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)) and (y!=5*self.TILE_SIZE)and (y!=6*self.TILE_SIZE) and (y!=9*self.TILE_SIZE):
                    self.bg.blit(wally,(x,y))
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))

                if (x==(14*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-8*self.TILE_SIZE)):
                    self.bg.blit(wally,(x,y))
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))

        #corners
        self.bg.blit(wall_corner,(9*self.TILE_SIZE,5*self.TILE_SIZE))
        self.bg.blit(wall_corner,(14*self.TILE_SIZE,3*self.TILE_SIZE))


        #stairs
        
        self.bg.blit(stair,(719,79))
        self.bg.blit(stair_b,(744,79))
        self.bg.blit(stair,(749,79))
        self.bg.blit(stair_b,(774,79))
        self.bg.blit(stair,(779,79))
        self.bg.blit(stair_b,(804,79))
        self.bg.blit(stair,(809,79))
        self.bg.blit(stair_b,(834,79))
        self.bg.blit(stair,(839,79))
        self.bg.blit(stair_b,(864,79))
        self.bg.blit(stair,(869,79))
        
        screen.blit(self.bg,(0,0))
        return self.bg

