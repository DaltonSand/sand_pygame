# Draw time/win status
def status(WIDTH,HEIGHT,fail,win,game_time,username,man,badguy_15,deadmen,font,font_v,bg,bg2,bg3):
    if fail == 0:
        if badguy_15.dead != 0:
            win = 1
            text_surface = font_v.render("VICTORY", True, (220,20,60))
            text_rect = text_surface.get_rect(center=(WIDTH/2,HEIGHT/2))
            color = (255, 215, 0)
            bg_alpha =120
            bg3.bg.set_alpha(bg_alpha)
            score = game_time
            # Record score
            while record:
                with open("scores.txt", "a") as file:
                    file.write(f"Username:{username} - {score}.\n")
                record = 0
        elif man.x <300 and man.y>400 and len (deadmen)==14 and level ==2:
            text_surface = font.render("", True, (0,0,0))
            level = 3
            text_rect = text_surface.get_rect(center=(652,30))
        elif man.x > 700 and man.y<200 and man.x<830 and len(deadmen) == 6 and fail ==0:
             text_surface = font.render("", True, (0,0,0))
             level = 2
             text_rect = text_surface.get_rect(center=(652,30))
        elif man.alive == 1:
            text_surface = font.render("", True, (0,0,0))
            fail = 1
            text_rect = text_surface.get_rect(center=(652,30))
        elif game_time > 1:
            text_surface = font.render(f"{int(game_time)}", True, (0,0,0))
            text_rect = text_surface.get_rect(center=(652,30))
        else:
            fail =1
    else:
        text_surface = font.render("FAIL", True, (225,225,225))
        text_rect = text_surface.get_rect(center=(WIDTH/2,HEIGHT/2))
        color = (138, 3, 3)
        bg_alpha =120
        bg.bg.set_alpha(bg_alpha)
        bg2.bg.set_alpha(bg_alpha)
        bg3.bg.set_alpha(bg_alpha)
        man.die()
    return text_surface, text_rect