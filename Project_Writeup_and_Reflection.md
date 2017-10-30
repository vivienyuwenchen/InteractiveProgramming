# Project Writeup and Reflection

### Project Overview [Maximum 100 words]

*Write a short abstract describing your project.*

Blockade is competitive arcade game. It has two players. Player 1 is a white block that is continually moving forward. Player 2’s job is to stop Player 1 by throwing obstacles in its way. Player 1 can avoid obstacles by jumping over or ducking under them. Both players are limited by a stamina bar. Actions such jumping or throwing obstacles depletes player’s stamina and if the stamina gets too low players cannot perform actions. The game uses keyboard inputs as commands.

### Results [~2-3 paragraphs + figures/examples]

*Present what you accomplished. This will be different for each project, but screenshots are likely to be helpful.*

The game starts with Player 1 on the bottom left corner of the screen. Player 1’s objective is simple, avoid obstacles and get as far as you can.  Player 1 can avoid obstacles by moving left, right or jumping. These actions are performed by pressing the Left, Right, and Up arrow keys respectively.  Player 2 does not show up on screen but can make is presence known by throwing obstacles at Player 1. These obstacles can be thrown at three heights: ground level, just over Player 1 and High in the air. Player 2 can control the height of the obstacles thrown by pressing the Z, X, and C keys. The game ends when Player 1 collides with an obstacle and dies, Player 1’s score is determined by how long they survived. The competitive nature of the game come when the human players swap roles. With both trying to ensure the other gets a lower score.

Player actions cost stamina. If a player’s stamina gets too low, they cannot perform any actions until it regenerates.  This adds another level of strategy to the game with each player trying to force the other to deplete their stamina bar. In the game, Player 2’s strategy heavily relies on forcing Player 1 to run out of stamina.

We playtested the game with around 9 individuals. Each person played at least one game as both players. Reviews were generally positive with testers describing it as "fascinating" and "A few minutes of mindless fun".


![screenshot1](https://github.com/vivienyuwenchen/InteractiveProgramming/blob/master/screenshot1.png)

Figure 1: This is how the game starts.  Player 1 is the white square in the bottom left corner. PLayer 1’s distance is in the top center of the screen. The stamina bars for Player 1 and 2 are in the top left and right screen respectively.

![screenshot2](https://github.com/vivienyuwenchen/InteractiveProgramming/blob/master/screenshot2.png)

Figure 2: During the game Player 1 avoids the red obstacles by jumping. Player 2 can spawn red obstacles at multiple heights. Player 2’s staminal bar(red) has almost been depleted.

![screenshot3](https://github.com/vivienyuwenchen/InteractiveProgramming/blob/master/screenshot3.png)

Figure 3: Game over screen reports the distance Player 1 traveled and gives instructions for how to play again.

### Implementation [~2-3 paragraphs + UML diagram]

*Describe your implementation at a system architecture level. Include a UML class diagram, and talk about the major components, algorithms, data structures and how they fit together. You should also discuss at least one design decision where you had to choose between multiple alternatives, and explain why you made the choice you did.*

Our minimum viable product was a one player game similar to Google Chrome's dino run, in which the player jumps over randomly generated obstacles. The first class we created was for the main game. Its init handled the main initialization of the game. The mainLoop was a method that ran the main loop of the game, which got keyboard inputs and used them to control the player (and later the obstacles). We created two other classes. Unsurprisingly, they were the player and the obstacle. The obstacle only needed to move forward, so it had a moveForward method aside from init and repr, as well as isGone, used to delete obstacles off screen to prevent the programming from crashing from having to keep track of too many obstacles. The player had more requirements, such as moving left, moving right, and jumping, so we created the methods accordingly. We also added a method for collision detection in order to determine when game over should happen. We then created a gameOver method inside the main class game. We included a conditional statement in the mainLoop to direct the program to gameOver when the player collides with any obstacle and a conditional in gameOver to direct the program back to mainLoop when the space key is pressed.

We got our MVP done by the mid-project check-in, so we added additional features to allow a second player to control the obstacles. We then created another class for the stamina bar, with one method to decrease the bar with every action (i.e. when the player jumps for the player's stamina bar and when an obstacle is generated for the second player's stamina bar) and increase the bar over time up to a certain length.

At one point, we considered implementing Model View Control. However, given the simplicity of our game, it wasn't worth rewriting whole sections just to split up the view and control into different classes. It would have cut down on the length of our mainLoop, but the pros just didn't outweigh the cons. Another decision that we made was to not create a subclass for each of the stamina bars since we only needed two and their only differences were their color and location, so we took those parameters as arguments instead.

![UML](https://github.com/vivienyuwenchen/InteractiveProgramming/blob/master/UML.png)

### Reflection [~2 paragraphs]

*From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?*

*Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by class, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time?*

Overall, this project went pretty well. We were able to deliver our MVP as well as a few of our stretch goals, like allowing a second player to generate obstacles and adding stamina bars, a scorekeeper, and a display of the score on the game over screen. For the most part, we planned on and were able to divide up the work based on what we wanted to complete within a period of time. We didn't look that far ahead, but planned at the beginning of each of our meetings what we wanted accomplished and divided the work as evenly as possible. Harry developed the main player and Vivien developed the obstacles. Once we made the two players, we both fixed bugs as they came up.

One problem we ran into was keeping a consistent class format. We developed the two players independently and as a result each player was done a little differently. We refactored the main player into an object in order to keep them consistent with each other. For the most part, we were able to effectively work independently and met up to either discuss future features for the project or how to fix bugs.

For a project of this scope our teamwork strategy was appropriate. However, it is not scalable. For larger projects we should spend more time planning out the classes so they can be easily integrated.  We also tried to implement a CMV structure into the game; however, by that point most of the game had been written and changing the structure was deemed not worth the effort. If we were to do this project again we would have implement CMV from the beginning.

Unfortunately, Vivien's family came to visit the weekend before the project was due, so she could not spend as much time adding more features to the game as Harry really wanted to do. However, since we got quite a lot done early on, Vivien was able to spend time with her family and Harry just added some of the things he wanted to add.
