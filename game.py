import pygame
import time
import random

pygame.init()
gray=(71,71,71)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
display_width=800
display_height=600


gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("kiasutok")
clock=pygame.time.Clock()
carimg=pygame.image.load('assets\\car.png')
backgroundpic=pygame.image.load("assets\\grass.png")
yellow_strip=pygame.image.load("assets\\road.png")
strip=pygame.image.load("assets\\strip.png")
intro_background=pygame.image.load("assets\\loadingscrren.png")
instruction_background=pygame.image.load("assets\\loadingscrren.png")
car_width=56
pause=False

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("Kis Autók",largetext)
        TextRect.center=(400,100)
        gamedisplays.blit(TextSurf,TextRect)
        button("Indít",150,520,100,50,green,bright_green,"play")
        button("Kilép",550,520,100,50,red,bright_red,"quit")
        button("Súgó",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)



def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("Kerüld ki a szembe jövő kocsikat és vigyázz ki ne menj a pályáról!",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("Súgó",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("Bal nyíl : Bal",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("Jobb nyíl : Jobb" ,smalltext)
        hTextRect.center=((150),(450))
        ptextSurf,ptextRect=text_objects("P : Megállítás  ",smalltext)
        ptextRect.center=((150),(350))
        sTextSurf,sTextRect=text_objects("Irányítás",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(ptextSurf,ptextRect)
        button("Vissza",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("Megállítva",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("Folytatás",150,450,150,50,green,bright_green,"unpause")
            button("Újraindítás",350,450,150,50,blue,bright_blue,"play")
            button("Főmenü",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)
def indul():
    indul=True

    while indul:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            game_loop()

def unpaused():
    global pause
    pause=False

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                indul()
            elif action=="quit":
                pygame.quit()
                quit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)


def alap():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplays.blit(carimg,(x,y))
    score=font.render("SCORE: 0",True,black)
    gamedisplays.blit(score,(0,30))
    button("Megáll",650,0,150,50,red,bright_red,"pause")

def obstacle(obs_startx,obs_starty,obs,):
    if obs==0:
        obs_pic=pygame.image.load("assets\\enemy.png")
    else:
        obs_pic=pygame.image.load("assets\\enemy2.png")
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))
    pygame.display.update()

def score_system(passed,score):
    font=pygame.font.SysFont(None, 25)
    text=font.render("Passed: "+str(passed),True,black)
    score=font.render("Score: "+str(score),True,black)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))


def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()


def crash():
    message_display("Ütköztél")

def car(x,y):
    gamedisplays.blit(carimg,(x,y))

def game_loop():
    global pause
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=0
    score=0
    y2=7
    fps=144

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
                if event.key==pygame.K_a:
                    obstacle_speed+=2
                if event.key==pygame.K_b:
                    obstacle_speed-=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        pause=True
        gamedisplays.fill(gray)

        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(700,rel_y-backgroundpic.get_rect().width))
        if rel_y<800:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(700,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y+100))
            gamedisplays.blit(yellow_strip,(400,rel_y+200))
            gamedisplays.blit(yellow_strip,(400,rel_y+300))
            gamedisplays.blit(yellow_strip,(400,rel_y+400))
            gamedisplays.blit(yellow_strip,(400,rel_y+500))
            gamedisplays.blit(yellow_strip,(400,rel_y-100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))

        y2+=obstacle_speed

        obs_starty -= (obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty += obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x>690-car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level=level+1
                obstacle_speed+=1
                largetext=pygame.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_objects("Level"+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)


        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
        button("Pause",650,0,150,50,red,bright_red,"pause")
        pygame.display.update()
        clock.tick(60)

intro_loop()
game_loop()
pygame.quit()
quit()