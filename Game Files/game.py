import pygame
import math
from man import Man
from walls import Background
from gun import Gun, Reload, reload
from badguy import BadGuy
from walls2 import Background_2
from countdown import countdown
from time import time
from walls3 import Background_3

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
shot_max =12
deadmen = []
fail = 0
show_title = 1
title_time = 0
bg_alpha = 120
bg_alpha2 =120
title_alpha = 400
title_alpha2 =400
color = (0,0,0)
level= 1
badguys = []
badguys2 = []
reload_time = 90
level_2time = 0
level_3time =0
title_time_2 = 0

# Tiles
grass = pygame.image.load('PNG/Tiles/tile_01.png')
box = pygame.image.load('PNG/crateMetal.png')
box_scale = (box.get_width()*2,box.get_height()*2)
bigger_box = pygame.transform.scale(box,box_scale)
wood_floor = pygame.image.load('PNG/Tiles/tile_43.png')
bullet = pygame.image.load('PNG/bullet.png')

##################CHANGEABLES#####################
game_time = 80
shot_max =8
##################################################

#font
font = pygame.font.Font(None,42)

# THE MAN
man = Man(75,350)

# Sizes
TILE_SIZE = grass.get_width()



# Create initial background and wall collisions
bg = Background(WIDTH, HEIGHT,TILE_SIZE)
bg.draw(screen)
bg.create_wall_collisions()

#badguys
badguy_1 = BadGuy(375,290)
badguys.append(badguy_1)
badguy_2 = BadGuy(250,540)
badguys.append(badguy_2)
badguy_3 = BadGuy(635,125)
badguys.append(badguy_3)
badguy_4 = BadGuy(250,125)
badguys.append(badguy_4)
badguy_5 = BadGuy(740,250)
badguys.append(badguy_5)
badguy_6 = BadGuy(730,450)
badguys.append(badguy_6)
#Level 2 badguys
badguy_7 = BadGuy(340,120,2)
badguys2.append(badguy_7)
badguy_8 = BadGuy(225,85,2)
badguys2.append(badguy_8)
badguy_9 = BadGuy(635,250,2)
badguys2.append(badguy_9)
badguy_10 = BadGuy(450,200,2)
badguys2.append(badguy_10)
badguy_11= BadGuy(950,150,2)
badguys2.append(badguy_11)
badguy_12= BadGuy(730,480,2)
badguys2.append(badguy_12)
badguy_13= BadGuy(1050,350,2)
badguys2.append(badguy_13)
badguy_14= BadGuy(250,350,2)
badguys2.append(badguy_14)
#Osama 
badguy_15= BadGuy(250,350,3)


#MUSIC
bg_music = pygame.mixer.Sound('VTEMO - Drifting (freetouse.com).mp3')
bg_music.set_volume(0.5)
bg_music.play(-1)

##############     Run game loop    ###################
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

    #DRAW EVERYTHING
    screen.fill(color)

    # Draw time/win status
    if fail == 0:
        if man.x > 700 and man.y<200 and man.x<830 and len(deadmen) == 6 and fail ==0:
             text_surface = font.render("", True, (0,0,0))
             level = 2
        elif man.alive == 1:
            text_surface = font.render("", True, (0,0,0))
            fail = 1
        elif game_time > 1:
            text_surface = font.render(f"{int(game_time)}", True, (0,0,0))
        else:
            fail =1
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

    # Check for Shoot (space)
    flag_1 = False
    if keys[pygame.K_SPACE] and shot_num <shot_max and reload_num >100 and man.alive ==0:
        shot = Gun()
        bullets.append(shot)
        shot.shoot(man.x+15,man.y+15,man.angle,screen)
        shot_num = shot_num+1
        reload_num =0
        flag_1 = True

    ############          LEVEL 1           ############################
    if level == 1:
        #draw background
        bg.draw(screen)
        # Draw Title/alpha 
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
        
        #Make Collisions (smoother glide)
        for wall in bg.walls_y:
            if pygame.Rect.colliderect(man.rect, wall):
                man.x = pre_x
        for wall in bg.walls_x:
            if pygame.Rect.colliderect(man.rect, wall):
                man.y = pre_y
        for wall in bg.boxes:
            if pygame.Rect.colliderect(man.rect, wall):
                man.y = pre_y
                man.x = pre_x           
                
        # Badguys move around/blit 
        badguy_1.rove(550,400)
        badguy_2.rove(550,544)
        badguy_3.rove(640,700)
        badguy_4.rove(350,200)
        badguy_5.rove(870,280)
        badguy_6.rove(950,600)
        for dude in badguys:
            dude.draw(screen)

        #bypass level 1 -> level 2
        if keys[pygame.K_p]:
            level = 2
            game_time = 60
        #bypass level 1 -> level 3
        if keys[pygame.K_y]:
            level = 3

        # Check if Man Spotted (kill him/chase him)
        for dude in badguys:
            if pygame.Rect.colliderect(man.rect,dude.vision_rect):
                print('\n\n\n SPOTED \n\n\n')
                dude.shot_flag = 1
                dude.shoot(bg,man,man.x,man.y,screen,badguys)
            if dude.shot_flag != 0 and man.alive ==0 and (dude.double_tap_timer ==45 or dude.double_tap_timer == 90 or dude.double_tap_timer ==135 or dude.double_tap_timer ==180 or dude.double_tap_timer ==225):
                dude.shoot(bg,man,man.x,man.y,screen,badguys)
                print('double tap')
            if dude.shot_flag !=0 and man.alive ==0:
                dude.chase_x(man,bg.walls_x,bg.walls_y) 

    ##############       LEVEL 2       #################
    elif level == 2:
        #start new walls for collisions
        title_time_2 += 1
        level_2time +=0.01
        walls = []
        shot_max =shot_max+7
        while level_2time == 0.01:
            man.x = 840
            man.y = 120
            game_time = game_time+12
            man.angle = 180
            break
        #draw everything
        bg2 = Background_2 (WIDTH,HEIGHT,TILE_SIZE)
        bg2.draw(screen)

        # Draw Title/alpha 
        if title_time_2 < 120:
            title_surface = font.render("Killing Osama bin Laden: Level 2", True, (255,255,255))
            bg_alpha2 += 1
            title_alpha2 -= 4
            print('alpha shit')
        else:
            title_surface = font.render("", True, (0,0,0))
            title_alpha = 0
            bg_alpha2 = 254
        bg2.bg.set_alpha(bg_alpha2)
        title_surface.set_alpha(title_alpha2)
        title_rect = title_surface.get_rect(center=(WIDTH//2,HEIGHT//2))
        screen.blit(title_surface,title_rect)

        for wall in bg2.walls:
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

        for dude in badguys2:
            dude.draw(screen)

        # Check if Man Spotted (kill him)
        for dude in badguys2:
            if pygame.Rect.colliderect(man.rect,dude.vision_rect):
                print('\n\n\n SPOTED \n\n\n')
                dude.shot_flag = 1
                dude.shoot(bg2,man,man.x,man.y,screen,badguys2)
            if dude.shot_flag != 0 and man.alive ==0 and (dude.double_tap_timer ==45 or dude.double_tap_timer == 90 or dude.double_tap_timer ==135 or dude.double_tap_timer ==180 or dude.double_tap_timer ==225):
                dude.shoot(bg2,man,man.x,man.y,screen,badguys2)
                print('double tap')
            if dude.shot_flag !=0 and man.alive ==0:
                dude.chase_x(man,bg2.walls_x,bg2.walls_y)
    
        #bypass back to level 1
        if keys[pygame.K_i]:
            level = 1
        #bypass to level 3
        if keys[pygame.K_y]:
            level = 3
    #############        LEVEL 3         ######################
    elif level == 3:
        #start new walls for collisions
        shot_max =1
        level_3time +=0.01
        walls = []
        while level_3time == 0.01:
            man.x = 250
            man.y = 550
            game_time = game_time+12
            man.angle = 0
            break
        #draw everything
        bg3 = Background_3 (WIDTH,HEIGHT,TILE_SIZE)
        bg3.draw(screen)

        for wall in bg3.walls:
            if pygame.Rect.colliderect(man.rect, wall):
                man.x = pre_x
                man.y = pre_y

        badguy_15.draw(screen)
        #bypass level 3 -> level 1
        if keys[pygame.K_i]:
            level = 1

    # Fire the bullet
    while flag_1:
        # Draw Everything (#hatewhileloops)
        if level ==1:
            bg.draw(screen)
        if level ==2:
            bg2.draw(screen)
        shot.update(screen)
        man.reload(screen)
        
        # Blit Text
        screen.blit(text_surface,text_rect)
        screen.blit(text_surface_reload,text_rect_reload)
        # Check for bullet/wall collisons
        if level ==1:
            for wall in bg.walls:
                if pygame.Rect.colliderect(shot.rect, wall):
                    flag_1 = False
                    break
        if level ==2:
            for wall in bg2.walls:
                if pygame.Rect.colliderect(shot.rect, wall):
                    flag_1 = False
                    break
        # Check to see if bullet hit a bad guy
        if level == 1:
            for dude in badguys:
                dude.draw(screen)
                if pygame.Rect.colliderect(shot.rect,dude.rect):
                    dude.die(deadmen)
                    game_time += 3
                    flag_1 = False
                    break
        elif level == 2: 

            for dude in badguys2:
                dude.draw(screen)
                if pygame.Rect.colliderect(shot.rect,dude.rect):
                    dude.die(deadmen)
                    game_time += 3
                    flag_1 = False
                    break
                
        if shot.x > WIDTH or shot.x <0 or shot.y <0 or shot.y > HEIGHT:
            break
        pygame.display.flip()
        # Speed up display (bullet -> faster)
        clock.tick(600)
    # Draw Num Bullets left
    bullet_r = pygame.transform.rotozoom(bullet,0,0.02)
    bullet_num = shot_max-shot_num
    for x in range(15,15*bullet_num+15,15):
        screen.blit(bullet_r, (x,75))
    # reload bar
    reload_num += 1
    reload(man,reload_num,shot_num,shot_max,screen,reload_time)
    
    # Blit Text
    screen.blit(text_surface,text_rect)
    screen.blit(text_surface_reload,text_rect_reload)

    # Blit man image
    if reload_num >100 or shot_num >shot_max:
        man.draw(screen)
    else:
        # blit man reloading
        man.reload(screen)

    # Increase Time for text
    game_time -= 1/60
    # Increase Time fot title
    title_time += 1
        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()