import pygame

# initiate pygame with all the modules
pygame.init()

# setup windows/surface
# 800 width, 600 height
gameDisplay = pygame.display.set_mode((800,600))

# Window title
pygame.display.set_caption('My game')

# define the game clock for timing feature
clock = pygame.time.Clock()

# Game loop
# if the game crash exit the game
crashed = False

while not crashed:
    # get any events that happen
    # e.g. mouse, keyboard
    for event in pygame.event.get():
        # if x button (close window)
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    # display after the above processing
    pygame.display.update()

    # move the frame on, define frame per second
    # how fast we want to update the frame
    # e.g. 30 fps
    clock.tick(30)

# stop pygame
pygame.quit()
# quit the program
quit()
