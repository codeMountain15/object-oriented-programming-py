# pyGameExample02.py

import pygame
 
# Define the color options
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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
 
# create a blue message on the surface of the font object
# the fonte color is BLUE in this example
# antialias is True, so the characters will have smooth edges
message = fontObject.render('Fon\'t forget to submit the WnV project!', True, BLUE)
 
# create a rectangular object for the
# text surface object
textRect = message.get_rect()
 
# set the center of the rectangular object.
textRect.center = (width / 2, height / 2)
 
# fill the surface object
# with white color
surfaceObject.fill(WHITE)
 
# copying the text surface object
# to the display surface object
# at the center coordinate.
surfaceObject.blit(message, textRect)

# for the loop
exit = False

# main program loop
while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        
        # keyboard arrows
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.fill(RED)
        if keys[pygame.K_RIGHT]:
            screen.fill(BLUE)
        if keys[pygame.K_UP]:
            screen.fill(GREEN)
        if keys[pygame.K_DOWN]:
            screen.fill(WHITE)

        # Draws the surface object on the screen
        pygame.display.update()
        # instead of
        #pygame.display.flip()

# Close the window
pygame.quit()
