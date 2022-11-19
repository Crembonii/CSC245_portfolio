************************************************************************************
				WELCOME TO BREAKOUT
************************************************************************************

Description:
These files are capable of running the game Breakout decently well. Two of the parameters of the game (the # of rows/columns of bricks to break and the window size) are easily variable, with other parts of the game adjusting to the changes.


Requirements:
Pygame (and python) must be installed for the code to funcion as intended.


Instructions:

In order to play the game:
	Simply open the folder in python, open the "breakout_game.py" file, and run the program.

Goal: 
	The ball bounces off the walls, celing, paddle, and bricks. If the ball touches the floor, the game ends and the player (you) loses. However, whenever the ball hits a brick, the brick is destroyed. If the player manages to hit all the bricks before the ball hits the ground, the game ends and the player (you) wins! 

Controls:
	Left arrow key moves the paddle left.
	Right arrow key moves the paddle right.
	Lifting either key stops the paddle.
	
 
In order to change the # of rows/columns:
	Open "breakout_game.py" and scroll to lines 51 and 52. Insert your desired # of rows/columns, save the file, and run the program again.
	Note: The game can only make a maximum of 4 rows, so setting rows = to a higher number might make the game never show a win screen (as some of the bricks will be off screen).


In order to change the window size:
	Open "breakout_game.py" and scroll to lines 24 and 25. Insert your desired width/height of the window, save the file, and run the program again.
	Note: Several other parameters can be altered between lines 23 and 43. 
	
