import pygame

# initiate pygame with all the modules
pygame.init()

# setup windows/surface
# 800 width, 600 height

# explicitly define to be able to refer to later
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

# define colors (RGB)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# Window title
pygame.display.set_caption('My game')

# define the game clock for timing feature
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')

def car(x,y):
    # place the car to the display
    gameDisplay.blit(carImg, (x,y))

# Initial car location
x = (display_width * 0.45)
y = (display_height * 0.8)

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

    # pour white color on display
    gameDisplay.fill(white)
    car(x,y)
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
