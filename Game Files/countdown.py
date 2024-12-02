import pygame

def countdown(screen,font,game_time,deadmen,man):     
    if man.x > 700 and man.y<200 and man.x<830 and len(deadmen) == 6 and fail ==0:
        text_surface = font.render("", True, (0,0,0))
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
    else:
        text_surface = font.render("", True, (0,0,0))
    text_rect = text_surface.get_rect(center=(652,30))
    screen.blit(text_surface,text_rect)
    game_time -= 1/60



def reload(man,reload_num,shot_num,shot_max,screen,time):
    if shot_num <shot_max:
        reload_0 = Reload(20,30,screen)
        reload_0.box()
        if reload_num ==0:
            man.reload(screen)
        if reload_num >time/6:
            reload_1 = Reload(20,50,screen)
            reload_1.fill()
        if reload_num >2*time/6:
            reload_2 = Reload(40,50,screen)
            reload_2.fill()
        if reload_num >3*time/6:
            reload_3 = Reload(60,50,screen)
            reload_3.fill()
        if reload_num >4*time/6:
            reload_4 = Reload(80,50,screen)
            reload_4.fill()
        if reload_num >5*time/6:
            reload_5 = Reload(100,50,screen)
            reload_5.fill()
        if reload_num >time:
            reload_6 = Reload(120,50,screen)
            reload_6.fill()
            man.reloading = False