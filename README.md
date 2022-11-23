# Nolan A. Kelley CSC 245 Portfolio 
This is the README document for my portfolio for CSC 245, Fall term 2022. Below this is a table of contents, through which all other folders can be navigated to. Below that is my Final Grade Bid, a section in which I delve into each of my Contract requirements one by one and try to discover what grade I have earned for this class. At the very bottom of this file the conclusion that I have come and a brief description on my thoughts about it.

# Table of Contents
| Folders                           | About                             |
| -------                           | -------                           |
|[Contract](Contract/README.md)     | My contract and kwl               |
|[Games](Games/README.md)           | Games developed for this class    |
|[In-Class](In-Class/README.md)     | In class projects                 |

# Final Grade Bid
Below I go through each objective in my [Replacement_Grading_Contract](Contract/Hopeful_Replacement_Grading_Contract.MD) (and in the original [Grading_Contract](Contract/CSC_245_Grading_Contract.MD)) and judge which grade I believe I've met.

## Meet 90% of my KWL objectives.
In my contract, I stated that, to get an A, I would meet 90% of my KWL objectives in the term. Below is a table with links to DevDiary files that prove that all but one KWL objective has been learned:

| Objective                         | Receipt  |
| -------                           | -------- |
|Git                                |[Flocking](Games/Flocking/Draft_Flocking/DevDiary.MD)|
|Linux Terminal                     |[Flocking](Games/Flocking/Draft_Flocking/DevDiary.MD)|
|markdown                           |[Breakout](Games/Breakout/Final_Breakout/DevDiary.MD)|
|Object Oriented Python             |[Breakout](Games/Breakout/Final_Breakout/DevDiary.MD)|
|list comprehensions                |[Roomba_Rampage](Games/Roomba_Rampage/cleaning-game/README.md)|
|ssh and ssh keys                   |[Flocking](Games/Flocking/Draft_Flocking/DevDiary.MD)|
|vector math                        |[Breakout](Games/Breakout/Final_Breakout/DevDiary.MD)|
|Platformer physics (collision)     |[Sprites](Games/Sprites/Draft_Sprites/DevDiary.MD)|
|finite state machines              |[FSMs](Games/FSMs/Draft_FSMs/DevDiary.md)|
|path planning                      |[Path_Planning](Games/Path_Planning/Draft_Path_Planning/DevDiary.MD)|
|Tree Search                        |[Path_Planning](Games/Path_Planning/Draft_Path_Planning/DevDiary.MD)|
|sprites                            |[Sprites](Games/Sprites/Draft_Sprites/DevDiary.MD)|
|sprite sheets and animation        |[Sprites](Games/Sprites/Draft_Sprites/DevDiary.MD)|
|rotating sprites                   |[Roomba_Rampage](Games/Roomba_Rampage/cleaning-game/README.md)|
|moving screen                      | Never learned |
|pygame API                         |any/all projects|
|clients and servers                |[Networking](Games/Networking/Draft_Networking/DevDiary.md)|
|hitboxes as separate objects       |[Roomba_Rampage](Games/Roomba_Rampage/cleaning-game/README.md)|

Because I had 18 objectives in total, missing one means I still made 94% of my objectives, which is enough for an A.

## Complete a final game project that demonstrates 90% of the concepts I've learned in the class.
This objective is out of order compared to the [contract](Contract/Hopeful_Replacement_Grading_Contract.MD), but I feel it should follow the previous one, as they both have to do with the KWL Chart. Below is a chart with all the learned objectives in my KWL Chart (and some other learned concepts b/c this prompt doesn't specify them being in the KWL chart) with links (where applicable) and explinations for the ones I believe I completed in Roomba Rampage.

| Objective                         | Explination | Demonstrated |
| -------                           | --------    | ------------ |
|Git                                | I made the Git repository for Roomba Rampage and figured out, with Matt and Liv, how to work on one project at the same time using git. | y |
|Linux Terminal                     | I used the terminal when setting up the Git repo. | y |
|markdown                           | I used Markdown while writing the [DevDiary](Games/Roomba_Rampage/cleaning-game/DevDiary.md), [Design_Document](cleaning-game/Design_Document.md), and the bare bones [README](Games/Roomba_Rampage/cleaning-game/README.md). |  y |
|Object Oriented Python             | Nearly everything is an object in this game. [Here](Games/Roomba_Rampage/cleaning-game/healthbar.py)'s an example!| y |
|list comprehensions                | I used one list comprehension in the init method of the [mess](Games/Roomba_Rampage/cleaning-game/mess.py) class specifically for this chart. | y |
|ssh and ssh keys                   | I made a repo for this in Git, so I had to use ssh keys. | y |
|vector math                        | I utelized some of that wonkey vector math from the [Breakout](Games/Breakout/Final_Breakout/DevDiary.MD) game in making the [roombas](Games/Roomba_Rampage/cleaning-game/roomba_rework_2.py).| y |
|trig math (not in KWL)             | I took advantage of trig functions (sin() and cos()) and the value pi imported from math to make the [broom](Games/Roomba_Rampage/cleaning-game/broom.py) rotate around the end of the handle rather than around the center of the sprite. Matt did most of the broom stuff, but I did this part. | y |
|Platformer physics (collision)     | I utilized much of the platformer phisics from the [player](Games/Sprites/Draft_Sprites/player.py) class in my sprite game for the [sweeper's_hitbox](Games/Roomba_Rampage/cleaning-game/sweeper_hitbox.py) class in Roomba Rampage. I just tweaked bits of it to get rid of gravity and stuff like that.| y |
|finite state machines  (I know, it's a lot)          | I did not officially use an FSM in this project, but I believe I came up with a different method to do a similar thing that seems easier to me. In the [roomba_rework_2](Games/Roomba_Rampage/cleaning-game/roomba_rework_2.py) file, I used and integer value (self.i) to denote which type of roomba it is. Then, in the `simulate` method, everything that the roomba does is filtered by if statements asking what value of i the roomba has. (I did this often in the `behave` method.) Then, to simulate transitions, whenever some event could change the roombas type, we can add an if statement only allowing roombas of a certain type to change in said event. (I never used this for changing type, as all the roombas I built are meant to transition to the broken state when hit by the broom, but I do prevent all rombas other than those with i == 0 from being picked up by the player in [roomba_rampage](Games/Roomba_Rampage/cleaning-game/roomba_rampage.py) under the comment that says "Simulate Roombas.") I'll admit that this method is a bit rougher and less neat than the method you taught us, but I feel it's more versitile. From what I can tell, the FSM is only capable of running one method in the object based on it's state, but in my method anything about the object (even it's sprite) can vary based on it's state. | y |
|path planning                      | I didn't use path planning in Roomba Rampage. | n |
|Tree Search                        | I didn't use Tree Search in Roomba Rampage. I would be upset that tree search and path planning both count against me, but I have platformer physics and vector math as two sepparet things so I guess it's fare.| n |
|sprites                            | Almost everything in this game was a sprite. [Here](Games/Roomba_Rampage/cleaning-game/start_button.py)'s an example!| y |
|sprite sheets and animation        | Ok. So *technically* I didn't use a sprite sheet b/c | y |
|rotating sprites                   | Matt figured out how to get the sprite for the [broom](Games/Roomba_Rampage/cleaning-game/broom.py) to rotate, and, through looking at his code, I figured out how to get the sprites for the [roombas](Games/Roomba_Rampage/cleaning-game/roomba_rework_2.py) to rotate in the direction the player faces. | y |
|pygame API                         | I mean, come on. | y |
|clients and servers                | I didn't use clients and/or servers in Roomba Rampage.| n |
|hitboxes as separate objects       | In Roomba Rampage, I split the player character into two objects: the [hitbox](Games/Roomba_Rampage/cleaning-game/sweeper_hitbox.py), which manages the physics, controlls, collision, and other such things, and the [sprite](Games/Roomba_Rampage/cleaning-game/sweeper.py), which displays the sprite to the screen and manages the animation. I did this mainly so that I could have the players hitbox be sepparate from it's sprite, as I felt it would be weird if they got hit in the head by a roomba that's on the ground.| y |

Sadly, I the final project only demonstrated 80% of the concepts that I learned in class. This still makes the requirement for a B, which asks I demonstrate at least 70%, but I didn't make the requirement to get an A. (I think the main reason I didn't make this requirement was that I focused too much on making the game I wanted to and too little on the game I had to. I definitely had the time and capability to implement all of the features, I just forgot I had to.)

## Submit documented revisions of all programming assignments.
This one really stings. In the [README](Games/README.md) file in the Games folder, I have a chart with all games and info about them. One of these colomns (titled "required revisions") shows whether the game required a revision or not, and all the ones that did have a y that links to the Final Draft of the project with revisions. I wasn't going to penalize myself for not making revisions for games John told me not to revise, but there were two games I submitted late and John didn't have time to make revisions for. Even though it's possible that John would have told me the games didn't need to be revised, that's not an assumption I can make. Thus, I have to not give myself credit for this one, keeping my grade at a B.

## Complete at least two challenges (on average) for each programming assignment.
In the same chart in the [README](Games/README.md) file in the Games folder, there is a colomn with the number of completed challenges for each game and links to their DevDiaries with the proof. I'm not gonna lie, I scrambled together a good number of these challenges while writing this portfolio, but I completed a total of 12 challenges out of a total of 6 games. (I think it's fair to exclude the Networking game from this calculation, as the Nexus page doesn't have a challenge section and the "Next Steps" section doesn't feel like a propper replacement.) Thus, I believe I made this requirement for an A.

## *Complete on average 2 personal optional challenges (worthyness by John's discretion) for each programming assignment.*
Of the personal challenges I made for myself, (list and proof also in [this](Games/README.md) chart.) I made a toatal of about 2.8 per assignment. John (you) can go through them and not count any he thinks aren't worthy. If he decides to do that, if the average is still above 2 I made this requirement for an A. Otherwise, this would be another requirement for an A I do not make.

## Write a clear explainer for your classmates on obtuse math/physics/CS concepts that are covered only lightly in the class. (Removed in replacement contract.)
I, uhh, never got around to this one. I forgot I had put in in my Contract for most of the term and when I remembered there were already no more classes for the term. If my replacement contract doesn't cut it, this is another requirement I failed to meet for an A.

## *Write all README and Dev_Diary documents for programming assignments neatly and thoroughly.*
I added this requirement in for the [replacement_contract](Contract/Hopeful_Replacement_Grading_Contract.MD) because I feel like I've always put in a sizeable amount of pollish in my README and DevDiary files, more so than I felt was required, and I believe that I deserve something for the effort I put in. In my opinion, I've met this requirement for an A, but ultimately it's up to you (John.) Below is a chart with all README and DevDiary files for you to judge. (Ps. The files for the first assignment are the worst ones because that assingment was split up into three parts and I wasn't sure how to organize it. Just make sure you look at at least the first few if you look at any.)

| Game                              | README | DevDiary | 
| -------                           | ------- | ------- |
[Baselines](Baselines)              |[README](Games/Baselines/Final_Baselines/README.md)|[DevDiary](Games/Baselines/Final_Baselines/DevDiary.MD)|
|[Breakout](Breakout)               |[README](Games/Breakout/Final_Breakout/README.md)|[DevDiary](Games/Breakout/Final_Breakout/DevDiary.MD)|
|[Sprites](Sprites)                 |[README](Games/Sprites/Draft_Sprites/README.MD)|[DevDiary](Sprites/Draft_Sprites/DevDiary.MD)|
|[Flocking](Flocking)               |[README](Games/Flocking/Draft_Flocking/README.md)|[DevDiary](Games/Flocking/Draft_Flocking/DevDiary.MD)
|[FSMs](FSMs)                       |[README](Games/FSMs/Draft_FSMs/README.md) |[DevDiary](FSMs/Draft_FSMs/DevDiary.md)|
|[Path_Planning](Path_Planning)     |[README](Games/Path_Planning/Draft_Path_Planning/README.md)|[DevDiary](Path_Planning/Draft_Path_Planning/DevDiary.MD)|
|[Networking](Networking)           |[README](Games/Networking/Draft_Networking/README.md)|[DevDiary](Games/Networking/Draft_Networking/DevDiary.md)|
|[Roomba_Rampage](Roomba_Rampage)   |[README](Games/Roomba_Rampage/cleaning-game/README.md)|[DevDiary](Games/Roomba_Rampage/cleaning-game/DevDiary.md) |

## Conclusion:
Based on the evidence above, I have come to the conclusion that I deserve a B for this class. I missed 2 to 3 of my contract requirements to get an A (depending on which contract you look at), but I did meet the backup requirements to make a B. Looking back, I feel I easily could have gotten an A. If I had only been more careful when writing my contract or spent more time checking to make sure that I was on track to meet my requirements, I'm sure this would have been a different story. Oh well.

# Final Score: B

(but, ya know, maybe a B+ isn't impossibe. I mean look at how much effort I put into Roomba Rampage. I spent at least 40 hours working on that thing! Alright, I'll go now.)