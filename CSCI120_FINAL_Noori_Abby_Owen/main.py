#SMALL FUNNY PET GAME
import pygame, sys, random
from button import Button
from healthbar_class import Health
from animation_class import movement
import os
#The Button, Health and Movement Classes are from other files within this folder
'''Small Funny Pet! Game by Owen Nasi, Noori Tween and Abby Wilkes: Main File'''

pygame.init()
# this intitializes pygame to use the internal functions throughout the code

clock = pygame.time.Clock() 
#creates a clock function that allows for frames to change throughout running

# defining width and length variables
win_w = 500 # window width (x)
win_h = 500 # window height (y)
button_w = 100 # button width (x)
button_h = 45 # button height (y)
sand_h = 60 # sand height (y)
sand_w = 90 # sand width (x)
exit_w = 100 # exit button width (x)
exit_h= 50 # exit button height (y)
pop_w = 300 # pop up button width (x)
pop_h = 200 # pop up button height (y)

#establishes the postion of the pet as the character and where it is within the screen
character1_w = 150 # character width (x)
character1_h = 150 # character height (y)
character1_pos_x, character1_pos_y = 175, 270 # character x and y position

# defining colors
FORESTGREEN = (34, 139, 34) # forest green color code
LIGHTGREEN = (144, 238, 144) # light green color code
BLACK = (0,0,0) # black color code
LIGHTGREY = (192,192,192) # light grey color code

# defining window with specific size determined by variables above
win = pygame.display.set_mode((win_w,win_h))

# defining images
background_image = pygame.transform.scale(pygame.image.load(os.path.join('images','background.png')),(win_w,win_h))
title_image = pygame.transform.scale(pygame.image.load(os.path.join('images','title2.png')),(300,70))

menu_image = pygame.transform.scale(pygame.image.load(os.path.join('images','menu.png')),(button_w,button_h))
menu2_image = pygame.transform.scale(pygame.image.load(os.path.join("images","menu2.png")),(button_w,button_h))

resume_image = pygame.transform.scale(pygame.image.load(os.path.join("images","resume2.png")),(button_w,button_h))
resume2_image = pygame.transform.scale(pygame.image.load(os.path.join("images","resume.png")),(button_w,button_h))

settings_image = pygame.transform.scale(pygame.image.load(os.path.join("images","settings.png")),(button_w,button_h))
settings2_image = pygame.transform.scale(pygame.image.load(os.path.join("images","settings2.png")),(button_w,button_h))

restart_image = pygame.transform.scale(pygame.image.load(os.path.join("images","restart.png")),(button_w,button_h))
restart2_image = pygame.transform.scale(pygame.image.load(os.path.join("images","restart2.png")),(button_w,button_h))

tutorial_image = pygame.transform.scale(pygame.image.load(os.path.join("images","tutorial.png")),(button_w,button_h))
tutorial2_image = pygame.transform.scale(pygame.image.load(os.path.join("images","tutorial2.png")),(button_w,button_h))

start_image = pygame.transform.scale(pygame.image.load(os.path.join("images","start2.png")),(button_w,button_h))
start2_image = pygame.transform.scale(pygame.image.load(os.path.join("images","start.png")),(button_w,button_h))

back_image = pygame.transform.scale(pygame.image.load(os.path.join("images","back.png")),(button_w,button_h))
back2_image = pygame.transform.scale(pygame.image.load(os.path.join("images","back2.png")),(button_w,button_h))

kitchen_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "cute_kitchen.png")), (500, 500))
park_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "park.png")), (500, 500))
hunger_image = pygame.transform.scale(pygame.image.load(os.path.join("images", "hungry_image.png")), (button_w, button_h))
sandwich = pygame.transform.scale(pygame.image.load(os.path.join("images","sandwich_eat.png")), (sand_w, sand_h))
CUTEsandwich = pygame.transform.scale(pygame.image.load(os.path.join("images", "sandwich_eat_fade.png")), (sand_w, sand_h))
TOXICsandwich = pygame.transform.scale(pygame.image.load(os.path.join("images", "sandwich_eat_glow.png")), (sand_w, sand_h))
ball = pygame.transform.scale(pygame.image.load(os.path.join('images','ball_play.png')),(button_w,button_h))
GLOWball =pygame.transform.scale(pygame.image.load(os.path.join('images','ball_playglow.png')),(button_w,button_h))

exit_sign = pygame.transform.scale(pygame.image.load(os.path.join("images", "exit_sign.png")), (exit_w, exit_h))
exit_sign_glow = pygame.transform.scale(pygame.image.load(os.path.join("images", "exit_sign_glow2.png")), (exit_w, exit_h))
pop_up_sign = pygame.transform.scale(pygame.image.load(os.path.join("images", "POPname.png")), (pop_w, pop_h))

hunger_image = pygame.transform.scale(pygame.image.load(os.path.join("images","hunger.png")),(button_w,button_h))
boredom_image = pygame.transform.scale(pygame.image.load(os.path.join("images","boredom.png")),(button_w,button_h))
energy_image = pygame.transform.scale(pygame.image.load(os.path.join("images","energy.png")),(button_w,button_h))
heart_image = pygame.transform.scale(pygame.image.load(os.path.join("images","heart.PNG")),(button_w,button_h))

play_image = pygame.transform.scale(pygame.image.load(os.path.join('images','play.png')),(button_w,button_h))
play2_image = pygame.transform.scale(pygame.image.load(os.path.join('images','play2.png')),(button_w,button_h))
sleep_image = pygame.transform.scale(pygame.image.load(os.path.join('images','sleep.png')),(button_w,button_h))
sleep2_image = pygame.transform.scale(pygame.image.load(os.path.join('images','sleep2.png')),(button_w,button_h))
feed_image = pygame.transform.scale(pygame.image.load(os.path.join('images','feed.png')),(button_w,button_h))
feed2_image = pygame.transform.scale(pygame.image.load(os.path.join('images','feed2.png')),(button_w,button_h))

tut_image = pygame.transform.scale(pygame.image.load(os.path.join("images","tut.png")),(win_w,win_h))
about_image = pygame.transform.scale(pygame.image.load(os.path.join("images","about.png")),(win_w,win_h))
sleepy_bgimage = pygame.transform.scale(pygame.image.load(os.path.join("images","sleepy_bg.png")),(win_w,win_h))
image_sleep = pygame.transform.scale(pygame.image.load(os.path.join("images","1sleep_3.png")),(win_w,win_h))

character1_image = pygame.transform.scale(pygame.image.load(os.path.join("images","image.png")),(character1_w,character1_h))

#variable that is a list that is storing the name used in play()
friend_namelist = []

#total health defined
total_health = 150

# defining health status bars
HungerStatus = Health(120,20,total_health,10,total_health,total_health)
SleepStatus = Health(120,70,total_health,10,total_health,total_health)
BoredomStatus = Health(120,120,total_health,10,total_health,total_health)


def popup():
    '''This is used to prompt the user to create a username rather than happen in the terminal 
    but it does not appear to be working yet'''
    input_rect = pygame.Rect(200, 200, 110, 25)
    color = pygame.Color('lightskyblue3')
    base_font = pygame.font.Font(None, 32)
    user_text = '' #essentially friend_name,, we cna use this to append to friend_namelist
    active = False
    while True:
        """here i will put the pop up"""
        pygame.display.set_caption("Enter Friend's Name")

        POPUP_MOUSE_POS = pygame.mouse.get_pos()

        win.blit(background_image, (0,0))
        win.blit(pop_up_sign, (100, 120))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(POPUP_MOUSE_POS):
                    active = True
                else:
                    active = False
        if active:
            if event.type == pygame.KEYDOWN:
                input += friend_name
            if event.type == pygame.K_BACKSPACE:
                friend_name = friend_name[:-1]
            if event.type == pygame.K_KP_ENTER or pygame.K_RETURN:
                    friend_namelist.append(friend_name)
                    play2()
        else:
            if len(friend_namelist) == 1:
                play2()
                #         friend_namelist.append(friend_name)
                
               


        
        pygame.draw.rect(win, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        win.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()

def play():
    '''This function creates the option to play the game from the menu. This 
    then allows for the frame to change to show the pet and allow the user to play. 
    It provides the options to go back and then play once the user enters a name in the 
    terminal'''
    while True:
        pygame.display.set_caption("Play Menu")

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        font = pygame.font.Font(os.path.join("images", "Minecraft.ttf"), 30)
        font2 = pygame.font.Font(os.path.join("images", "Minecraft.ttf"), 22)
        
        play1_text1 = font.render('Welcome to our game!', True, BLACK)
        playtextRect1 = play1_text1.get_rect()
        playtextRect1.center = (win_w // 2, 200)

        play1_text2 = font2.render('Please click START then input your friends', True, BLACK)
        playtextRect2 = play1_text2.get_rect()
        playtextRect2.center = (win_w // 2, 250)

        play1_text3 = font2.render('name in your terminal and hit enter!', True, BLACK)
        playtextRect3 = play1_text3.get_rect()
        playtextRect3.center = (win_w // 2, 275)
                 
        win.blit(background_image, (0,0))
        win.blit(play1_text1, playtextRect1)
        win.blit(play1_text2, playtextRect2)
        win.blit(play1_text3, playtextRect3)

        # this win.blit could be used to write / present what is on this screen - win.blit(next_image,(100,100))

        back_tomenu_button = Button(x_pos=(200), y_pos=(425), button_w = button_w , button_h = button_h, base_image=back_image, hovering_image=back2_image)
        play_button = Button(x_pos=(200), y_pos=(325), button_w = button_w , button_h = button_h, base_image=start_image, hovering_image=start2_image)

        for button in [back_tomenu_button, play_button]:#, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS,win,button_w,button_h)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_tomenu_button.checkForInput(PLAY_MOUSE_POS,button_w, button_h):
                    main_menu()

                if event.type == pygame.MOUSEBUTTONDOWN:
        
            
                 if play_button.checkForInput(PLAY_MOUSE_POS,button_w, button_h):
                    #  popup()
                    friend_name = str(input("Please input your friend's name here: "))
                    friend_namelist.append(friend_name)
                    if len(friend_namelist) == 1:
                            play2()

        pygame.display.flip() #Refresh on-screen display
        clock.tick(60)

        pygame.display.flip() #Refresh on-screen display
        clock.tick(60)

def play2():
    '''This is the main play page which has the health bars and the interaction buttons.
     When these buttons are pressed on this page, it takes the user to a different pages, 
    and the health levels are restored when returned. '''
    
    global HungerStatus 
    global SleepStatus 
    global BoredomStatus 

    while True:
        pygame.display.set_caption(f"{friend_namelist[0]} World")

        PLAY2_MOUSE_POS = pygame.mouse.get_pos() # used for clicking + knowing where the mouse is

        font = pygame.font.Font(os.path.join("images", "Minecraft.ttf"), 20)
        play2_text1 = font.render(f'{friend_namelist[0]}', True, BLACK)
        play2textRect1 = play2_text1.get_rect()
        play2textRect1.center = (win_w // 2, character1_pos_y-20)

        win.blit(background_image, (0,0))
        win.blit(character1_image, (character1_pos_x, character1_pos_y))
        win.blit(play2_text1, play2textRect1)
        win.blit(hunger_image, (10,10))
        win.blit(boredom_image, (10,60))
        win.blit(energy_image, (10,110))


        character_butt = Button(x_pos=character1_pos_x, y_pos=character1_pos_y, button_w = character1_w, button_h = character1_h, base_image=character1_image, hovering_image=character1_image)
        feed_button = Button(x_pos=10, y_pos=240, button_w = button_w, button_h = button_h, base_image=feed_image, hovering_image=feed2_image)
        sleep_button = Button(x_pos=10, y_pos=290, button_w = button_w, button_h = button_h, base_image=sleep_image, hovering_image=sleep2_image)
        play_button = Button(x_pos=10,y_pos=340, button_w = button_w, button_h = button_h, base_image=play_image, hovering_image=play2_image)

        for button in [character_butt,feed_button,sleep_button,play_button]:#, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(PLAY2_MOUSE_POS,win,button_w,button_h)

        HungerStatus.health(win)
        SleepStatus.health(win)
        BoredomStatus.health(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if character_butt.checkForInput(PLAY2_MOUSE_POS,character1_w, character1_h):
                    print(f'My name is {friend_namelist[0]}!!!')
                if feed_button.checkForInput(PLAY2_MOUSE_POS,button_w, button_h):
                    feed()
                if sleep_button.checkForInput(PLAY2_MOUSE_POS,button_w,button_h):
                    sleepy()
                if play_button.checkForInput(PLAY2_MOUSE_POS,button_w, button_h):
                    play_time()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    HungerStatus.gain(25) # increment of health increase every time up pressed
                    #print(HungerStatus.current_health) 
                    '''use this above variable to change what comes up!!!'''
                    '''HungerStatus.current_health = variable but diff for diff values'''
                    # momentary button vs toggle button
                if event.key == pygame.K_a:
                    HungerStatus.loss(25)
                if event.key == pygame.K_w:
                    SleepStatus.gain(25) # increment of health increase every time up pressed
                if event.key == pygame.K_s:
                    SleepStatus.loss(25)
                if event.key == pygame.K_e:
                    BoredomStatus.gain(25) # increment of health increase every time up pressed
                if event.key == pygame.K_d:
                    BoredomStatus.loss(25)
        pygame.display.flip() #Refresh on-screen display
        clock.tick(60)

def settings():
    '''This allows the user to go to the settings page which provides credits and a QR 
    code that can be scanned and explains the sources used in the code.'''
    while True:
        pygame.display.set_caption("Settings Menu")

        SETTINGS_MOUSE_POS = pygame.mouse.get_pos()

        win.blit(about_image, (0,0))

        back_tomenu_button = Button(x_pos=(200), y_pos=(425), button_w = button_w , button_h = button_h, base_image=back_image, hovering_image=back2_image)
        for button in [back_tomenu_button]:
            button.changeColor(SETTINGS_MOUSE_POS,win,button_w,button_h)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_tomenu_button.checkForInput(SETTINGS_MOUSE_POS,button_w, button_h):
                    main_menu()
        pygame.display.flip()
        clock.tick(60)

def tutorial():
    '''This allows the user to go to the tutorial page which provides information on 
    how the game is played and how the statuses are measured.'''
    while True:
        pygame.display.set_caption("Tutorial Menu")

        PLAY_TUTORIAL_POS = pygame.mouse.get_pos()

        win.blit(tut_image, (0,0))

        back_tomenu_button = Button(x_pos=(200), y_pos=(445), button_w = button_w , button_h = button_h, base_image=back_image, hovering_image=back2_image)
        
        for button in [back_tomenu_button]:
            button.changeColor(PLAY_TUTORIAL_POS,win,button_w,button_h)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_tomenu_button.checkForInput(PLAY_TUTORIAL_POS,button_w, button_h):
                    main_menu()

        pygame.display.flip()
        clock.tick(60)

def main_menu():
    '''This is the beginning page when the code is run and it allows the user to choose between 
    the settings, tutorial and play option pages.'''
    while True:
        pygame.display.set_caption("Main Menu")

        win.blit(background_image, (0, 0))
        win.blit(title_image,(100,60))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # defining buttons
        play_button = Button(x_pos=(200), y_pos=(175), button_w = button_w , button_h= button_h, base_image=start_image, hovering_image=start2_image)
        settings_button = Button(x_pos=(200), y_pos=(250), button_w = button_w , button_h= button_h, base_image=settings_image, hovering_image=settings2_image)
        tutorial_button = Button(x_pos=(200), y_pos=(325), button_w = button_w , button_h= button_h, base_image=tutorial_image, hovering_image=tutorial2_image)

        for button in [play_button, settings_button, tutorial_button]: # add the different buttons here
            button.changeColor(MENU_MOUSE_POS,win,button_w,button_h)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(MENU_MOUSE_POS, button_w, button_h):
                    play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settings_button.checkForInput(MENU_MOUSE_POS, button_w, button_h):
                    settings()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tutorial_button.checkForInput(MENU_MOUSE_POS, button_w, button_h):
                    tutorial()

                '''following two commands would close the code'''
                    # pygame.quit()
                    # sys.exit()
        pygame.display.flip() #Refresh on-screen display
        clock.tick(60)
        #pygame.display.update()

def feed():
    '''This function opens up a page that shows the pet and allows a sandwich to be 
    shown up randomly on the screen to be clicked to feed the pet. When clicking the exit button, 
    the hunger status is replenished.'''
    startx = random.randint(0, win_w -10)
    starty = random.randint(0, win_h - 10)
    while True:
        pygame.display.set_caption(f"{friend_namelist[0]}'s Hungry")
        FEED_MOUSE_POS = pygame.mouse.get_pos()

        character1_pos_x = 200
        character1_pos_y = 330

        win.blit(kitchen_image, (0,0))
        win.blit(character1_image, (character1_pos_x, character1_pos_y))
        win.blit(sandwich, (startx, starty))

        sandwich_button = Button(x_pos=startx, y_pos=starty, button_h=sand_h, button_w=sand_w, base_image=sandwich, hovering_image=CUTEsandwich) 
        exit_button = Button(x_pos=(390), y_pos=(10), button_h=exit_h, button_w=exit_w, base_image=exit_sign, hovering_image=exit_sign_glow)
        for button in [sandwich_button, exit_button]:#, OPTIONS_BUTTON, QUIT_BUTTON]: character_butt,feed_button,sleep_button,play_button, 
            button.changeColor(FEED_MOUSE_POS,win,button_w,button_h)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.checkForInput(FEED_MOUSE_POS, button_w, button_h):
                    play2()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sandwich_button.checkForInput(FEED_MOUSE_POS, button_w, button_h):
                    feed()
                    """make conditional statememt that only allows you to eat 3 times before being full"""
                    # pygame.transform.scale(sandwich_button, (0,0))
            else:
                pass
        pygame.display.flip() #Refresh on-screen display
        clock.tick(60)

def sleepy():
    '''This function provides a connection from the play page to the sleeping page 
    which shows a nighttime background and the sleeping pet.  When clicking the exit button, 
    the energy status is replenished.'''
    while True:
        pygame.display.set_caption(f"{friend_namelist[0]}'s Sleepy!")
        SLEEP_MOUSE_POS = pygame.mouse.get_pos()

        image_sleep_pos_x = 200
        image_sleep_pos_y = 330

        win.blit(sleepy_bgimage, (0,0))
        win.blit(image_sleep, (image_sleep_pos_x, image_sleep_pos_y))

        exit_button = Button(x_pos=(390), y_pos=(10), button_h=exit_h, button_w=exit_w, base_image=exit_sign, hovering_image=exit_sign_glow)
        for button in [exit_button]:#, OPTIONS_BUTTON, QUIT_BUTTON]: character_butt,feed_button,sleep_button,play_button, 
            button.changeColor(SLEEP_MOUSE_POS,win,button_w,button_h)
                    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.checkForInput(SLEEP_MOUSE_POS, button_w, button_h):
                    play2()
            else:
                pass
        pygame.display.flip() #Refresh on-screen display
        clock.tick(60)

def play_time():
    '''This runs a similar function to the feed screen, but uses a ball instead of various foods 
    for the user to click on all over the screen'''
    startx = random.randint(0, win_w -10)
    starty = random.randint(0, win_h - 10)
    while True:
        pygame.display.set_caption(f"{friend_namelist[0]}'s Ready 2 Play")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        character1_pos_x = 200
        character1_pos_y = 330

        win.blit(park_image, (0,0))
        win.blit(character1_image, (character1_pos_x, character1_pos_y))
        win.blit(ball, (startx, starty))

        ball_button = Button(x_pos=startx, y_pos=starty, button_h=sand_h, button_w=sand_w, base_image=ball, hovering_image=GLOWball) 
        exit_button = Button(x_pos=(390), y_pos=(10), button_h=exit_h, button_w=exit_w, base_image=exit_sign, hovering_image=exit_sign_glow)
        for button in [ball_button, exit_button]:#, OPTIONS_BUTTON, QUIT_BUTTON]: character_butt,feed_button,sleep_button,play_button, 
            button.changeColor(PLAY_MOUSE_POS,win,button_w,button_h)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.checkForInput(PLAY_MOUSE_POS, button_w, button_h):
                    play2()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball_button.checkForInput(PLAY_MOUSE_POS, button_w, button_h):
                    play_time()
                    """make conditional statememt that only allows you to eat 3 times before being full"""
                    # pygame.transform.scale(ball_button, (0,0))
            else:
                pass
        pygame.display.flip() #Refresh on-screen display
        clock.tick(60)

main_menu() #runs the whole code
