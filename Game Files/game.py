import pygame
import math
from man import Man
from walls import Background
from gun import Gun, Reload, reload
from badguy import BadGuy
from walls2 import Background_2

# pygame setup
pygame.init()
WIDTH = 1216
HEIGHT = 704
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# variable set up
bullets = []
shot_num = 0 
reload_num = 100
shot_max =7
deadmen = []
fail = 0
show_title = 1
title_time = 0
bg_alpha = 120
title_alpha = 400
color = (0,0,0)
level= 1

# Tiles
grass = pygame.image.load('PNG/Tiles/tile_01.png')
box = pygame.image.load('PNG/crateMetal.png')
box_scale = (box.get_width()*2,box.get_height()*2)
bigger_box = pygame.transform.scale(box,box_scale)
wood_floor = pygame.image.load('PNG/Tiles/tile_43.png')
bullet = pygame.image.load('PNG/bullet.png')

# Text - time, font
game_time = 15.1
font = pygame.font.Font(None,42)

# THE MAN
man = Man(75,350)

# Sizes
TILE_SIZE = grass.get_width()

#create bad guys for each level
if level == 1:
    # Create initial background and wall collisions
    bg = Background(WIDTH, HEIGHT,TILE_SIZE)
    bg.draw(screen)
    bg.create_wall_collisions()

    #badguys
    badguy_1 = BadGuy(375,290)
    badguy_2 = BadGuy(250,540)
    badguy_3 = BadGuy(635,125)
    badguy_4 = BadGuy(250,125)
    badguy_5 = BadGuy(740,250)
    badguy_6 = BadGuy(730,450)
elif level == 2:
    #create level 2 background & collisons
    bg = Background_2 (WIDTH,HEIGHT,TILE_SIZE)
    bg.draw(screen)

#MUSIC
bg_music = pygame.mixer.Sound('VTEMO - Drifting (freetouse.com).mp3')
bg_music.set_volume(0.5)
bg_music.play(-1)

# Run game loop
while running:
    # Run until 'X' is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #initilize keys
    keys = pygame.key.get_pressed()

    #COLLISONS - walls/screen
    pre_x = man.x
    pre_y = man.y
    man.check_keys()
    if man.x <1 or man.x >WIDTH-35:
        man.x = pre_x
    if man.y <1 or man.y > HEIGHT-35:
        man.y = pre_y
    for wall in bg.walls:
        if pygame.Rect.colliderect(man.rect, wall):
            man.x = pre_x
            man.y = pre_y

    #DRAW EVERYTHING
    screen.fill(color)
    #LEVEL 1
    if level == 1:
        #draw background
        bg.draw(screen)
        # Draw Title
        if title_time < 120:
            title_surface = font.render("Killing Osama bin Laden: Level 1", True, (255,255,255))
            bg_alpha += 1
            title_alpha -= 4
        else:
            title_surface = font.render("", True, (0,0,0))
            title_alpha = 0
            bg_alpha = 254
        bg.bg.set_alpha(bg_alpha)
        title_surface.set_alpha(title_alpha)
        title_rect = title_surface.get_rect(center=(WIDTH//2,HEIGHT//2))
        screen.blit(title_surface,title_rect)

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
        if fail == 0:
            if man.x > 700 and man.y<200 and man.x<830 and len(deadmen) == 6 and fail ==0:
                text_surface = font.render("VICTORY", True, (0,0,0))
                level = 2
            elif man.alive == 1:
                text_surface = font.render("", True, (0,0,0))
                fail = 1
            elif game_time > 19:
                text_surface = font.render("19", True, (0,0,0))
            elif game_time > 18 and game_time <19:
                text_surface = font.render("18", True, (0,0,0))
            elif game_time > 17 and game_time <18:
                text_surface = font.render("17", True, (0,0,0))
            elif game_time > 16 and game_time <17:
                text_surface = font.render("16", True, (0,0,0))
            elif game_time > 15 and game_time <16:
                text_surface = font.render("15", True, (0,0,0))
            elif game_time > 14 and game_time <15:
                text_surface = font.render("14", True, (0,0,0))
            elif game_time > 13 and game_time <14:
                text_surface = font.render("13", True, (0,0,0))
            elif game_time > 12 and game_time <13:
                text_surface = font.render("12", True, (0,0,0))
            elif game_time > 11 and game_time <12:
                text_surface = font.render("11", True, (0,0,0))
            elif game_time > 10 and game_time <11:
                text_surface = font.render("10", True, (0,0,0))
            elif game_time > 9 and game_time <10:
                text_surface = font.render("9", True, (0,0,0))
            elif game_time > 8 and game_time <9:
                text_surface = font.render("8", True, (0,0,0))
            elif game_time > 7 and game_time <8:
                text_surface = font.render("7", True, (0,0,0))
            elif game_time > 6 and game_time <7:
                text_surface = font.render("6", True, (0,0,0))
            elif game_time > 5 and game_time <6:
                text_surface = font.render("5", True, (0,0,0))
            elif game_time > 4 and game_time <5:
                text_surface = font.render("4", True, (0,0,0))
            elif game_time > 3 and game_time <4:
                text_surface = font.render("3", True, (0,0,0))
            elif game_time > 2 and game_time <3:
                text_surface = font.render("2", True, (0,0,0))
            elif game_time > 1 and game_time <2:
                text_surface = font.render("1", True, (0,0,0))
            elif game_time <1:
                text_surface = font.render("", True, (0,0,0))
                fail = 1
            text_rect = text_surface.get_rect(center=(652,30))
        else:
            text_surface = font.render("FAIL", True, (225,225,225))
            text_rect = text_surface.get_rect(center=(WIDTH/2,HEIGHT/2))
            color = (138, 3, 3)
            bg_alpha =120
            bg.bg.set_alpha(bg_alpha)
            man.die()

        # MAN RELOAD - TEXT
        if man.reloading == True and shot_num < shot_max:
            text_surface_reload = font.render("RELOADING", True, (0,0,0))
        elif man.reloading == False:
            text_surface_reload = font.render("READY TO FIRE", True, (0,0,0))
        else:
            text_surface_reload = font.render("OUT OF BULLETS", True, (0,0,0))
        text_rect_reload = text_surface_reload.get_rect(center =(125,30))

        # Draw Num Bullets left
        bullet_r = pygame.transform.rotozoom(bullet,0,0.02)
        bullet_num = shot_max-shot_num
        for x in range(15,15*bullet_num+15,15):
            screen.blit(bullet_r, (x,75))

        # reload bar
        reload_num +=1
        reload(man,reload_num,shot_num,shot_max,screen)


        # Check for Shoot (space)
        flag_1 = False
        if keys[pygame.K_SPACE] and shot_num <shot_max and reload_num >100 and man.alive ==0:
            shot = Gun()
            bullets.append(shot)
            shot.shoot(man.x+15,man.y+15,man.angle,screen)
            shot_num = shot_num+1
            reload_num =0
            flag_1 = True

        #bypass level 1
        if keys[pygame.K_p]:
            level = 2

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
            # Blit Text
            screen.blit(text_surface,text_rect)
            screen.blit(text_surface_reload,text_rect_reload)
            # Check for bullet/wall collisons
            for wall in bg.walls:
                if pygame.Rect.colliderect(shot.rect, wall):
                    flag_1 = False
                    break
            # Check to see if bullet hit a bad guy
            if pygame.Rect.colliderect(shot.rect,badguy_1.rect):
                badguy_1.die(deadmen)
                game_time += 3
                break
            if pygame.Rect.colliderect(shot.rect,badguy_2.rect):
                badguy_2.die(deadmen)
                game_time += 3
                break
            if pygame.Rect.colliderect(shot.rect,badguy_3.rect):
                badguy_3.die(deadmen)
                game_time += 3
                break
            if pygame.Rect.colliderect(shot.rect,badguy_4.rect):
                badguy_4.die(deadmen)
                game_time += 3
                break
            if pygame.Rect.colliderect(shot.rect,badguy_5.rect):
                badguy_5.die(deadmen)
                game_time += 3
                break
            if pygame.Rect.colliderect(shot.rect,badguy_6.rect):
                badguy_6.die(deadmen)
                game_time += 3
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

        # Increase Time for text
        game_time -= 1/60
        # Increase Time fot title
        title_time += 1
    #LEVEL 2
    elif level == 2:
        #start new walls for collisions
        walls = []
        #draw everything
        bg = Background_2 (WIDTH,HEIGHT,TILE_SIZE)
        bg.draw(screen)
        #bypass back to level 1
        if keys[pygame.K_i]:
            level = 1

    # Blit man image
    if reload_num >100 or shot_num >shot_max:
        man.draw(screen)
    else:
        # blit man reloading
        man.reload(screen)
        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()