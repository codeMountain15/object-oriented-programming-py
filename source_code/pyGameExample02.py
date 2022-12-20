# pyGameExample02.py

"""
 Implelenting pygame library
 for a simple python program
 that opens a new window,
 shows a text message
 and changes its color
 with the keyboard arrows
"""

import pygame
 
# Define the color options
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define the dimensions
width = 800
height = 500

# power up the pygame library
pygame.init()

# Set the window dimensions [width, height]
window_dimensions = (width, height)
surfaceObject = pygame.display.set_mode(window_dimensions)

# Set the window title
pygame.display.set_caption("Warming up for Object Oriented Programming with Python")

 
# create a font object
# freesansbold.ttf is the font file
# that is already in pygame
# 40 is the font size
fontObject = pygame.font.Font('freesansbold.ttf', 40)

# for the loop
exit = False

nextColor = BLUE

# main program loop
while not exit:

    # create a blue message on the surface of the font object
    # the font color is stored in the nextColor variable
    # antialias is True, so the characters will have smooth edges
    message = fontObject.render('Don\'t forget to submit the WnV project!', True, nextColor)
 
    # create a rectangular object for the
    # text surface object
    textRectObject = message.get_rect()
 
    # set the center of the rectangular object
    # in the center of the canvas
    textRectObject.center = (width / 2, height / 2)
 
    # fill the surface object
    # with white color
    surfaceObject.fill(WHITE)
 
    # copy the message (=text surface object)
    # to the surface object
    # at the coordinates mentrined above
    surfaceObject.blit(message, textRectObject)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
        # keyboard arrows
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            nextColor = RED
        if keys[pygame.K_RIGHT]:
            nextColor = BLUE
        if keys[pygame.K_UP]:
           nextColor = GREEN
        if keys[pygame.K_DOWN]:
            nextColor = BLACK

        # Draws the surface object on the screen
        pygame.display.update()
        # instead of
        #pygame.display.flip()

# Close the window
pygame.quit()
