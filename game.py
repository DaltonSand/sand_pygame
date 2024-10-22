import pygame

# pygame setup
pygame.init()
WIDTH = 1216
HEIGHT = 704

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#Background 
bg = pygame.Surface((WIDTH,HEIGHT))
bg.fill((255,0,0))

#ground tile_1
grass = pygame.image.load('PNG/Tiles/tile_01.png')
dirt = pygame.image.load('PNG/Tiles/tile_05.png')
gravel = pygame.image.load('PNG/Tiles/tile_07.png')
wood_floor = pygame.image.load('PNG/Tiles/tile_71.png')
TILE_SIZE = grass.get_width()
wallx = pygame.Surface((TILE_SIZE,15))
wally = pygame.Surface((15,TILE_SIZE))
wally.fill((0,0,0))
wallx.fill((0,0,0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # blit bg onto screen
    screen.blit(bg,(0,0))
    #fill in background
    for x in range(0,WIDTH,TILE_SIZE):
    # loop over y direction
        for y in range(0,HEIGHT, TILE_SIZE):
        # blit the tile to our BG
            bg.blit(grass,(x,y))
            if (x>(2*TILE_SIZE) and x<(WIDTH-TILE_SIZE)) and (y>(.5*TILE_SIZE) and y<(HEIGHT-TILE_SIZE)):
                bg.blit(wood_floor,(x,y))
            #bilt walls
            if (x>(2*TILE_SIZE) and x<(WIDTH-TILE_SIZE)) and (y==TILE_SIZE):
                bg.blit(wallx,(x,y))
            elif (x>(2*TILE_SIZE) and x<(WIDTH-TILE_SIZE)) and (y==HEIGHT-TILE_SIZE):
                bg.blit(wallx,(x,y))
            elif (x>(2*TILE_SIZE) and x<(WIDTH-TILE_SIZE)) and (y==HEIGHT-(4*TILE_SIZE)):
                bg.blit(wallx,(x,y))

            if (x==(3*TILE_SIZE)) and (y>(.5*TILE_SIZE) and y<(HEIGHT-TILE_SIZE)) and (y!= 8*TILE_SIZE):
                bg.blit(wally,(x,y))
            elif (x==(WIDTH-TILE_SIZE)) and (y>(.5*TILE_SIZE) and y<(HEIGHT-TILE_SIZE)):
                bg.blit(wally,(x,y))
            


    
           
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()