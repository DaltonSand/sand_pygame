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
        y_corner = pygame.Surface((1,15))
        x_corner = pygame.Surface((15,1))
        x_corner.fill((101, 67, 33))
        y_corner.fill((101, 67, 33))
        stair= pygame.Surface((25,113))
        stair_b = pygame.Surface((5,113))
        stair_b.fill((0,0,0))
        stair.fill((113, 121, 126))
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
                if (x==(3*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)) and (y!=8*self.TILE_SIZE):
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
        #coners_y
        self.bg.blit(y_corner,(11*self.TILE_SIZE,3*self.TILE_SIZE))
        self.bg.blit(y_corner,(4*self.TILE_SIZE,4*self.TILE_SIZE))
        self.bg.blit(y_corner,(8*self.TILE_SIZE,4*self.TILE_SIZE))
        self.bg.blit(y_corner,(7*self.TILE_SIZE,7*self.TILE_SIZE))
        self.bg.blit(y_corner,(8*self.TILE_SIZE,7*self.TILE_SIZE))
        
        #coners_x
        self.bg.blit(x_corner,(3*self.TILE_SIZE,8*self.TILE_SIZE-1))
        self.bg.blit(x_corner,(3*self.TILE_SIZE,9*self.TILE_SIZE))
        self.bg.blit(x_corner,(9*self.TILE_SIZE,9*self.TILE_SIZE-1))
        self.bg.blit(x_corner,(9*self.TILE_SIZE,5*self.TILE_SIZE-1))
        self.bg.blit(x_corner,(9*self.TILE_SIZE,6*self.TILE_SIZE))
        self.bg.blit(x_corner,(11*self.TILE_SIZE,5*self.TILE_SIZE-1))
        self.bg.blit(x_corner,(11*self.TILE_SIZE,7*self.TILE_SIZE-1))
        self.bg.blit(x_corner,(11*self.TILE_SIZE,8*self.TILE_SIZE-1))
        self.bg.blit(x_corner,(15*self.TILE_SIZE,3*self.TILE_SIZE))
        self.bg.blit(x_corner,(15*self.TILE_SIZE,5*self.TILE_SIZE-1))




        #575    3578
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

        # Draw boxes

        self.bg.blit(bigger_box,(300,463))
        self.bg.blit(bigger_box,(400,584))
        self.bg.blit(bigger_box,(300,325))
        self.bg.blit(bigger_box,(800,500))
        
        screen.blit(self.bg,(0,0))
        return self.bg
       

    # Wall collision rectangles
    def create_wall_collisions(self):
        self.walls = []
        self.walls_y =[]
        self.walls_x =[]
        self.boxes = []
        self.walls_outside = []
        for x in range(0,self.WIDTH,self.TILE_SIZE):
            for y in range(0,self.HEIGHT, self.TILE_SIZE):
                # Exterior X walls
                if (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y==self.TILE_SIZE):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    self.walls_x.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    
                elif (x>(2*self.TILE_SIZE) and x<(self.WIDTH-self.TILE_SIZE)) and (y==self.HEIGHT-self.TILE_SIZE):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    self.walls_x.append(pygame.Rect(x, y, self.TILE_SIZE, 15))

                    
                # Exterior Y walls
                if (x==(3*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)) and (y!=8*self.TILE_SIZE):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                    self.walls_y.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                elif (x==(self.WIDTH-self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x-15, y, 15, self.TILE_SIZE))
                    self.walls_y.append(pygame.Rect(x-15, y, 15, self.TILE_SIZE))
                    
                    
                # Interior X self.walls
                if (x>(2*self.TILE_SIZE) and x<(9*self.TILE_SIZE)) and (x!=7*self.TILE_SIZE) and (y==self.HEIGHT-(4*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    self.walls_x.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                if (x>(2*self.TILE_SIZE) and x<(8*self.TILE_SIZE)) and (x!=3*self.TILE_SIZE)and(y==self.HEIGHT-(7*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    self.walls_x.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                if (x>(10*self.TILE_SIZE) and x<(15*self.TILE_SIZE)) and(y==self.HEIGHT-(8*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    self.walls_x.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                if (x>(10*self.TILE_SIZE) and x<(18*self.TILE_SIZE)) and(y==self.HEIGHT-(5*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    self.walls_x.append(pygame.Rect(x, y, self.TILE_SIZE, 15))
                    
                # Interior Y self.walls
                if (x==(9*self.TILE_SIZE)) and (y!=5*self.TILE_SIZE) and (y!=9*self.TILE_SIZE) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                    self.walls_y.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                if (x==(6*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-7*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                    self.walls_y.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                if (x==(11*self.TILE_SIZE)) and (y>(.5*self.TILE_SIZE) and y<(self.HEIGHT-self.TILE_SIZE)) and (y!= 7*self.TILE_SIZE) and (y!= 3*self.TILE_SIZE) and (y!= 4*self.TILE_SIZE):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                    self.walls_y.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                if (x==(15*self.TILE_SIZE)) and (y>(2*self.TILE_SIZE) and y<(self.HEIGHT-6*self.TILE_SIZE)):
                    self.walls.append(pygame.Rect(x, y, 15, self.TILE_SIZE))
                    self.walls_y.append(pygame.Rect(x, y, 15, self.TILE_SIZE))

                #coners_y
                self.walls_y.append(pygame.Rect(11*self.TILE_SIZE,3*self.TILE_SIZE,1,14))
                self.walls_y.append(pygame.Rect(4*self.TILE_SIZE,4*self.TILE_SIZE,1,14))
                self.walls_y.append(pygame.Rect(8*self.TILE_SIZE,4*self.TILE_SIZE,1,14))
                self.walls_y.append(pygame.Rect(7*self.TILE_SIZE,7*self.TILE_SIZE,1,14))
                self.walls_y.append(pygame.Rect(8*self.TILE_SIZE,7*self.TILE_SIZE,1,14))
                #coners_x
                self.walls_x.append(pygame.Rect(3*self.TILE_SIZE,8*self.TILE_SIZE-1,15,1))
                self.walls_x.append(pygame.Rect(3*self.TILE_SIZE,9*self.TILE_SIZE,15,1))
                self.walls_x.append(pygame.Rect(9*self.TILE_SIZE,9*self.TILE_SIZE-1,15,1))
                self.walls_x.append(pygame.Rect(9*self.TILE_SIZE,5*self.TILE_SIZE-1,15,1))
                self.walls_x.append(pygame.Rect(9*self.TILE_SIZE,6*self.TILE_SIZE,15,1))
                self.walls_x.append(pygame.Rect(11*self.TILE_SIZE,5*self.TILE_SIZE-1,15,1))
                self.walls_x.append(pygame.Rect(11*self.TILE_SIZE,7*self.TILE_SIZE-1,15,1))
                self.walls_x.append(pygame.Rect(11*self.TILE_SIZE,8*self.TILE_SIZE-1,15,1))
                self.walls_x.append(pygame.Rect(15*self.TILE_SIZE,3*self.TILE_SIZE,15,1))
                self.walls_x.append(pygame.Rect(15*self.TILE_SIZE,5*self.TILE_SIZE-1,15,1))


                #Boxes
                self.walls.append(pygame.Rect(300,463,bigger_box.get_width(),bigger_box.get_width()))
                self.boxes.append(pygame.Rect(300,463,bigger_box.get_width(),bigger_box.get_width()))

                self.walls.append(pygame.Rect(400,584,bigger_box.get_width(),bigger_box.get_width()))
                self.boxes.append(pygame.Rect(400,584,bigger_box.get_width(),bigger_box.get_width()))

                self.walls.append(pygame.Rect(300,325,bigger_box.get_width(),bigger_box.get_width()))
                self.boxes.append(pygame.Rect(300,325,bigger_box.get_width(),bigger_box.get_width()))

                self.walls.append(pygame.Rect(800,500,bigger_box.get_width(),bigger_box.get_width()))
                self.boxes.append(pygame.Rect(800,500,bigger_box.get_width(),bigger_box.get_width()))

