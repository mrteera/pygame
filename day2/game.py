import pygame
import time

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
car_width = 73

def car(x,y):
    # place the car to the display
    gameDisplay.blit(carImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    # I think pygame expect to handle all events before update the display
    pygame.event.get()
    pygame.time.wait(1000)
    game_loop()

def crash():
    message_display('You crashed')

def game_loop():
    # Initial car location
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    # Game loop
    # if the game crash exit the game
    gameExit = False

    while not gameExit:
        # get any events that happen
        # e.g. mouse, keyboard
        for event in pygame.event.get():
            # if x button (close window)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            # if the key has been released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        # pour white color on display
        gameDisplay.fill(white)
        car(x,y)

        # x is on top left of the car
        if x > display_width - car_width or x < 0:
            crash()


        # display after the above processing
        pygame.display.update()

        # move the frame on, define frame per second
        # how fast we want to update the frame
        # e.g. 30 fps
        clock.tick(60)

game_loop()
# stop pygame
pygame.quit()
# quit the program
quit()
