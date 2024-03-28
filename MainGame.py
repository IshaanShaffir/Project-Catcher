import pygame
from pygame.locals import *
import os
from pygame import mixer
from tkinter import *
import random 
# Game Initialization
pygame.init()
from tkinter import *
from tkinter import ttk
import mysql.connector as mycon
con = mycon.connect(host='localhost',user='root',passwd='arib',database='recordb')
cur = con.cursor()

 
def popup():
        
        root1 = Tk()
        root1.title("idk2")
        root1.geometry("500x600")
        count1=0

        def add_record1():
                
                 A=[] 
                 a=name_box1.get()
                 b=score1.get()
                 c = random.randint(0,100000)
                 Z=[a]
                 if str(b).isalpha()==True:
                         
                         root2 = Tk()
                         root2.title("idk23")
                         root2.geometry("400x200")
                         label1 = Label(root2, text = "CANNOT ENTER ALPHABETS",bd = 100, font = "Castellar")
                         label1.pack()
                         root2.mainloop()
                         
                         pass
                  
                 if int(b) > 20:
                         
                         root42 = Tk()
                         root42.title("idk23")
                         root42.geometry("400x200")
                         label13 = Label(root42, text = "CANNOT BE MORE THAN 20",bd = 100, font = "Castellar")
                         label13.pack()
                         root42.mainloop()

                         pass
                         
                 if str(a)=="" or str(a).isspace()==True: #not working
                         root3 = Tk()
                         root3.title("idk23")
                         root3.geometry("400x200")
                         label12 = Label(root3, text = "NAME CANNOT BE EMPTY",bd = 100, font = "Castellar")
                         label12.pack()
                         root3.mainloop()
                          

                         
                  
                         
                 else:
                         for i in range(0,1):
                                 A.append(a)
                                 A.append(b)
                                 A.append(c)
                         #try the above 
                         my_tree1.insert(parent='',index='end', text="", values=(name_box1.get(),score1.get(),c))
                         t1 = tuple(A)
                         entr = 'Insert into record(name,score,id) values(%s,%s,%s)'
                         cur.execute(entr,t1)
                         #to clear the boxes
                         name_box1.delete(0,END)
                         score1.delete(0,END)
                         con.commit()
                

         
                         
                  
     
        my_tree1 = ttk.Treeview(root1)
        add_frame1=Frame(root1)
        add_frame1.pack(pady=20)

        name_box1 = Entry(add_frame1)
        name_box1.grid(row=1,column=0)

        score1 = Entry(add_frame1)
        score1.grid(row=1,column=1)

         

         

        nl1 = Label(add_frame1, text="Name")
        nl1.grid(row=0,column=0)

        il1 = Label(add_frame1, text="Score")
        il1.grid(row=0, column=1)

         

        
        add_record1 = Button(root1, text="Add Record", command=add_record1)
        add_record1.pack(pady=20)
        
 

def update_name_window():
        root1 = Tk()
        root1.title("idk2")
        root1.geometry("200x300")
        add_frame1=Frame(root1)
        add_frame1.pack(pady=20)
        prompt0= Label(add_frame1, text='Enter game id')
        prompt0.grid(row=200, column=0)

        user_id=Entry(add_frame1)
        user_id.grid(row=250, column=0)
        c=user_id.get()

        prompt= Label(add_frame1, text='Enter the new username')
        prompt.grid(row=100,column=0)
        new_name = Entry(add_frame1)
        new_name.grid(row=150,column=0)
        user_new=new_name.get()
        update_record = Button(root1, text="update record", command=update_name)
        update_record.pack(pady=20)  
        
        def update_name():
                
                A1=[]
                for i in range(0,1):
                    A1.append(user_new)
                    A1.append(c)        
                up = 'Update record set name = %s where id = %s'
                 
                t11 = tuple(A1)
                cur.execute(up,t11)
                con.commit()
                
                 

        
 
def admin():
         


        root = Tk()
        root.title("idk")
        root.geometry("500x600")

        my_tree = ttk.Treeview(root)

        #define our coloumns
        my_tree['columns'] =("Name" ,"GAME SCORE", "ID")

        #Format our coloumns
        my_tree.column("#0",width=0,minwidth=2)
        my_tree.column("Name",anchor=W,width=100)
        my_tree.column("GAME SCORE",anchor=CENTER,width=100)
        my_tree.column("ID",anchor=E,width=140)
        


        add_frame=Frame(root)
        add_frame.pack(pady=20)

        nl = Label(add_frame, text="Name")
        nl.grid(row=0,column=0)

       

        tl = Label(add_frame, text="Game Score")
        tl.grid(row=0,column=1)

        
        
        def add_record():
                
            global count
            
    
             
            #to clear the boxes
            A=[] 
            a=name_box.get()
            b=game_score.get()
            c=random.randint(0,888888)
            if str(b).isalpha()== True:
                         
                         root2 = Tk()
                         root2.title("idk23")
                         root2.geometry("400x200")
                         label1 = Label(root2, text = "CANNOT ENTER ALPHABETS",bd = 100, font = "Castellar")
                         label1.pack()
                         root2.mainloop()
                         
                         pass
            if str(b)=="" or str(b).isspace()==True:
                         root34 = Tk()
                         root34.title("idk23")
                         root34.geometry("400x200")
                         label121 = Label(root34, text = "SCORE CANNOT BE EMPTY",bd = 100, font = "Castellar")
                         label121.pack()
                         root34.mainloop()
                         pass
            if int(b) >20:
                         
                         root42 = Tk()
                         root42.title("idk23")
                         root42.geometry("400x200")
                         label13 = Label(root42, text = "SCORE CANNOT BE MORE THAN 20",bd = 100, font = "Castellar")
                         label13.pack()
                         root42.mainloop()

                         pass
                         
            if str(a)=="" or str(a).isspace()==True: #not working
                         root3 = Tk()
                         root3.title("idk23")
                         root3.geometry("400x200")
                         label12 = Label(root3, text = "NAME CANNOT BE EMPTY",bd = 100, font = "Castellar")
                         label12.pack()
                         root3.mainloop()
             
                    
            else:
                         for i in range(0,1):
                                 
                                        A.append(a)
                                        A.append(b)
                                        A.append(c)
                         #try the above 
                         my_tree.insert(parent='',index='end', text="", values=(name_box.get(),game_score.get(),c))
                         t1 = tuple(A)
                         entr = 'Insert into record(name,score,id) values(%s,%s,%s)'
                         cur.execute(entr,t1)
                         #to clear the boxes
                         name_box.delete(0,END)
                         game_score.delete(0,END)
                         con.commit()
                         name_box.delete(0,END)
                        
                         game_score.delete(0,END)

        def remove_all():
                cur.execute('delete from record')
                
                for record in my_tree.get_children():
                        my_tree.delete(record)
                con.commit()

        update_record = Button(root, text="Update Record", command=update_name_window)
        update_record.pack(pady=20)
        
         
        

         

 
        name_box = Entry(add_frame)
        name_box.grid(row=1,column=0)

        game_score = Entry(add_frame)
        game_score.grid(row=1,column=1)



        add_record = Button(root, text="Add Record", command=add_record)
        add_record.pack(pady=20)

         
 
        #create headings
        my_tree.heading("#0",text="",)
        my_tree.heading("Name",text="Name",anchor=W)
        my_tree.heading("GAME SCORE",text="GAME SCORE",anchor=CENTER)
        my_tree.heading("ID",text="ID",anchor=E)
        
        cur.execute('select * from record')
        data = cur.fetchall()
        global count
        count = 0
        for record in data:
            my_tree.insert(parent='',index='end',iid=count, text="", values=(record[0],record[1],record[2]))
            count+=1
        
        #reomve all

        remove_all = Button(root,text="Remove all records" ,command=remove_all)
        remove_all.pack(pady=10)

        #update

         

 
        #pack to the screen
        my_tree.pack(pady=20)
        root.mainloop()
 
        
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
def game():
    import math
    import pygame
    import sys
    import os
    import random
    pygame.init()
    popup()
      
    
    
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Hungry Bird')
    icon = pygame.image.load('in.png')
    pygame.display.set_icon(icon)
    bg = pygame.image.load('rainforest.png')
    bg_sound = mixer.music.load("ambience.wav")
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
        x_z.append(random.randint(1,2))
        y_z.append(random.randint(1,2))
    def enemy(x,y,i):
        screen.blit(enemyimg[i],(x,y))
     
    def isCollision(enemyx,enemyy,playerx,playery,i):
        distance = math.sqrt((math.pow(enemyx[i]-playerx,2))+(math.pow(enemyy[i]-playery+5,2)))
        if distance<30:
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
                      x_z[i] = 1
                  elif enemyx[i] >=  736: #Taking size of img in mind
                      x_z[i] = -1
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
                        popup()
                        
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
con.commit()
pygame.quit()
quit()

