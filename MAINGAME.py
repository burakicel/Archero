# # # BURAK ICEL # # #
# # # GAME ARCHERO # # #
# # # PROJECT START : 28 MAY 2013 # # #

# # # IMPORT PYGAME # # #
import pygame, sys
from pygame import *
from pygame.locals import *
import math
import random
import operator #Imported for sorting 2 dimensional lists
pygame.init()


# # # WINDOW SETTINGS # # #
screen = pygame.display.set_mode((900,600)) #center point would be (450,300)
pygame.display.set_caption('GAME ARCHERO - BURAK ICEL') # title


# # # IMPORTED IMAGES # # #
background = pygame.image.load(‘resources/bgc1.jpg') #3rd person background
first_switch = pygame.image.load('resources/1stperson.png') #Switch message for 1st person
second_switch = pygame.image.load('resources/spacebar2.png') #Switch message for 3rd person
hitmark = pygame.image.load('resources/hitmark.png') #Hitmark symbol for 1st person
lost = pygame.image.load('resources/youlost.png') #Lost message
first_person_bg = pygame.image.load('resources/1stbg.jpg') #Background for 1st person
highscore_bg = pygame.image.load('resources/highscore_bg.png')
instructions_bg = pygame.image.load('resources/instructions_bg.png')
fps_arrow = pygame.image.load('resources/arrow.png')
fps_arrow_action = pygame.image.load('resources/arrow_action.png')
button_bg = pygame.image.load('resources/button_bg.jpg')
button_bg_overlay = pygame.image.load('resources/button_bg_overlay.jpg')
bg_loop = pygame.image.load('resources/bg_loop.jpg')
bg_menu = pygame.image.load('resources/bg_menu.png')
instructions = pygame.image.load('resources/info.png')
#Movement for 3RD Person Pics
movement1 = pygame.image.load('resources/movement1.png')
movement2 = pygame.image.load('resources/movement12.png')
movement3 = pygame.image.load('resources/movement2.png')
movement4 = pygame.image.load('resources/movement22.png')
shoulders = pygame.image.load('resources/shoulders.png')
shoulders2 = pygame.image.load('resources/shoulders2.png')
#Music
pygame.mixer.music.load("resources/legend.mp3")


# # # PYGAME DEFINING COLORS # # #
redColor = pygame.Color(255,0,0)
blueColor = pygame.Color(0,0,255)
blackColor = pygame.Color(0,0,0)
whiteColor = pygame.Color(255,255,255)
orangeColor = pygame.Color(255,168,0)


# # # GAME VARIABLES # # #
myfont = pygame.font.SysFont("freesansbold.ttf", 64) #Font for menu
mx = 0 #Mouse x cordinate
my = 0 #Mouse y cordinate
screentype = 0 #Variable to keep track of the screen the user is in like menu, instructions etc.
gameBreaker = 0 #To exit the game



# # # 1ST PERSON DRAWING CLASS # # #

def enemyDrawer(headx,heady,radius): #The function to draw enemies on first person
    
    if radius < 255 : #To make sure that radius does not go over 255, as 255 is the last color avaible on RGB
        radius = int(radius) #converting radius into an integer instead of a decimal
    else :
        radius = 255
    whiteColor = pygame.Color(200-radius,200-radius,200-radius) #TO MAKE THE PLAYER FADE 
    headx = int(headx)
    heady = int(heady)
    pygame.draw.circle(screen,blueColor,(headx,heady),radius) # HEAD OF THE ENEMY
    pygame.draw.rect(screen,whiteColor,(headx-radius,heady+radius,radius*2,radius*4)) #BODY OF THE ENEMY
    
    
    # # LEGS AND ARMS # #
    if counter %10 < 5: #TO ANIMATE THE LEGS
        pygame.draw.rect(screen,orangeColor,(headx-radius,heady+radius+radius*4,radius*0.7,radius*2)) #legs of the enemy
        pygame.draw.rect(screen,orangeColor,(headx-radius+radius*2-(radius*0.7),heady+radius+radius*4,radius*0.7,radius*3))#legs of the enemy
        
        pygame.draw.rect(screen,whiteColor,(headx-radius-(radius*0.5),heady+radius,radius,radius*3)) #arms of the enemy
        pygame.draw.rect(screen,whiteColor,(headx-radius+(radius*2),heady+radius,radius*0.5,radius*2.5)) #arms of the enemy
        
    else:
        pygame.draw.rect(screen,orangeColor,(headx-radius,heady+radius+radius*4,radius*0.7,radius*3)) #legs of the enemy
        pygame.draw.rect(screen,orangeColor,(headx-radius+radius*2-(radius*0.7),heady+radius+radius*4,radius*0.7,radius*2)) # legs of the enemy
        
        pygame.draw.rect(screen,whiteColor,(headx-radius-(radius*0.5),heady+radius,radius,radius*2.5)) #arms of the enemy
        pygame.draw.rect(screen,whiteColor,(headx-radius+(radius*2),heady+radius,radius*0.5,radius*3)) #arms of the enemy
        
    whiteColor = pygame.Color(255,255,255) # RESETTING THE WHITE COLOR
    

# # # MOUSE MOTION DETECTION # # # 
def getVal(tup):
    for i in range(3):
        if tup[i]==1:
            return i+1
        return 0



# # # # # # # # # GAME LOOP # # # # # # # # # 

pygame.mixer.music.play(-1) # Music play, -1 for infinity amount of times played

while True and gameBreaker == 0: #Used loops to be able to make the game playable over and over again
    
    
    looper = 0 #this the variable for the looping background image on the main menu
    looper2 = 1782 #this the variable for the looping background image on the main menu
    
    # # # MAIN MENU # # #
    while True:
        
        for event in pygame.event.get(): #Tracks users mouse motion
            if event.type == MOUSEMOTION:
                mx, my = event.pos
                button = getVal(event.buttons)
                
        screen.blit(bg_loop,(looper,0)) #Background image that moves constantly
        screen.blit(bg_loop,(looper2,0)) #Background image that moves constantly
        screen.blit(bg_menu,(0,0)) #Main interface of the menu. for example the header and footer.
        screen.blit(button_bg,(270,170)) #Button for Play
        screen.blit(button_bg,(270,270)) #Button for instructions
        screen.blit(button_bg,(270,370)) #Button for exit
        
        # # # PLAY BUTTON # # #
        
        if mx > 270 and mx < 630: #checks if the user's mouse is on the play button
            if my > 170 and my < 245:
                screen.blit(button_bg_overlay,(270,170)) #changes the button background
                if event.type == MOUSEBUTTONDOWN: #checks if the user clicked on the button
                    screentype = 0 #directs the player on the game (screentype of 0 means the play screen)
                    break #quits the main menu
        
        # # # INSTRUCTIONS BUTTON # # #        
                
        if mx > 270 and mx < 630: #checks if the user's mouse is on the instructions button
            if my > 270 and my < 345:
                screen.blit(button_bg_overlay,(270,270)) #changes the button background
                if event.type == MOUSEBUTTONDOWN: #checks if the user clicked on the button
                    screentype = 1 #directs the player on the instructions page (screentype of 1 means the instructions screen)
                    break #quits the main menu
        
        # # # EXIT BUTTON # # #
                
        if mx > 270 and mx < 630: #checks if the user's mouse is on the instructions button
            if my > 370 and my < 445:
                screen.blit(button_bg_overlay,(270,370)) #changes the button background
                if event.type == MOUSEBUTTONDOWN: #checks if the user clicked on the button
                    gameBreaker = 1 #forbids the game loop from running, eventually the player exits the game
                    break
        
        # # # BUTTON TEXTS # # #
        label = myfont.render("Play", 1, (20,20,20))
        screen.blit(label, (400, 190))
        label = myfont.render("Instructions", 1, (20,20,20))
        screen.blit(label, (315, 290))
        label = myfont.render("Exit", 1, (20,20,20))
        screen.blit(label, (400, 390))        
        pygame.display.flip()
        
        # For the movement of the background image on the main menu
        looper -= 10
        looper2 -= 10
        if looper < -1782 :
            looper = 1782
        if looper2 < -1782:
            looper2 = 1782
    
    # # # INSTRUCTIONS SCREEN # # #
    if screentype == 1: 
        
        instructionsx = 340 #Variable for keeping track of the scrolling of the information box
        
        while True:
            screen.fill(whiteColor)
            for event in pygame.event.get(): #tracks players mouse motion
                if event.type == MOUSEMOTION:
                    mx, my = event.pos
                    button = getVal(event.buttons)
            screen.blit(instructions,(280,instructionsx)) #Instructions itself
            screen.blit(instructions_bg,(0,0)) #Instructions inteface or menu image
            screen.blit(button_bg,(270,435)) #Button picture for the back button
            
            if mx > 270 and mx < 630: #checks if the users mouse is on the back button
                if my > 435 and my < 510:
                    screen.blit(button_bg_overlay,(270,435)) #changes the button's background
                    if event.type == MOUSEBUTTONDOWN: # checks if the player clicked the button
                        screentype = -1 #changes the screenmode back the main menu
                        break
            
            # Text for the buttons
            label = myfont.render("Back", 1, (20,20,20))
            screen.blit(label, (390, 450))              
            pygame.display.flip() #updates the screen
            
            #For scrolling the information box
            instructionsx -= 1
            if instructionsx < -560:
                instructionsx = 380
     
    
    # # #  VARIABLES AND LISTS NEEDED FOR THE GAME ARCHERO # # #
    
    characterPos = [308,197] #keeps track of the character cordinates based on the third person view
    mx = 0 # user mouse x coordinate
    my = 0 # user mouse y cordinate
    angle = 0 #Angle for aiming purposes
    arrows = [] #Arrow FOR 3RD PERSON VIEW Locations are stored in Lists
    counter = 0 #General Accumulator by 1
    counter2 = 0 # General Accumulator by 2
    counter3 = 0 #For First Person, Accumulator by 1
    enemies = [] #Enemy Locations stored in Lists
    breaker = 0 
    breaker2 = 0
    health = 163 #HEALTH STARTOFF, MAXIMUM IS 163
    archer_speed = 8 #Archer throwing speed, the lower the faster archer shoots arrows
    arrow_speed = 8 #Speed of the arrows, greater the faster the arrows go
    hardness = 300 #Hardness Level of the game, the lower the harder, 1 being the hardest
    arrow_distance_limit = 200 #The higher it goes, the higher distance the arrow can shoot
    enemy_speed = 1 #The lower the slower 
    fpsx = -450 #For keeping track of first person shooter movement (x cordinate)
    fpsy = -180 #For keeping track of first person shooter movement (y cordinate)
    user_pov = 3 #For keeping track of users point of view , 3 for Third Person, 1 for First Person Shooter
    userhighscore = 0 #User HighScore
    radius = 0 #For calculating the scale of enemies for first person shooter
    headshots = 0 #Player's scored headshots
    highscoreprint = "" #highscore output
    fontObj = pygame.font.Font('freesansbold.ttf',64) #Fonts for the score screen
    fontObj2 = pygame.font.Font('freesansbold.ttf',32) #Fonts for the score screen
    quitter = 0 #For checking the game replayibility stays on track
    player_movement = 0  #3rd person view, character animation
    
    
    # # # THE GAME STARTS HERE # # #
    while quitter == 0 and screentype == 0 and gameBreaker == 0: #checks the needed conditions to be able to run the game
        
        enemies = sorted(enemies, key=operator.itemgetter(3)) #orders the enemies list from biggest radius to smaller radius so that the furthest enemy gets drawn first (enemies dont overlap)
        
        
        # # # ENEMY GENERATION # # #
        
        if counter2 % hardness == 0: # hardness calculates how many enemies will be outputted at a certain amount of time
            
            randomnumber = random.randint(0,1) #Random side for the enemy
            randomyLoc = random.randint(0,600) #Random location for the enemy
            
            if randomnumber == 0: #side 1
                xside = 450.
                yside = abs(300.-randomyLoc)
                slope = yside/xside #calculates the path of the enemy
                if randomyLoc > 300:
                    enemies.append([0,randomyLoc,-slope,1])
                else :
                    enemies.append([0,randomyLoc,slope,1])
                    
            else: #side 2 
                xside = 450
                yside = abs(300.-randomyLoc)
                slope = yside/xside #calculates the path of the enemy
                if randomyLoc > 300:
                    enemies.append([900,randomyLoc,-slope,1])
                else :
                    enemies.append([900,randomyLoc,slope,1])
        
        
        #Enemy Collision Checker
        for i in range(0,len(enemies)):
            if enemies[i][0] > 300 and enemies[i][0] < 600: #checks if there are any enemies over the castles and removes them from the enemy list 
                enemies.remove(enemies[i])
                health -= 25 #decreases the health by 25
                break
        
        
        #Enemy Movement    
        for i in range(0,len(enemies)):
                if enemies[i][0] < 450: #1st Side
                    enemies[i][0] += enemy_speed #Enemy moves in x cordinate
                    enemies[i][1] += enemies[i][2]*enemy_speed #enemy moves in y cordinate
                    enemies[i][3] += (enemies[i][3]*0.015)*enemy_speed #radius of the enemy gets larger
                    
                else: #2nd Side
                    enemies[i][0] -= enemy_speed #Enemy moves in x cordinate
                    enemies[i][1] += enemies[i][2]*enemy_speed #enemy moves in y cordinate
                    enemies[i][3] += (enemies[i][3]*0.015)*enemy_speed #radius of the enemy gets larger
                    
        for event in pygame.event.get(): #Tracks the player's mouse coordinates
                if event.type == MOUSEMOTION:
                    mx, my = event.pos
                    button = getVal(event.buttons)
                    
        keys = pygame.key.get_pressed() #defines the keyboard
        
            
        #3RD PERSON DRAWINGS AND PLAY SECTION
        
        if user_pov == 3: #checks if the player is 3rd point of view
            
            pygame.mouse.set_visible(False) #makes the cursor invisible
            
            screen.blit(background,(0,0)) #outputs the background
            
            # Enemy Drawer / Draws the enemies on 3rd person view
            for i in range(0,len(enemies)): # for all of the enemies in the list
                pygame.draw.circle(screen,blackColor,(int(enemies[i][0]),int(enemies[i][1])),10) #black circles represent the enemies
            
            
            #Health Output    
            if health > 0: #The health is not being outputted on screen if it is below zero
                pygame.draw.rect(screen,redColor,(45,48,health,15)) #health bar
            
            
            #3rd Person Player Animation Added / Mr. Ching Suggestion
            if player_movement == 1 or player_movement == 2: #checks the direction of the player
                if counter % 30 < 15: #animates the player's legs
                    screen.blit(movement1,(characterPos[0]-13,characterPos[1]-9))
                else :
                    screen.blit(movement2,(characterPos[0]-13,characterPos[1]-9))
                    
            elif player_movement == 3 or player_movement == 4:
                if counter % 30 < 15: #animates the player's legs
                    screen.blit(movement3,(characterPos[0]-13,characterPos[1]-9))
                else :
                    screen.blit(movement4,(characterPos[0]-13,characterPos[1]-9))
                    
            else: #animates the player's legs
                if characterPos[1] > 195 and characterPos[1] < 203:
                    screen.blit(shoulders2,(characterPos[0]-13,characterPos[1]-9))
                elif characterPos[1] < 385 and characterPos[1] > 370:
                    screen.blit(shoulders2,(characterPos[0]-13,characterPos[1]-9))
                else:
                    screen.blit(shoulders,(characterPos[0]-13,characterPos[1]-9))
            
            
            player_movement = 0 #sets the player's direction to zero
            
            pygame.draw.circle(screen,redColor,(characterPos[0],characterPos[1]),8) #Draw's the player's body, red circle
            
            
            #Hitmark
            pygame.draw.circle(screen,redColor,(mx,my),12,2) #3rd person red hitmark 
            
            
            #Printing Highscore on to the screen        
            highscoreprint = str(userhighscore)
            msgSurfaceobj = fontObj.render(highscoreprint,False,whiteColor)
            msgRectobj = msgSurfaceobj.get_rect()
            msgRectobj.topleft = (30,500)
            screen.blit(msgSurfaceobj, msgRectobj)
            
            #Draws the arrows on to the screen
            for i in range(0,len(arrows)): #this loop outputs all of the arrows in to the screen
                    pygame.draw.line(screen,blueColor,(arrows[i][0],arrows[i][1]),(arrows[i][2],arrows[i][3]),6)
            
            
            # # # # 3RD PERSON MOUSE AIMING # # # #
            
            
            if my < characterPos[1] and mx < characterPos[0]: # QUADRANT 2
                #NOTE : I AM USING TRIGONOMETRY TO CALCULATE THE 3RD PERSON AIMING
                    opposite = float(characterPos[1])-my
                    adjacent = float(characterPos[0])-mx
                    angle = math.atan(opposite/adjacent) #Calculates the angle of the aiming by the opposite and adjacent sides
                    x = abs(30.*math.cos(angle)) #SIDES 1
                    y = math.sqrt(30**2-x**2) #SIDE 2 CALCULATED BY PYTHOGERA'S THEOREM
                    x = int(round(x, 0))
                    y = int(round(y, 0))
                    angle = 180/(math.pi/angle) #CONVERTS IT TO DEGREES FROM RADIANS 
                    pygame.draw.line(screen,blueColor,(characterPos[0],characterPos[1]),(characterPos[0]-x,characterPos[1]-y),6) #DRAWS THE BLUW BOW
                    
                    if event.type == MOUSEBUTTONDOWN: #CHECKS IF THE USER CLICKED ON THEIR MOUSE TO SHOOT
                        speed = arrow_speed # Appoints the speed to the arrow
                        slope = (opposite/adjacent)*speed #Calculates the slope and modifies it based on the speed
                        
                        while (slope+speed) > arrow_speed: #TO MAKE SURE THE ARROW IS NOT REALLY FAST * IDEA CREDIT = MOHAMED
                            slope = slope*0.9
                            speed = speed*0.9
                            
                        if counter > archer_speed: #Inserts the arrow into the arrows lists after it has an appropiate speed
                            arrows.append([characterPos[0],characterPos[1],characterPos[0]-x,characterPos[1]-y,-slope,0,-speed])
                            counter = 0
                
                
            elif my < characterPos[1] and mx > characterPos[0]: #QUADRANT 1
                opposite = float(characterPos[1])-my
                adjacent = mx-float(characterPos[0])
                angle = math.atan(opposite/adjacent) #Calculates the angle of the aiming by the opposite and adjacent sides
                x = abs(30.*math.cos(angle)) #SIDES 1
                y = math.sqrt(30**2-x**2) #SIDE 2 CALCULATED BY PYTHOGERA'S THEOREM
                x = int(round(x, 0))
                y = int(round(y, 0))        
                angle = 180/(math.pi/angle) #CONVERTS IT TO DEGREES FROM RADIANS
                pygame.draw.line(screen,blueColor,(characterPos[0],characterPos[1]),(characterPos[0]+x,characterPos[1]-y),6) #DRAWS THE BLUE BOW
                
                if event.type == MOUSEBUTTONDOWN: #CHECKS IF THE USER CLICKED ON THEIR MOUSE TO SHOOT
                    speed = arrow_speed # Appoints the speed to the arrow
                    slope = (opposite/adjacent)*speed #Calculates the slope and modifies it based on the speed
                    while (slope+speed) > arrow_speed: #TO MAKE SURE THE ARROW IS NOT REALLY FAST * IDEA CREDIT = MOHAMED
                        slope = slope*0.9
                        speed = speed*0.9
                    if counter > archer_speed: #Inserts the arrow into the arrows lists after it has an appropiate speed
                        arrows.append([characterPos[0],characterPos[1],characterPos[0]+x,characterPos[1]-y,-slope,0,speed])
                        counter = 0
                        
                        
            elif my > characterPos[1] and mx < characterPos[0]: # QUADRANT 3
                opposite = my-float(characterPos[1])
                adjacent = float(characterPos[0])-mx
                angle = math.atan(opposite/adjacent) #Calculates the angle of the aiming by the opposite and adjacent sides
                x = abs(30.*math.cos(angle)) #SIDES 1
                y = math.sqrt(30**2-x**2) #SIDE 2 CALCULATED BY PYTHOGERA'S THEOREM
                x = int(round(x, 0))
                y = int(round(y, 0))                
                angle = 180/(math.pi/angle) #CONVERTS IT TO DEGREES FROM RADIANS
                pygame.draw.line(screen,blueColor,(characterPos[0],characterPos[1]),(characterPos[0]-x,characterPos[1]+y),6) #DRAWS THE BLUE BOW
                if event.type == MOUSEBUTTONDOWN: #CHECKS IF THE USER CLICKED ON THEIR MOUSE TO SHOOT
                    speed = arrow_speed # Appoints the speed to the arrow
                    slope = (opposite/adjacent)*speed #Calculates the slope and modifies it based on the speed
                    while (slope+speed) > arrow_speed: #TO MAKE SURE THE ARROW IS NOT REALLY FAST * IDEA CREDIT = MOHAMED
                        slope = slope*0.9
                        speed = speed*0.9
                    if counter > archer_speed: #Inserts the arrow into the arrows lists after it has an appropiate speed
                        arrows.append([characterPos[0],characterPos[1],characterPos[0]-x,characterPos[1]+y,slope,0,-speed])
                        counter = 0
                        
                        
            elif my > characterPos[1] and mx > characterPos[0]: #QUADRANT 4
                opposite = my-float(characterPos[1])
                adjacent = mx-float(characterPos[0])
                angle = math.atan(opposite/adjacent) #Calculates the angle of the aiming by the opposite and adjacent sides
                x = abs(30.*math.cos(angle)) #SIDES 1
                y = math.sqrt(30**2-x**2) #SIDE 2 CALCULATED BY PYTHOGERA'S THEOREM
                x = int(round(x, 0))
                y = int(round(y, 0))        
                angle = 180/(math.pi/angle) #CONVERTS IT TO DEGREES FROM RADIANS
                pygame.draw.line(screen,blueColor,(characterPos[0],characterPos[1]),(characterPos[0]+x,characterPos[1]+y),6) #DRAWS THE BLUE BOW
                if event.type == MOUSEBUTTONDOWN: #CHECKS IF THE USER CLICKED ON THEIR MOUSE TO SHOOT
                    speed = arrow_speed # Appoints the speed to the arrow
                    slope = (opposite/adjacent)*speed #Calculates the slope and modifies it based on the speed
                    while (slope+speed) > arrow_speed: #TO MAKE SURE THE ARROW IS NOT REALLY FAST * IDEA CREDIT = MOHAMED
                        slope = slope*0.9
                        speed = speed*0.9
                    if counter > archer_speed: #Inserts the arrow into the arrows lists after it has an appropiate speed
                        arrows.append([characterPos[0],characterPos[1],characterPos[0]+x,characterPos[1]+y,slope,0,speed])
                        counter = 0
            
            else: #TO MAKE SURE THE ARROW DOESNT DISAPEAR IN ABSURD CASES SUCH AS WHEN ARROW IS AIMED AT 90 or 0 degrees
                my += 1
                mx += 1
            
            
            # ARROW MOVEMENT IN 3RD PERSON
            if len(arrows) > 0: #Applies to all the arrows that are saved on the list
                for i in range(0,len(arrows)): #2ND DIMENSIONAL LIST USED AS AN ACCUMULATOR TO GET THE ARROWS MOVING
                    arrows[i][0] += arrows[i][6]
                    arrows[i][2] += arrows[i][6]
                    arrows[i][1] += arrows[i][4]
                    arrows[i][3] += arrows[i][4]
                    arrows[i][5] += abs(arrows[i][4])+abs(arrows[i][6])
                    
                for i in range(0,len(arrows)): # Checks if the arrows meet their distance limit
                    if arrows[i][5] > arrow_distance_limit: # if the arrows has travelled longer distance than the limit, it is immediatly removed
                        arrows.remove(arrows[i])
                        break
                    
            pygame.mouse.set_visible(False) #Mouse is set to invisible
            
            
            # # #  PLAYER MOVEMENT IN 3RD PERSON PERSPECTIVE # # #
                    
            if keys[K_UP]: # DEALS WITH THE UPPER MOVEMENT OF THE PLAYER WITH THE UP KEY
                if characterPos[1] > 197: #Limits are used to make the enemy only be able to move at the castle walls
                    if characterPos[0] > 300 and characterPos[0] < 315:
                        characterPos[1] -= 2
                    if characterPos[0] < 595 and characterPos[0] > 580:
                        characterPos[1] -= 2
                    player_movement = 1 #direction of the player
                    
            if keys[K_DOWN]: # DEALS WITH THE LOWER MOVEMENT OF THE PLAYER WITH THE DOWN KEY
                if characterPos[1] < 375: #Limits are used to make the enemy only be able to move at the castle walls
                    if characterPos[0] > 300 and characterPos[0] < 315:
                        characterPos[1] += 2
                    if characterPos[0] < 595 and characterPos[0] > 580:
                        characterPos[1] += 2
                    player_movement = 2 #direction of the player
                    
            if keys[K_RIGHT]: # DEALS WITH THE RIGHT MOVEMENT OF THE PLAYER WITH THE RIGHT KEY
                if characterPos[0] < 585:
                    if characterPos[1] > 195 and characterPos[1] < 203:
                        characterPos[0] += 3
                    if characterPos[1] < 385 and characterPos[1] > 370:
                        characterPos[0] += 3
                    player_movement = 3 #direction of the player
                    
            if keys[K_LEFT]: # DEALS WITH THE RIGHT MOVEMENT OF THE PLAYER WITH THE RIGHT KEY
                if characterPos[0] > 308:
                    if characterPos[1] > 195 and characterPos[1] < 203:
                        characterPos[0] -= 3
                    if characterPos[1] < 385 and characterPos[1] > 370:
                        characterPos[0] -= 3
                    player_movement = 4 #direction of the player
            
            
            # # # TURRET POSITION # # #
            if characterPos[1] > 275 and characterPos[1] < 290: #Checks if the user is at one of the turrets
                screen.blit(first_switch,(170,0)) #Invites the user to 1st person by displaying a message
                if keys[K_1]: #Checks if the user pressed 1
                    user_pov = 1
                    enemy_speed = 0.3 #Enemy speed gets lowered in 1st Person View
                        
                
            pygame.display.flip()
            
            
            # 3RD PERSON SHOOTING COLLISON DETECTOR
            for i in range(0,len(enemies)): #Checks all of the enemies
                if breaker == 1:
                    break
                for q in range(0,len(arrows)): #The distance is checked between each arrow and enemy, this is achieved by the inner loops
                    distance = math.sqrt((arrows[q][0]-enemies[i][0])**2+(arrows[q][1]-enemies[i][1])**2)
                    if distance < 15:
                        enemies.remove(enemies[i]) #enemies and arrows are removed if the distance is low enough
                        arrows.remove(arrows[q])
                        userhighscore += 15 #highscore is acting an accumulator
                        breaker = 1
                        break
        
        
        # # # # # # # # FIRST PERSON SHOOTER SECTION # # # # # # # #
        
        else:
            screen.blit(first_person_bg,(fpsx,fpsy)) # Outputs the background which is the grass field
            screen.blit(second_switch,(170,0)) # Invites the user to go in to the 3rd person mode by pressing 3
            screen.blit(highscore_bg,(0,0))
            
            if health > 0: #Outputs the health if it is greater than zero
                pygame.draw.rect(screen,redColor,(45,48,health,15))
            
            if keys[K_3]: #If the user presses 3, it changes the point of view to Third Person.
                    user_pov = 3
                    enemy_speed = 1
                    fpsx = -450
            
            if keys[K_LEFT]: # Player Left Movement
                if fpsx < 0:
                    fpsx += 10
                    
            if keys[K_RIGHT]: #Player Right Movement
                if fpsx > -900:
                    fpsx -= 10
                    
            if keys[K_UP]: #Player Up Movement
                if fpsy < 0:
                    fpsy += 10
                    
            if keys[K_DOWN]: #Player Down Movement
                if fpsy > -300:
                    fpsy -= 10
            
            
            # # # FIRST PERSON SHOOTING # # #     
            
            if keys[K_SPACE]: #detects if the user pressed space
                
                screen.blit(fps_arrow_action,(0,0)) #Outputs the arrow shooting image
                
                if characterPos[0] < 450: #Checks for the enemies on the 1st side
                    for i in range(0,len(enemies)):
                        if enemies[i][0] < 450:
                            enemyLoc = ( abs(enemies[i][1]-600.) / 600) * 1800
                            #Checks if the arrow hit the body of the enemy
                            if 419 > (enemyLoc+fpsx)-enemies[i][3] and 419 < ((enemyLoc+fpsx)-enemies[i][3])+(enemies[i][3]*2):
                                if 269 > (350+(fpsy+180)) + enemies[i][3] and 269 < ((350+(fpsy+180)) + enemies[i][3])+(enemies[i][3]*4):
                                    enemies.pop(i)
                                    userhighscore += 30
                                    break
                            distance = math.sqrt((enemyLoc+fpsx-419)**2+((350+(fpsy+180)-269)**2))
                            #Checks if the arrow hit the enemy's head by using the distance formula
                            if distance < enemies[i][3]:
                                enemies.pop(i)
                                userhighscore += 60
                                headshots += 1
                                break
                            
                else: #Checks for the enemies on the 2nd side
                    for i in range(0,len(enemies)):
                        if enemies[i][0] > 450:
                            enemyLoc = ( enemies[i][1] / 600.) * 1800
                            #Checks if the arrow hit the body of the enemy
                            if 419 > (enemyLoc+fpsx)-enemies[i][3] and 419 < ((enemyLoc+fpsx)-enemies[i][3])+(enemies[i][3]*2):
                                if 269 > (350+(fpsy+180)) + enemies[i][3] and 269 < ((350+(fpsy+180)) + enemies[i][3])+(enemies[i][3]*4):
                                    enemies.pop(i)
                                    userhighscore += 30
                                    break
                            distance = math.sqrt((enemyLoc+fpsx-419)**2+((350+(fpsy+180)-269)**2))
                            #Checks if the arrow hit the enemy's head by using the distance formula
                            if distance < enemies[i][3]:
                                enemies.pop(i)
                                userhighscore += 60
                                headshots += 1
                                break
                            
                            
            # # # ENEMY OUTPUTTING ON FPS # # #
            
            if characterPos[0] < 450: # Enemies that are on the 1st side
                for i in range (0,len(enemies)):
                    if enemies[i][0] < 450:
                        enemyLoc = ( abs(enemies[i][1]-600.) / 600) * 1800 #EnemyLoc uses the ratio between the 1st person 3rd person view to output the enemies appropiately 
                        enemyDrawer(enemyLoc+fpsx,350+(fpsy+180),enemies[i][3]) #outputs the enemies
                        
            else: #Enemies that are on the 2nd side
                for i in range (0,len(enemies)):
                    if enemies[i][0] > 450:
                        enemyLoc = ( enemies[i][1] / 600.) * 1800 #EnemyLoc uses the ratio between the 1st person 3rd person view to output the enemies appropiately 
                        enemyDrawer(enemyLoc+fpsx,350+(fpsy+180),enemies[i][3]) #outputs the enemies
                        
            screen.blit(fps_arrow,(0,0)) #FPS ARROW OUTPUT
            
            #Printing the Highscore
            highscoreprint = str(userhighscore)
            msgSurfaceobj = fontObj.render(highscoreprint,False,whiteColor)
            msgRectobj = msgSurfaceobj.get_rect()
            msgRectobj.topleft = (30,500)
            screen.blit(msgSurfaceobj, msgRectobj)        
            pygame.display.flip()
            
            
        breaker = 0
        
        
        
        # # # # PLAYER DEATH / LOST # # #
        
        if health < 0 : # Player loses once all the health is gone
            
            pygame.mouse.set_visible(True) #mouse becomes visible
            screen.blit(lost,(170,200)) #lost message
            
            #Prints highscore
            output_text = str("Your score :"+str(userhighscore))
            highscoreoutput = highscoreprint
            highscoreprint = output_text
            msgSurfaceobj = fontObj2.render(highscoreprint,False,redColor)
            msgRectobj = msgSurfaceobj.get_rect()
            msgRectobj.topleft = (320,340)
            screen.blit(msgSurfaceobj, msgRectobj)
            
            #Prints Headshots amount
            label = myfont.render("Headshots :"+str(headshots), 1, (20,20,20))
            screen.blit(label, (320, 140))
            
            #Back to the Main Menu Button
            while True:
                screen.blit(button_bg,(240,430))                      
                for event in pygame.event.get():
                    if event.type == MOUSEMOTION:
                        mx, my = event.pos
                        button = getVal(event.buttons)
                if mx > 240 and mx < 600:
                    if my > 430 and my < 505:
                        screen.blit(button_bg_overlay,(240,430))
                        if event.type == MOUSEBUTTONDOWN: #checks if the player pressed the button
                            quitter = 1
                text = "Main Menu"
                highscoreoutput = highscoreprint
                highscoreprint = text
                msgSurfaceobj = fontObj2.render(highscoreprint,False,redColor)
                msgRectobj = msgSurfaceobj.get_rect()
                msgRectobj.topleft = (330,455)
                screen.blit(msgSurfaceobj, msgRectobj)            
                pygame.display.flip()
                if quitter == 1:
                    break
        
        # GENERAL ACCUMULATORS THAT ARE RUNNING BOTH ON THE FIRST PERSON AND THIRD PERSON VIEW
        
        #COUNTERS
        counter += 1
        counter2 += 1
        
        # HARDNESS SETTINGS , AS THE HIGHSCORE INCREASES IT BECOMES HARDER
        if userhighscore > 200:
            hardness = 200
            enemyspeed = 2
        if userhighscore > 400:
            hardness = 150
        if userhighscore > 600:
            hardness = 100

# Closing the window                
pygame.display.update()
pygame.quit()