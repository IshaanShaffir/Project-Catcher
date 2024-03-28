import pygame
from pygame.locals import *
import os
from pygame import mixer
from tkinter import *
# Game Initialization
pygame.init()
def admin():
    
    def register():
        global register_screen
        register_screen = Toplevel(main_screen)
        register_screen.title("Register")
        register_screen.geometry("300x250")
        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
        Label(register_screen, text="Please enter details below", bg="blue").pack()
        Label(register_screen, text="").pack()
        username_lable = Label(register_screen, text="Username * ")
        username_lable.pack()
        username_entry = Entry(register_screen, textvariable=username)
        username_entry.pack()
        password_lable = Label(register_screen, text="Password * ")
        password_lable.pack()
        password_entry = Entry(register_screen, textvariable=password, show='*')
        password_entry.pack()
        Label(register_screen, text="").pack()
        Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
    def login():
        global login_screen
        login_screen = Toplevel(main_screen)
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()

        global username_verify
        global password_verify
        username_verify = StringVar()
        password_verify = StringVar()
 
        global username_login_entry
        global password_login_entry
 
        Label(login_screen, text="Username * ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)
        username_login_entry.pack()
        Label(login_screen, text="").pack()
        Label(login_screen, text="Password * ").pack()
        password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
        password_login_entry.pack()
        Label(login_screen, text="").pack()
        Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

    def register_user():
        username_info = username.get()
        password_info = password.get()
 
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
 
        username_entry.delete(0, END)
        password_entry.delete(0, END)
 
        Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess()
 
            else:
                password_not_recognised()
 
        else:
            user_not_found()
        
    def login_sucess():
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=delete_login_success).pack()
    def password_not_recognised():
        global login_success_screen
        login_success_screen = Toplevel(login_screen)
        login_success_screen.title("Success")
        login_success_screen.geometry("150x100")
        Label(login_success_screen, text="Login Success").pack()
        Button(login_success_screen, text="OK", command=delete_login_success).pack()
    def user_not_found():
        global user_not_found_screen
        user_not_found_screen = Toplevel(login_screen)
        user_not_found_screen.title("Success")
        user_not_found_screen.geometry("150x100")
        Label(user_not_found_screen, text="User Not Found").pack()
        Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
    def delete_login_success():
        login_success_screen.destroy()
    def delete_password_not_recognised():
        password_not_recog_screen.destroy() 
    def delete_user_not_found_screen():
        user_not_found_screen.destroy()
    def main_account_screen():
        global main_screen
    def main_account_screen():
        global main_screen
        main_screen = Tk()
        main_screen.geometry("300x250")
        main_screen.title("Account Login")
        Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command = login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=register).pack()
        main_screen.mainloop() 
    main_account_screen()
    
        
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
def game():
    import math
    import pygame
    import sys
    import random
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Hungry Bird')
    icon = pygame.image.load('bird.png')
    pygame.display.set_icon(icon)
    bg = pygame.image.load('rainforest.png')
    bg_sound = mixer.music.load("foresta.wav")
    mixer.music.play(-1)
    score_value=0
    live=3
    font = pygame.font.Font("Retro.ttf",30)
    textx=10
    texty=10
    textx1 = 600
    texty1 = 10
    def scores(x,y):
        score = font.render("Score:" +str(score_value),True,(255,255,255))
        screen.blit(score,(x,y))
    def gameover():
        overfont=pygame.font.Font("Retro.ttf",100)
        over_text=overfont.render("GAME OVER",True,(255,0,0))
        screen.blit(over_text, (250, 250))

    def gamewon():
        wonfont=pygame.font.Font("Retro.ttf",100)
        won_text=wonfont.render("YOU WON!!", True,(255,0,0))
        screen.blit(won_text, (250, 250))

    def lives(x,y):
        life = font.render('Lives Left :' + str(live),True,(255,255,255))
        screen.blit(life,(x,y))    
    playerimg = pygame.image.load('doveR.png')
    playerx = 370
    playery = 480
    x_change = 0
    y_change = 0
    def player(x,y):
        screen.blit(playerimg,(x,y))
    enemyimg = []
    enemyx = []
    enemyy = []
    x_z = []
    y_z = []
    numenemy = random.randint(3,4)
    for i in range(numenemy):
        enemyimg.append(pygame.image.load('ladybugs.png'))
        enemyx.append(random.randint(10,730))
        enemyy.append(random.randint(20,100))
        x_z.append(random.randint(1,3))
        y_z.append(random.randint(1,3))
    def enemy(x,y,i):
        screen.blit(enemyimg[i],(x,y))
     
    def isCollision(enemyx,enemyy,playerx,playery,i):
        distance = math.sqrt((math.pow(enemyx[i]-playerx,2))+(math.pow(enemyy[i]-playery+5,2)))
        if distance<40:
            return True
        else:
            return False
    slashimg = pygame.image.load("45.png")
    def slash(x,y):
        screen.blit(slashimg,(x,y+10))
        
    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    running = False    
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT:
                     x_change = -5
                 if event.key == pygame.K_RIGHT:
                     x_change = 5
                 if event.key == pygame.K_UP:
                     y_change = -5
                 if event.key == pygame.K_DOWN:
                     y_change = 5
                 if event.key == pygame.K_KP0:
                     snd = mixer.Sound("gulp.mp3")
                     snd.play()
                     slash(playerx,playery)
                     for i in range(numenemy):
                        collision = isCollision(enemyx,enemyy,playerx,playery,i)
                        if collision:
                            score_value += 1 
                            enemyx[i] = random.randint(10,650)
                            enemyy[i] = random.randint(20,50) 
                            
                         
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP:
                    y_change = 0
                if event.key == pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_KP0:
                     
                    slash(playerx,playery)
                     
                    for i in range(numenemy):
                        collision = isCollision(enemyx,enemyy,playerx,playery,i)
                        if collision:
                            score_value += 1 
                            enemyx[i] = random.randint(10,650)
                            enemyy[i] = random.randint(20,50)
                            
        playerx = playerx + x_change
        playery = playery + y_change
        #GameOver initialized
        if live ==0:
            for j in range(numenemy):
                enemyy[j]=2000
            while live==0:
                playery= 2000
                playerx= 2000
                break
            gameover()
        if playerx <= 0:
            playerx = 0
        elif playerx >=  736: #Taking size of img in mind
            playerx = 736
        if playery <= 0:
            playery = 0
        elif playery >= 536:
            playery = 536    
        
        for i in range(numenemy):
                  enemyx[i] = enemyx[i] + x_z[i]
                  enemyy[i] = enemyy[i] + y_z[i]
                  if enemyx[i] <= 0:
                      x_z[i] = 3
                  elif enemyx[i] >=  736: #Taking size of img in mind
                      x_z[i] = -3
                  if enemyy[i] <= 0:
                      y_z[i] = 2
                  elif enemyy[i] >= 536 and enemyy[i]<=537:
                      live-=1



                  enemy(enemyx[i],enemyy[i],i) 
        player(playerx,playery)    
        
        scores(textx,texty)
        lives(textx1,texty1)
        # Initialises Gamewon
        if score_value==20:
            gamewon()
            for j in range(numenemy):
                enemyy[j]=2000
            while score_value>=0:
                playery= 2000
                playerx= 2000
                break

        pygame.display.update()




# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Font 
font = "Retro.ttf"


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():
    icon = pygame.image.load('book.png')
    pygame.display.set_icon(icon)

    menu=True
    selected="start"

    while menu:
        bgk = pygame.image.load('i01_bird.png')
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                    
                elif event.key==pygame.K_LEFT:
                    selected="admin"
                
                if event.key==pygame.K_RETURN:
                    if selected=="start":# here put game function
                        game()
                    if selected=="quit":
                        pygame.quit()
                        quit()
                    if selected=="admin":
                        admin()

        # Main Menu  
        screen.fill(blue)
        title=text_format("Hungry Bird", font, 90, yellow)
        if selected=="start":
            text_start=text_format("START", font, 75, white)
        else:
            text_start = text_format("START", font, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, white)
        else:
            text_quit = text_format("QUIT", font, 75, black)
        if selected=="admin":
            text_admin=text_format("ADMIN", font, 75, white)
        else:
            text_admin=text_format("ADMIN", font, 75, black)    
        


        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
        admin_rect=text_admin.get_rect()

        # Main Menu Text
        screen.blit(bgk,(0,0))
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        screen.blit(text_admin, (screen_width/2 - (admin_rect[2]/2), 420))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("WELCOME TO THE GAME")

#Initialize the Game
main_menu()
pygame.quit()
quit()

