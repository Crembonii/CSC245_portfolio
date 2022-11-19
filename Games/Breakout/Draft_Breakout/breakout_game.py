##
## (Hopefully) playable game of Breakout

from pickle import FALSE, TRUE
from turtle import Screen
#from pandas import concat
import pygame
import random
from brick import Brick

from moving_ball_sprite_2d import MovingBall
from paddle import Paddle
from vector import Vector

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.
    pygame.init()
    
    bricks = []
    win = False

    # Set window size here:
    width = 860
    height = 680
    my_win = pygame.display.set_mode((width,height))
    
    # ball stats
    bRadius = 25
    bSpeedx = 1
    bSpeedy = 1 

    # paddle stats
    pSpeed = 1.1
    pWidth = 80
    pHeight = 30
    pX = (width/2) - (pWidth/2)
    pY = height - 50

    # brick stats
    # Set number of rows and columns here:
    rows = 4  # rows (max of 4) 
    coll = 3 # columns (no max, but maybe don't push it)

    bWidth = width/coll
    bHeight = (height/4)/3

    ## important properties of the environment
    env = {'ground':height, 'g':100.0}

    ## initialize the ball

    b1 = MovingBall (width/2 - 200, 10+height/2, bRadius, 15, pygame.color.Color("darkmagenta"), bSpeedx, bSpeedy, True)

    ## initialize the bricks
    
    i = 0
    while i < rows*coll:
        if i < coll:
            brick = Brick(0 + bWidth*i, 0, bWidth, bHeight, "red", True)
            bricks.append(brick)
        elif i < coll*2:
            brick = Brick(0 + bWidth*(i-coll), bHeight, bWidth, bHeight, "yellow", True)
            bricks.append(brick)
        elif i < coll*3:
            brick = Brick(0 + bWidth*(i-(coll*2)), bHeight*2, bWidth, bHeight, "green", True)
            bricks.append(brick)
        elif i < coll*4:
            brick = Brick(0 + bWidth*(i-(coll*3)), bHeight*3, bWidth, bHeight, "blue", True)
            bricks.append(brick)
        i += 1


    ## initialize the paddle
    paddle = Paddle (pX, pY, pWidth, pHeight, 0, "darkred")

    # elasticity coefficient
    e = 1.0
    
    ## setting up the clock
    clock = pygame.time.Clock()
    dt = 0
    
    ## Initialize the eventMap

    eventMap = {
        pygame.K_RIGHT:paddle.setVelocity,
        pygame.K_LEFT:paddle.setVelLeft
    }
    

    ## setting up the score
    score = 0
    font = pygame.font.SysFont("Helvetica", 25)
    losefont = pygame.font.SysFont("comicsansms", int(width/15))
    winfont = pygame.font.SysFont("Helvetica", int(width/17))

    ## The game loop starts here.

    keepGoing = True    
    while (keepGoing):


        #dt = clock.tick(50)
        #print dt

        ## Handle events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key in eventMap.keys():
                    fn = eventMap[key] 
                    fn(pSpeed)        
            elif event.type == pygame.KEYUP:
                key = event.key
                if key in eventMap.keys():
                    paddle.setVelocity(0)
                   
        if win == False:
            if b1.up:

                ## Simulate game world
                b1.simulate(dt, width, height, paddle)
                
                for br in bricks:
                    if br.getBe():
                        b1.bounce_brick(br)
                        if br.getBe() == False:
                            score += 1
                

                paddle.simulate(width)

                if score == coll * rows:
                    win = True

        #brick.simulate()
       

        ## Draw frame
        
        if b1.up:
            my_win.fill(pygame.color.Color("gray14"))
           

            for b in bricks:
                b.draw(my_win)

            b1.draw(my_win)

            paddle.draw(my_win)

            # Draw score
            my_text = font.render("Score: " + str(score), False, "gray25")
            my_win.blit(my_text, (10,10))
        
            
        if b1.up == False:
            my_win.fill(pygame.color.Color("black"))
            my_text = losefont.render("You lose! Your score was: " + str(score), False, "red")
            my_win.blit(my_text, (width/11, height/2))

        if win:
            my_win.fill(pygame.color.Color("darkblue"))
            my_text = winfont.render("Congratulations! You hit all " + str(score) + " bricks!", False, "green")
            my_win.blit(my_text, (width/17, height/2))

        ## Swap display

        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Start game
run_game()
