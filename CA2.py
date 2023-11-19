### Name : RoryKirwan ###
### Student Num : 121435152 ###

#import the necessary libraries
import pygame, sys

'''--- SUPPORT FUNCTIONS ---'''
#The spawning enemies function
def spawn_enemies( X):
    '''
        Input : an x coordinate to make sure it spawns above the current row of enemies
        Function : to spawn in a new row of 6 enemies
        Output : A list containing 6 enemy objects with up to date co-ordinates
    '''
    #define the variables
    enemy_list = []
    x = X
    i = 0
    #make it loop through 6 times and to spawn six enemies
    while i < 6:
        #create the enemy object
        enemy_list.append(enemy(x, 30, 60, 30))
        #update x and the counter
        x += 100
        i += 1
    #return the list of newly created enemies
    return(enemy_list)

#The collision function
def Collision_detection(TopL, TopR, BottomL, BottomR, x, y):
    '''
        Input : sets of co-ordinates oen for every corner of one object and the x and y for the other
        Function : to detect if there has been a collision between two objects
        Output : A Boolean expression on wether or not there was a collision
    '''
    #check if there is a collision and return a true or false boolean
    if TopL < x < TopR and BottomL < y < BottomR:
        return True
    else:
        return False

'''-- GAME CLASS ---'''
#define the game class
class Game(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Galaxy Attackers")

        '''--- SCREEN VARIABLES ---'''
        #set the size of the screen using a tuple
        self.size = self.width, self.height = 900, 650
        #define the background colour
        self.colour = 0, 0, 0

        #set the screen
        self.screen = pygame.display.set_mode(self.size)
        #define the player sprite
        self.playerview = pygame.image.load("player_img.png")#92px X 207px
        #define the size if the sprite
        self.playermodel = PlayerState(((self.width/2) - 46),(self.height- 200), self.width, 1, 92, 207)
        
        '''--- MISC. VARIABLES ---'''
        #set the movement variables
        self.MovL = False
        self.MovR = False

        #set the variables for the bullet object
        self.bullet = None
        self.bulletview = pygame.image.load("Laser.png")#10px X 30px

        #set the score variable
        self.score = 0

        '''--- FIRST SET OF ENEMIES ---'''
        #set up the enemy variables
        self.counter = 0
        self.turnaround = False
        self.enemy_list = []
        self.movement = 0.2
        #spawn the enemies
        self.enemy_list = spawn_enemies(30)

    '''--- GAME FUNCTION ---'''
    #This function just runs the game
    def rungame(self):

        #infinite loop
        while True:
            
            '''--- MANAGE INPUTS---'''
            #check for an event
            for event in pygame.event.get():
                #end the program if pygame returns a quit command
                if event.type == pygame.QUIT:
                    sys.exit()
                #if pygame detects a key being pressed
                if event.type == pygame.KEYDOWN:
                    #check if they key was left in either of the control schemes
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        #change the appropriate movement variable
                        self.MovL = True
                    #check if the key was right in either of the control schemes
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        #change the appropriate movement variable
                        self.MovR = True
                    
                    #check if the key was shoot in either of the control schemes
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                        #check if an instance of the bullet class exists if it doesn't make one
                        if isinstance(self.bullet, Bullet) == False:
                            #call the shooting function
                            self.bullet = self.playermodel.Shoot()
                        
                #reset the movement variables if a key has been released
                if event.type == pygame.KEYUP:
                    self.MovL = False
                    self.MovR = False
                
            #Move the player
            if self.MovL == True:
                self.playermodel.MoveLeft()
            #Move the player
            if self.MovR == True:
                self.playermodel.MoveRight()

            '''--- BULLET MANAGEMENT ---'''
            #if a bullet exists make it "go up"
            if isinstance(self.bullet, Bullet) == True:
                self.bullet.changey()
                #if it has run off the screen delete this instance of the class
                if self.bullet.y - self.bullet.height < 0 - self.bullet.height:
                    del self.bullet
                    #reinstate the variable self.bullet
                    self.bullet = False

            '''--- SCREEN UPDATING ---'''
            #fill the screen with the background colour
            self.screen.fill(self.colour)
            
            #if a bullet exists load the bullet model
            if isinstance(self.bullet, Bullet) == True:
                self.screen.blit(self.bulletview, (self.bullet.x, self.bullet.y))
            
            #load the player model
            self.screen.blit(self.playerview, (self.playermodel.x, self.playermodel.y))
            
            '''--- SCORE TEXT RENDERING ---'''
            #load up the score font and colour
            self.font = pygame.font.Font("Minecraftia-Regular.ttf", 24)
            self.text_colour = 255, 255, 255
            #add the score variable onto the string for an auto updating score text variable
            self.score_text = "Score : " + str(self.score)
            #define the text that will appear on screen
            self.text = self.font.render(self.score_text, True, self.text_colour)
            self.textRect = self.text.get_rect()
            self.textRect.center = (80, 20)
            #load the text
            self.screen.blit(self.text, self.textRect)

            '''--- ENEMY UPDATING ---'''
            #loading up all the aliens in their new positions
            n = 0
            while n < len(self.enemy_list):

                #check if the enemies are on the left border of the screen
                if self.enemy_list[n].x < 10:
                    x = 0
                    while x < len(self.enemy_list):
                        #move every enemy down towards the player
                        self.enemy_list[x].changeY()
                        self.enemy_list[x].changeX(1)
                        #update the counter
                        x += 1
                    #spawn a new set of enemies
                    a = spawn_enemies(self.enemy_list[0].x)
                    for y in a:
                        self.enemy_list.append(y)
                    a = None
                    #turn the aliens around
                    self.turnaround = False

                #if the enemy gets to the edge of the screen move them all down by their own height
                a = (self.enemy_list[n].x + self.enemy_list[n].width)
                if a > 890:
                    x = 0
                    while x < len(self.enemy_list):
                        #move every enemy down towards the player
                        self.enemy_list[x].changeY()
                        self.enemy_list[x].changeX(-1)
                        #update the counter
                        x += 1
                    #spawn a new set of enemies
                    a = spawn_enemies(self.enemy_list[0].x)
                    #append the returned new enemies to the list
                    for y in a:
                        self.enemy_list.append(y)
                    a = None
                    #turn the aliens around
                    self.turnaround = True

                '''--- ENEMY COLLISION ---'''
                if self.enemy_list[n].alive != False:
                    #check if a bullet exists in the game
                    TF = None
                    #check if a bullet exists as to not iterate through the enemy list more times than needed
                    if isinstance(self.bullet, Bullet) == True:
                        #assign a true false based on wether or not the enemy has eben hit with a bullet
                        TF = Collision_detection(self.enemy_list[n].x, (self.enemy_list[n].x + self.enemy_list[n].width), self.enemy_list[n].y, (self.enemy_list[n].y + self.enemy_list[n].height), self.bullet.x, self.bullet.y)
                        #if it has been hit with a bullet delete the bullet, stop the enemy and add 5 score
                        if TF == True:
                            self.bullet = None
                            self.enemy_list[n].alive = False
                            self.score += 5

                     #draw the aliens in their most up to date position
                    self.alienview = pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.enemy_list[n].x,self.enemy_list[n].y,50,30))

                    # check if the enemy could be colliding with the player
                    if self.playermodel.y < self.enemy_list[n].y < (self.playermodel.y + self.playermodel.height):
                        #call the collision function
                        self. playermodel.alive = Collision_detection(self.enemy_list[n].x, (self.enemy_list[n].x + self.enemy_list[n].width), self.enemy_list[n].y, (self.enemy_list[n].y + self.enemy_list[n].height), self.playermodel.x, self.playermodel.y)

                #if the aliens are meant to be moving right move them
                if self.turnaround == False:
                    a = self.movement
                    self.enemy_list[n].changeX(a)
                #if the enemies are meant to be turning left
                if self.turnaround == True:
                    a = self.movement * -1
                    self.enemy_list[n].changeX(a)

                #delete the enemy once it heads off screen 
                if self.enemy_list[n].alive == False and self.enemy_list[n].y > self.height:
                    del (self.enemy_list[n])

                #update the counter
                n += 1
            
            #If the player is dead call the end game function
            if self.playermodel.alive == False:
                print("Game Over! Your final score was :", self.score)
                sys.exit()

            #refresh the screen
            pygame.display.flip()
    

'''--- PLAYER CLASS + FUNCTIONS ---'''
#Define the player class
class PlayerState(object):
    def __init__(self, x, y, max, n, width, height):
        #set all the positions
        self.x = x
        self.y = y
        self.maxPos = max
        self.change = n
        self.width = width
        self.height = height
        self.alive = True
    
    #Move left function
    def MoveLeft(self):
        #check if space is available to move and move if so
        if self.x + self.change < self.maxPos:
            self.x -= self.change
        #check if it is going to end up off the screen if it is set it on the edge of the screen and stop it if so
        if self.x - self.change < 0:
            self.x = 0

    #function for moving right
    def MoveRight(self):
        #check if there is space on the right hand side and move if so
        if self.x - self.change < self.maxPos:
            self.x += self.change
        #check if the player is going to end up off of the screen and then set it to the edge of the screen
        if self.x + self.width > self.maxPos:
            a = self.maxPos - self.width
            self.x = a

    #the function for shooting projectiles
    def Shoot(self):
        #get a co-ordinate at the centre of the player
        a = self.x + (self.width/2)
        #create the bullet object
        bullet = Bullet(a ,self.y, 10, 10, 30)
        return bullet

'''--- BULLET CLASS + FUNCTIONS ---'''
#The projectile class
class Bullet():
    
    def __init__(self, x, y, n, width, height):
        #set all the positional variables
        self.x = x
        self.y = y
        self.change = n
        self.width = width
        self.height = height
    
    #function for the bullet going "up" as it is shot
    def changey(self):
        self.y  -= self.change

'''--- ENEMY CLASS + FUNCTIONS ---'''
#the enemy class
class enemy():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alive = True

    #change y function
    def changeY(self):
        self.y += self.height + 30

    #change x function
    def changeX(self, n):
        self.x += n

'''--- RUNNING THE GAME ---'''
#run the game
if __name__ == "__main__":
    game = Game()
    game.rungame()