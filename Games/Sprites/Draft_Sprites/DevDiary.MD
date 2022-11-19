# Sprite Game Dev Diary
By: Nolan Kelley
## Completed Assignment Requirements:
* Update the sprite movement so that it can move both left and right.
* Find a way using the flip() method for sprites to have the sprite drawn correctly when walking to the left.
* Implement AABB collisions using the Sprite collision functions.
* Implement gravity for the sprite.
* Implement jumping for the sprite.
* Using the pygame sprite collision API, add the ability for the sprite to jump on top of platforms.
* Add more platforms!
* README
 
## Completed Optional Features:
* Use a different sprite sheet (from those included) to make textures for the platforms, and other sprites.
 
## Completed Personal Optional Features:
* Have sprites reflect when player is rising/falling/idle.
    * Have sprites reflect what direction the player was facing before stopping when not moving horizontally.
* Added a terminal velocity.
* Added a drop function to allow for more controll in the air.

## New knowledge learned:
* Making and using a sprite sheet.
* Sprite/platform collision with gravity.
* Basic markdown.

## Old knowledge dusted off:
* Object lists.
* If statements (there were many.)
* Making methods

## Easiest/Most fun:
* Implementing gravity and the jump function.
* Making my player sprite.
* Making more platforms.

## Struggles:
* When making the platform physics, I struggled with defining whether the player is colliding with a platform from the side or from above. I fixed this by checking to make sure a collision in the x isn't also a collision in the y with wider parameters before checking if it's an x collision and vice versa. (I also had a check to move the player up a bit if they land a bit inside the platform.)
* Getting the sprite animation to look the way I wanted was a struggle. I tried for a long time, but couldn't for the life of me get the feet of each frame to be touching the ground. I'm pretty sure it was caused by the facts that the origin of each sprite is the top left corner, many of my sprites have varying heights, and the hitbox of the character stays the same regardless of the sprite size/shape (which I am very thankful for).
* It took me a supprising amount of time just to figure out what a markdown file was and how to make one. Once I figured that out though, using markdown was easy.