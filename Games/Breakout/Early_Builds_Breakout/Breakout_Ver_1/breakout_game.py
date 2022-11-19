##
## (Hopefully) playable game of Breakout

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

    balls = []
    
    bricks = []

    width = 640
    height = 480
    my_win = pygame.display.set_mode((width,height))
    
    # ball stats
    bRadius = 30
    bSpeedx = 0.3
    bSpeedy = 0.3

    # paddle stats
    pSpeed = 0.05
    pWidth = 80
    pHeight = 30
    pX = (width/2) - (pWidth/2)
    pY = 400

    # brick stats
    bWidth = 128
    bHeight = 40

    ## important properties of the environment
    env = {'ground':height, 'g':100.0}

    ## initialize the balls
    numballs = 1

    b1 = MovingBall (width/2 - 200, 10+height/2, bRadius, 15, pygame.color.Color("darkmagenta"), bSpeedx, bSpeedy)
    balls.append(b1)

    ## initialize the bricks
    numbricks = 15  # max of 20

    i = 0
    while i < numbricks:
        if i < 5:
            brick = Brick(0 + bWidth*i, 0, bWidth, bHeight, "red", True)
            bricks.append(brick)
        elif i < 10:
            brick = Brick(0 + bWidth*(i-5), bHeight, bWidth, bHeight, "yellow", True)
            bricks.append(brick)
        elif i < 15:
            brick = Brick(0 + bWidth*(i-10), bHeight*2, bWidth, bHeight, "green", True)
            bricks.append(brick)
        elif i < 20:
            brick = Brick(0 + bWidth*(i-15), bHeight*3, bWidth, bHeight, "blue", True)
            bricks.append(brick)
        i += 1


    ## initialize the paddle
    paddle = Paddle (pX, pY, pWidth, pHeight, 0, "darkred")

    ## Initialize the eventMap (NOPE)

    """
    eventMap = {
        pygame.K_RIGHT:Paddle.setVelocity,
        pygame.K_LEFT:Paddle.setVelocity,
        pygame.KEYDOWN:Paddle.setVelocity
    }

    if pygame.K_RIGHT in eventMap.keys():
        fn = eventMap[pygame.K_RIGHT]
        fn (paddle, pSpeed)

    if pygame.K_LEFT in eventMap.keys():
        fn = eventMap[pygame.K_LEFT]
        fn (paddle, -pSpeed)

    if pygame.KEYUP in eventMap.keys():
        fn = eventMap[pygame.KEYUP]
        fn (paddle, 0)
    """

    # elasticity coefficient
    e = 1.0
    
    ## setting up the clock
    clock = pygame.time.Clock()
    dt = 0
    
    ## setting up the score
    score = 0
    font = pygame.font.SysFont("comicsansms", 25)
    my_text = font.render("Score: " + str(score), False, (0, 0, 0))

    ## The game loop starts here.

    keepGoing = True    
    while (keepGoing):


        #dt = clock.tick(50)
        #print dt

        ## Handle events.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False


        ## Simulate game world
        for b in balls:
            b.simulate(dt, width, height, paddle)
        
        for b in bricks:
            

        paddle.simulate(width)

        #brick.simulate()
       

        ## Draw frame
        
        my_win.fill(pygame.color.Color("gray14"))

        for b in balls:
            b.draw(my_win)

        for b in bricks:
            b.draw(my_win)

        paddle.draw(my_win)

        # Draw score
        my_win.blit(my_text, (50,50))

        ## Swap display

        pygame.display.update()

    ## The game loop ends here.

    pygame.quit()


## Start game
run_game()
