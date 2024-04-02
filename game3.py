import pygame
from pygame.locals import *
import time
import random

#flat icon
# Set_Caption 
pygame.display.set_caption((" Moeed Rajpoot "))
clock=pygame.time.Clock()

Size=32
### Parent Class including start  Function and score display as well
#as Game Over function
class Game:
    def __init__(self):
        self.runing=True
        self.screenX=800
        self.screenY=600
        self.screen=pygame.display.set_mode((self.screenX,self.screenY))
        self.snake=Snake(self.screen,2)
        self.snake.Draw()
        self.apple=Apple(self.screen)
        self.level="easy"
        self.borderhard="easy"
        self.bgplay="play"
        self.apple.Draw()
        
        
# Check difficulty level for create border solid without showing 
    def bgstop(self):
        self.bgplay="stop"
        print("stop")
    def easy_level(self):
        self.level="easy"
        if self.level=="easy":
            self.snake.bordersolid="hard" 
    def hard_level(self):
        self.level="hard"
    
    # colision    Check snake and apple positions are matching or not
    def isMatch(self,x1,y1,x2,y2):
        if x1>=x2 and x1 < x2 + Size:
            if y1>=y2 and y1 < y2 + Size:
                return True
        return False
    
    def Score(self):
        pygame.font.init()
        scorecard=pygame.image.load("scorecard.png")
        self.screen.blit(scorecard,(300,-40))
        font=pygame.font.SysFont("timesnewroman",22,bold=True)
        score=font.render(f"Score:{self.snake.length}",True,(0,0,0))
        self.screen.blit(score,(360,13))
        

    def play(self):
        pygame.mixer.init()
        self.snake.snake_walking()
        # call the border functions
        if self.level=="hard":
            self.borders_none()
        elif self.level=="easy":
             self.solid_borders()
        self.apple.Draw()
        
        self.Score()
        pygame.display.flip()
        
        # increase length and score if snake and apple positions are same 
        
        if self.isMatch(self.snake.snake_positionX[0],self.snake.snake_positionY[0],self.apple.x,self.apple.y):
            sound=pygame.mixer.Sound("sound.mp3")
            pygame.mixer.Sound.play(sound)
            pygame.display.update()
            self.apple.move_apple()
            self.snake.increase_length()
        #Game Over if positions of snakes matches
        for i in range(3,self.snake.length):
             if self.isMatch(self.snake.snake_positionX[0],self.snake.snake_positionY[0],self.snake.snake_positionX[i],self.snake.snake_positionY[i]):
                 
                 self.Game_Over()
                 Start.runing=False
                 time.sleep(5)
                 self.runing=False
       
       
    #######   if Snake hit the border then Game will be Over
    def solid_borders(self):
        if self.snake.snake_positionX[0] > self.screenX or  self.snake.snake_positionX[0] < 0:
           self.Game_Over()
           
           time.sleep(5)
           self.runing=False
           
        if self.snake.snake_positionY[0] > self.screenY or  self.snake.snake_positionY[0] < 0:
            self.Game_Over()
            time.sleep(5)
            self.runing=False
                
    def borders_none(self):
        if self.snake.snake_positionX[0] > self.screenX :
            self.snake.snake_positionX[0]=0 
            
        elif  self.snake.snake_positionX[0] <= 0:
            self.snake.snake_positionX[0]=self.screenX
        
        if self.snake.snake_positionY[0] > self.screenY :
            self.snake.snake_positionY[0]=0
        elif  self.snake.snake_positionY[0] <= 0:
            self.snake.snake_positionY[0]=self.screenY

        
    def Game_Over(self):
       
        self.screen=pygame.display.set_mode((800,600))
        
        gameover=pygame.image.load("gameover.jpg")
        self.screen.blit(gameover,(0,0))
        
        card=pygame.image.load("lastcard.png")
        self.screen.blit(card,(200,20))
        font=pygame.font.SysFont("timesnewroman",40,bold=True)
        fontrender=font.render(f"Your Score is {self.snake.length}",True,(255,255,255))
        self.screen.blit(fontrender,(270,170))
        sound=pygame.mixer.Sound("over.mp3")
        pygame.mixer.Sound.play(sound)
        pygame.display.update()

    def bg_sound(self):
        if self.bgplay=="play":
             pygame.mixer.init()
             sound=pygame.mixer.Sound("bgsound.mp3")
             pygame.mixer.Sound.play(sound)
       
        
        
    
   
    def run(self):
        
        while self.runing:
            
            for i in pygame.event.get(): #Get Events
                if i.type==KEYDOWN:        
                    if i.key==K_UP:
                        self.snake.move_up()
                    if i.key==K_DOWN:
                        self.snake.move_down()
                    if i.key==K_RIGHT:
                        self.snake.move_right()
                    if i.key==K_LEFT:
                        self.snake.move_left()
                elif i.type==QUIT:
                    self.runing=False
                    
                    
                    
            ## Display Score 
            self.play()
            time.sleep(.1) 

# Draw  A Snake including Functionality
class Snake:
    def __init__(self,parent_screen,length):
        self.parent_screen=parent_screen
        self.length=length
        self.snake_icon=pygame.image.load("snake.png")
        self.bg=pygame.image.load("darkbg.png")  
        self.border_x=pygame.image.load("right.png")
        self.border_y=pygame.image.load("up.png")
        self.bordersolid="easy"
      
        self.snake_positionX=[Size]*length
        self.snake_positionY=[Size]*length
        self.direction="right"
   
# Game Border
    def game_border(self):
        self.parent_screen.blit(self.border_x,(-5,-600))
        self.parent_screen.blit(self.border_x,(-790,-600))
        self.parent_screen.blit(self.border_y,(-120,-400))
        self.parent_screen.blit(self.border_y,(-120,-985))
        
   
# Method of increase The Length  
    def increase_length(self):
         self.setlength=self.length-1
         self.x=self.snake_positionX[self.setlength]
         self.y=self.snake_positionY[self.setlength]
         self.length+=1
         self.snake_positionX.append(self.x)
         self.snake_positionY.append(self.y)

### Snake movement And walking Section  Starts including Draw function
 # i) set the direction of the snake 
    def move_up(self):
        self.direction='up'
    def move_down(self):
        self.direction="down"
    def move_right(self):
        self.direction="right"
    def move_left(self):
        self.direction="left"
    #ii) snake walking function
    def snake_walking(self):
        for i in range(self.length-1,0,-1):
            self.snake_positionX[i]=self.snake_positionX[i-1]
            self.snake_positionY[i]=self.snake_positionY[i-1]

        if self.direction=="up":
            self.snake_positionY[0] -=Size
        if self.direction=="down":
            self.snake_positionY[0] +=Size
        if self.direction=="right":
            self.snake_positionX[0] +=Size
        if self.direction=="left":
            self.snake_positionX[0] -=Size
        self.Draw()
        
        
     
    def Draw(self):    
        self.parent_screen.blit(self.bg,(0,0))
        # If The Option Hard Selected then Border will display
        if self.bordersolid=="hard":

            self.game_border()
        

        for i in range(self.length):
             self.parent_screen.blit(self.snake_icon,(self.snake_positionX[i],self.snake_positionY[i]))
             
        pygame.display.flip()

# Start Apple Section
class Apple:
    
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.img=pygame.image.load("apple.png")
       
        self.x=Size*3
        self.y=Size*3

    def move_apple(self):
        self.x=random.randint(0,20)*Size
        self.y=random.randint(0,15)*Size

    
    def Draw(self):  
        self.parent_screen.blit(self.img,(self.x,self.y))
        pygame.display.flip()
#############################################################   
Start=Game()
 
#####################################################################

            #  Front Page And Buttons 
class Buttons(Game,Snake,Apple):
    def __init__(self,):
        self.image=pygame.image.load("redbtn.png")
        self.b2=pygame.image.load("greenbtn.png")
        self.main=pygame.display.set_mode((800,600))
        self.greentext=pygame.image.load("easy.png")
        self.redtext=pygame.image.load("hard.png")
        self.front=pygame.image.load("darkbg.png")
       
        self.posiX=400
        self.posiY=-13
        self.b2x=30
        self.b2y=-10
        self.runing=Game
        self.clicked=False
    # Sound Per Click Function
    def click_sound(self):
        pygame.mixer.init()
        sound=pygame.mixer.Sound("click.mp3")
        pygame.mixer.Sound.play(sound)
    
    


   # Main Game Run Function with Buttons
    def draw(self):
        self.main.fill((122,125,123))
        self.main.blit(self.front,(0,0))
        self.rect2=self.main.blit(self.b2,(self.b2x,self.b2y))
        self.rect=self.main.blit(self.image,(self.posiX,self.posiY))
        self.main.blit(self.greentext,(30,130))
        self.main.blit(self.redtext,(350,130))
        
        pygame.display.update()
        # Get Position of the mouse
        pos=pygame.mouse.get_pos()
        # First Button
        if self.rect.collidepoint(pos):
               if pygame.mouse.get_pressed()[0]==1:
                  
                  self.click_sound()   
                  self.clicked=True
                  Start.easy_level()
                  
                  Start.run()  
           
        # Second Button
        if self.rect2.collidepoint(pos):
               if pygame.mouse.get_pressed()[0]==1:
                  
                  self.click_sound()
                  self.clicked=True
                  
                  
                  Start.hard_level()
                  Start.run()    
    # Front Page
    def Front(self):
        self.screen=pygame.display.set_mode((800,600))
        front=pygame.image.load("landingpage.jpg")
        self.screen.blit(front,(0,0))
        Start.bg_sound()
        pygame.display.update()  


    def runs(self):
        self.Front()
        
        time.sleep(3)
        while self.runing:
            for i in pygame.event.get():
                if i.type==QUIT:
                    self.runing=False 
                    Start.runing=False
                    
            self.draw()
            
# game.run()
btn=Buttons()
btn.runs()