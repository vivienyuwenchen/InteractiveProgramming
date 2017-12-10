"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""



import pygame
from playermoves import *


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
jumping = False
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
frames = 0;
startjump = 0
x_min = 0
x_max = 200
rectx = 100
recty = 400

# -------- Main Program Loop -----------
while not done:

    # --- Main event loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #if event.type == pygame.KEYDOWN:
#
 #           if event.key == pygame.K_SPACE:
  #              if frames - startjump > 20:
   #                 jumping = True
    #                startjump = frames

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        if frames - startjump > 20:
                jumping = True
                startjump = frames  
    if pressed[pygame.K_LEFT]:
        if rectx > x_min:
            rectx -= 5      
    if pressed[pygame.K_RIGHT]:
        if rectx < x_max:
            rectx += 5  


  


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [0,425,700,100])
    jumpclock = frames%21

    # --- Drawing code should go here
    # --- Drawing code should go here
    
    jumpover = False
    
    #if False:#if detect_key_press() == 'space':
    #    jumping = True                 #if the spacebar is pressed start the jump
    #    print("boing")
    #else:
     #   print(detect_key_press())
    if jumping == True:
        recty = jump(frames-startjump+1,300)[0]
        jumpover = jump(frames-startjump+1,300)[1]
    if jumpover == True:
       
        jumping = False

    pygame.draw.rect(screen, WHITE, [rectx,recty,25,25])
    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()
    frames+=1 # increments frame count

    # --- Limit to 60 frames per second
    clock.tick(60)


# Close the window and quit.
pygame.quit()
