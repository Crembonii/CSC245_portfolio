# **Feedback of Feedback (Change_Log)**
## **Key**
* ~~sample~~ Revisions that have been made.
* **sample** My comments on your comments.

## Required Features
* [x] Bouncing Ball
* [x] Paddle
* [x] Blocks
* [x] Score
* [x] OO Implementation
* [x] README.md
* [**x**] GameDev Diary
    * **The file name isn't exactly "GameDevDiary" but I like having it be more specific.**

## Optional Features (that I noticed):
* [x]  splash screen

## Notes and Revision
* nice work!
    * **Thank you, nice revisions!**
* ~~your diary is a pdf~~
    * **Replaced it with a Markdown file.**
* you handle collisions in a weird way, by painting the brick black instead of just removing it from the list of objects.
    * **Weird ≠ bad (my personal opinion (if you really think it should be the other way I'll change it.))**
* ~~you don't have to use getters and setters in python OO code, and are largely un-necessary for programs like this~~
* ~~some code inelegancies with if/elif statements~~

```
        if self.be:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.w, self.h))
        elif self.be == False:
            pygame.draw.rect(window, "black", (self.x, self.y, self.w, self.h))
```

**Replaced**
```
elif self.be == False:
```
**with**
```
else:
```
~~code like below also uses a hidden variable (self.be) controlled by the `bounce_brick()` method, whereas it's better to just have `bounce_brick()` return true of false!~~

```
                    if br.getBe():
                        b1.bounce_brick(br)
                        if br.getBe() == False:
                            score += 1
```

```
                    if br.be:
                        bounced = b1.bounce_brick(br)
                        if bounced: 
                            score += 1

```
**I simplified it further by useing the "bounce_brick" method itself as the parameter for the if statement. (Is there any reason I shouldn't do that? Cause it feels like there could be.)**

**I also removed the code in the "bounce_brick" method that sets "exists" for the brick to False and instead set "exists" to false in the if statement.**

```
for br in bricks:
    if br.exists:
        if b1.bounce_brick(br):
            score += 1
            br.exists = False
```
* ~~also "be" is not a great variable name.~~
* **Replaced "be" with "exists"**
