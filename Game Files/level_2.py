#LEVEL 2
import pygame
from walls2 import Background_2
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


bg = Background_2(WIDTH, HEIGHT,TILE_SIZE)
bg.draw(screen)
#badguys
badguy_1 = BadGuy(275,125,2)
badguy_2 = BadGuy(225,140,2)
badguy_3 = BadGuy(635,125,2)
#badguy_4 = BadGuy(250,125,2)
badguy_5 = BadGuy(740,250,2)
badguy_6 = BadGuy(730,450,2)
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
    badguy_1.rove(300,300)
    badguy_2.rove(350,280)
    badguy_3.rove(640,700)
    #badguy_4.rove(350,200)
    badguy_5.rove(870,280)
    badguy_6.rove(950,600)
    badguy_1.draw(screen)
    badguy_2.draw(screen)
    badguy_3.draw(screen)
    #badguy_4.draw(screen)
    badguy_5.draw(screen)
    badguy_6.draw(screen)

    man.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()