import pygame
import math
from man import Man
from walls import Background
from gun import Gun, Reload, reload
from badguy import BadGuy

# pygame setup
pygame.init()
WIDTH = 1216
HEIGHT = 704
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
bullets = []
shot_num = 0 
reload_num = 100
shot_max =8
deadmen = []
fail = 0

# Tiles
grass = pygame.image.load('PNG/Tiles/tile_01.png')
box = pygame.image.load('PNG/crateMetal.png')
box_scale = (box.get_width()*2,box.get_height()*2)
bigger_box = pygame.transform.scale(box,box_scale)
wood_floor = pygame.image.load('PNG/Tiles/tile_43.png')

# Text - time, font
text = 541
font = pygame.font.Font(None,42)


# THE MAN
man = Man(75,350)
badguy_1 = BadGuy(375,290)
badguy_2 = BadGuy(250,540)
badguy_3 = BadGuy(635,125)
badguy_4 = BadGuy(250,125)
badguy_5 = BadGuy(740,250)
badguy_6 = BadGuy(730,450)


# Sizes
TILE_SIZE = grass.get_width()

# Create initial background and wall collisions
bg = Background(WIDTH, HEIGHT,TILE_SIZE)
bg.draw(screen)
bg.create_wall_collisions()

# Run game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    #DRAW EVERYTHING
    bg.draw(screen)

    # Badguys move around/blit 
    badguy_1.rove(550,400)
    badguy_2.rove(550,544)
    badguy_3.rove(640,700)
    badguy_4.rove(350,200)
    badguy_5.rove(870,280)
    badguy_6.rove(950,600)
    badguy_1.draw(screen)
    badguy_2.draw(screen)
    badguy_3.draw(screen)
    badguy_4.draw(screen)
    badguy_5.draw(screen)
    badguy_6.draw(screen)

    # Draw time/win status
    if man.x > 700 and man.y<200 and man.x<900 and len(deadmen) == 6 and fail ==0:
        text_surface = font.render("VICTORY", True, (0,0,0))
    elif man.alive == 1:
        text_surface = font.render("FAIL", True, (0,0,0))
        fail = 1
    elif text <600:
        text_surface = font.render("", True, (0,0,0))
    elif text > 600 and text <660:
        text_surface = font.render("10", True, (0,0,0))
    elif text > 660 and text <720:
        text_surface = font.render("9", True, (0,0,0))
    elif text > 720 and text <780:
        text_surface = font.render("8", True, (0,0,0))
    elif text > 780 and text <840:
        text_surface = font.render("7", True, (0,0,0))
    elif text > 840 and text <900:
        text_surface = font.render("6", True, (0,0,0))
    elif text > 900 and text <960:
        text_surface = font.render("5", True, (0,0,0))
    elif text > 960 and text <1020:
        text_surface = font.render("4", True, (0,0,0))
    elif text > 1020 and text <1080:
        text_surface = font.render("3", True, (0,0,0))
    elif text > 1080 and text <1140:
        text_surface = font.render("2", True, (0,0,0))
    elif text > 1140 and text <1200:
        text_surface = font.render("1", True, (0,0,0))
    elif text >1200:
        text_surface = font.render("FAIL", True, (0,0,0))
        fail = 1
    text_rect = text_surface.get_rect(center=(652,30))

    # MAN RELOAD - TEXT
    if man.reloading == True and shot_num < shot_max:
        text_surface_reload = font.render("RELOADING", True, (0,0,0))
    elif man.reloading == False:
        text_surface_reload = font.render("READY TO FIRE", True, (0,0,0))
    else:
        text_surface_reload = font.render("OUT OF BULLETS", True, (0,0,0))
    text_rect_reload = text_surface_reload.get_rect(center =(125,30))
    

    reload_num +=1
    reload(man,reload_num,shot_num,shot_max,screen)

    # Initilize Keys
    keys = pygame.key.get_pressed()

    # Check for Shoot (space)
    flag_1 = False
    if keys[pygame.K_SPACE] and shot_num <shot_max and reload_num >100 and man.alive ==0:
        shot = Gun()
        bullets.append(shot)
        shot.shoot(man.x+15,man.y+15,man.angle,screen)
        shot_num = shot_num+1
        reload_num =0
        flag_1 = True

    # Fire the bullet
    while flag_1:
        # Draw Everything (#hatewhileloops)
        bg.draw(screen)
        shot.update(screen)
        man.reload(screen)
        badguy_1.draw(screen)
        badguy_2.draw(screen)
        badguy_3.draw(screen)
        badguy_4.draw(screen)
        badguy_5.draw(screen)
        badguy_6.draw(screen)
        
        # Check for bullet/wall collisons
        for wall in bg.walls:
            if pygame.Rect.colliderect(shot.rect, wall):
                flag_1 = False
                break
        # Check to see if bullet hit a bad guy
        if pygame.Rect.colliderect(shot.rect,badguy_1.rect):
            badguy_1.die(deadmen)
            text -= 200
            break
        if pygame.Rect.colliderect(shot.rect,badguy_2.rect):
            badguy_2.die(deadmen)
            text -= 200
            break
        if pygame.Rect.colliderect(shot.rect,badguy_3.rect):
            badguy_3.die(deadmen)
            text -= 200
            break
        if pygame.Rect.colliderect(shot.rect,badguy_4.rect):
            badguy_4.die(deadmen)
            text -= 200
            break
        if pygame.Rect.colliderect(shot.rect,badguy_5.rect):
            badguy_5.die(deadmen)
            text -= 200
            break
        if pygame.Rect.colliderect(shot.rect,badguy_6.rect):
            badguy_6.die(deadmen)
            text -= 200
            break
        if shot.x > WIDTH or shot.x <0 or shot.y <0 or shot.y > HEIGHT:
            break
        pygame.display.flip()
        # Speed up display (bullet -> faster)
        clock.tick(600)

    # Check if Man Spotted (kill him)
    if pygame.Rect.colliderect(man.rect, badguy_1.vison_rect):
        print('\n\n\n\nspoted\n\n\n\n\n')
        badguy_1.shoot(bg,man,man.x,man.y,screen,badguy_1,badguy_2,badguy_3,badguy_4,badguy_5,badguy_6)
    if pygame.Rect.colliderect(man.rect, badguy_2.vison_rect):
        print('\n\n\n\nspoted\n\n\n\n\n')
        badguy_2.shoot(bg,man,man.x,man.y,screen,badguy_1,badguy_2,badguy_3,badguy_4,badguy_5,badguy_6)
    if pygame.Rect.colliderect(man.rect, badguy_3.vison_rect):
        print('\n\n\n\nspoted\n\n\n\n\n')
        badguy_3.shoot(bg,man, man.x,man.y,screen,badguy_1,badguy_2,badguy_3,badguy_4,badguy_5,badguy_6)
    if pygame.Rect.colliderect(man.rect, badguy_4.vison_rect):
        print('\n\n\n\nspoted\n\n\n\n\n')
        badguy_4.shoot(bg,man, man.x,man.y,screen,badguy_1,badguy_2,badguy_3,badguy_4,badguy_5,badguy_6)
    if pygame.Rect.colliderect(man.rect, badguy_5.vison_rect):
        print('\n\n\n\nspoted\n\n\n\n\n')
        badguy_5.shoot(bg,man, man.x,man.y,screen,badguy_1,badguy_2,badguy_3,badguy_4,badguy_5,badguy_6)
    if pygame.Rect.colliderect(man.rect, badguy_6.vison_rect):
        print('\n\n\n\nspoted\n\n\n\n\n')
        badguy_6.shoot(bg,man, man.x,man.y,screen,badguy_1,badguy_2,badguy_3,badguy_4,badguy_5,badguy_6)

    # Blit Text
    screen.blit(text_surface,text_rect)
    screen.blit(text_surface_reload,text_rect_reload)

    # Blit man image
    if reload_num >100 or shot_num >shot_max:
        man.draw(screen)
    else:
        man.reload(screen)
    
    # Increase Time for text
    text += 1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()