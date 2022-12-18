# pyGameExample01.py

"""
 Implelenting pygame library
 for a simple python program
 that opens a new window
 and changes its color
 with the keyboard arrows
"""

import pygame

# Define the color options
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# power up the pygame library
pygame.init()

# Set the window dimensions [width, height]
window_dimensions = (700, 500)
screen = pygame.display.set_mode(window_dimensions)

# Set the window title
pygame.display.set_caption("Di codes with Python")

# for the loop
exit = False

# control the screen update speed
screen_update = pygame.time.Clock()

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

        # update window with what we drew
        pygame.display.flip()

        # see above: screen_update = pygame.time.Clock()
        # set the limit to 60 frames per second
        screen_update.tick(60)
        # however, it is not necessary
        # in this example

# Close the window and exit
pygame.quit()
