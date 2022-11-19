# Feedback of Feedback for Baselines Game
**Bold text is all my comments on your comments.**
## HW1 - travel time

* functions should (almost) never print, they should simply return.
    * **Removed the print statement**
* you should include testing code in your py file.  I'll teach how
    * **Added test situations to code and printed outside of the function**

## HW2 - guessing game

You're using two back-to-back `if` statements where you should be using `if/elif/else`.

**"Should" is a strong word, but I replaced the second `if` with an `else`.**

I'm not sure what the `imp` module you're importing is.

**Me neither. I removed it and the file still works, so I guess it was nothing.**

## Night Sky

On one hand, this is your first python program at Union.  On the other hand, it's not great:

* you say "blatantly stolen" code, but don't give credit.  stolen from where?
    * **Edited comment to be less incriminating.**
* you draw stars outside of the Game Loop, thereby violating the Sanctity Of The Loop
    * **I know my crimes against the game loop can never be forgiven, but I've altered the code to be back in the game loop.**
* **I also entirely revamped my nightsky file.**
    * **Now I use a list of star objects instead of drawing all the stars at once.**
        * **This allows me to print the stars and background repeatedly without makeing new stars each loop.**
    * **I got the bonus 'shooting star' working and made it way more complicated than it needed to be.**

## Overall Feedback

This is a good start, but you've got a lot of fundamental clean coding skills to develop

