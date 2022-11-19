# Game 3: Platformer 
Partially made by: Nolan Kelley
## Brief Description:
These files are capable of running a simple platforming game/simulation.
## Requirements:
Pygame must be installed for the game to function properly.
## Start up:
The game can be played by opening "sprite_demo_1.py" in python and running the file.
## Controlls:
The player character (the little grey blob in the bottom left of the screen) can be controlled by player input. 

* Holding the left or right arrowkey will move the player left or right respectively. 

* Taping the up arrowkey while the player is grounded will cause the player to jump up into the air before decending back to the ground.

* Holding the down button while in the air will increase the acceleration of the falling speed and letting go will return the rate to normal.
## Mechanics:
* Whenever the player collides with a platform from above (or is standing on it), the player will be considered grounded. 

  * While grounded, the y velocity of the player will remain at 0 and the player will be able to jump.

  * While not grounded, the player's y velocity will be constantly increasing (towards the ground) until they reach terminal velocity. The player also won't be able to jump in this state.

* Whenever the player collides with a platform from below, their y velocity is set to 0 and their y position is decreased by 1. (This is to prevent the player from getting stuck in or jumping through the platforms.)

* Whenever the player collides with a platform from the side their's x velocity is set to zero, preventing them from moving through platforms from either side.

* If the player falls a certain distance below the bottom border of the screen, the game ends.
## Goal:
The game doesn't have an end goal in the common sense. There is a platforming challenge, but it doesn't have any reward at the end.
## Known Bugs:
* There is an inconsistant bug that causes the player to not be able to move left or right while stanging on a platform. There's a variable in the player class (self.lenience) just to deal with this bug but it only decreases how often it occurs.
