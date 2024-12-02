#LEVEL 2
import pygame
from walls3 import Background_3
from man import Man
from gun import Gun, Reload, reload
from badguy import BadGuy

pygame.init()
WIDTH = 1216
HEIGHT = 704
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
# Tiles
grass = pygame.image.load('PNG/Tiles/tile_01.png')
box = pygame.image.load('PNG/crateMetal.png')
box_scale = (box.get_width()*2,box.get_height()*2)
bigger_box = pygame.transform.scale(box,box_scale)
wood_floor = pygame.image.load('PNG/Tiles/tile_43.png')
bullet = pygame.image.load('PNG/bullet.png')

man = Man(750,120)

TILE_SIZE = grass.get_width()


bg = Background_3(WIDTH, HEIGHT,TILE_SIZE)
bg.draw(screen)
#badguys
badguy_7 = BadGuy(340,120,2)
badguy_8 = BadGuy(225,85,2)
badguy_9 = BadGuy(635,125,2)
badguy_10 = BadGuy(450,200,2)
badguy_11= BadGuy(950,150,2)
badguy_12= BadGuy(730,480,2)
badguy_13= BadGuy(1050,350,2)
badguy_14= BadGuy(250,350,2)
# Run game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    bg.draw(screen)
        #COLLISONS - walls/screen
    pre_x = man.x
    pre_y = man.y
    man.check_keys()
    if man.x <1 or man.x >WIDTH:
        man.x = pre_x
    if man.y <1 or man.y > HEIGHT:
        man.y = pre_y
    for wall in bg.walls:
        if pygame.Rect.colliderect(man.rect, wall):
            man.x = pre_x
            man.y = pre_y

    # Badguys move around/blit 
    badguy_7.rove_rev(85,230)
    badguy_8.rove(310,190)
    badguy_9.rove(640,450)
    badguy_10.rove(580,320)
    badguy_11.rove(1040,220)
    badguy_12.rove(970,560)
    badguy_13.rove_rev(600,380)
    badguy_14.rove(800,380)
    badguy_7.draw(screen)
    badguy_8.draw(screen)
    badguy_9.draw(screen)
    badguy_10.draw(screen)
    badguy_11.draw(screen)
    badguy_12.draw(screen)
    badguy_13.draw(screen)
    badguy_14.draw(screen)

    man.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()