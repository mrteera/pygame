import pygame
import random

# initiate pygame with all the modules
pygame.init()

crash_sound = pygame.mixer.Sound("./Car_Impact_and_scrape.wav")
pygame.mixer.music.load('./Joy_to_the_World_Jazz.wav')
pygame.mixer.music.play(-1)

# setup windows/surface
# 800 width, 600 height

# explicitly define to be able to refer to later
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

# define colors (RGB)
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

# Window title
pygame.display.set_caption('My game')

# define the game clock for timing feature
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png')
car_width = 73

pause = False

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0,0))


def things(thingx, thingy, thingw, thingh, color):
    # draw a box to the screen
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

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
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    message_display('You crashed')

# ic: inactive color, ac: active color
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    # (left, middle, right) button click
    click = pygame.mouse.get_pressed()

    # 150 << x-coordinate + 100 (width)
    # right side of the box
    # 4550+50 << bottom of the box
    # replace 150 with x
    # replace 450 with y
    # replace 100 with w
    # replace 50 with h
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            # if action == 'play':
            #     game_loop()
            # elif action == 'quit':
            #     pygame.quit()
            #     quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    # center at x coordinate and y coordinate
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def quitegame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():
    while pause:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects('Paused', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        # pass game_loop object
        button('Continue', 150, 450, 100, 50, green, bright_green, unpause)
        button('Quit', 500, 450, 100, 50, red, bright_red, quitegame)

        pygame.display.update()
        clock.tick(15)

# a separate sequence, just one time run
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects('Fast and Furious', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        # pass game_loop object
        button('Go!', 150, 450, 100, 50, green, bright_green, game_loop)
        button('Quit', 500, 450, 100, 50, red, bright_red, quitegame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    # Initial car location
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    # starting values for thing
    thing_startx = random.randrange(0, display_width)
    # 600 px off the screen
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0

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
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    x_change = 20
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            # if the key has been released
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        # pour white color on display
        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, black)
        # add 7 px to y of thing every frame
        thing_starty += thing_speed

        car(x,y)

        things_dodged(dodged)

        # x is on top left of the car
        if x > display_width - car_width or x < 0:
            crash()
        # check thing if off the screen
        # y measure from top down
        if thing_starty > display_height:
            # immediately shows thing after it goes off
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 0.5

        # check things over the car
        if y < thing_starty+thing_height:
            # check top left and top right of the car if it's inside bottom of the box
            if x > thing_startx and x < thing_startx+thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
                crash()


        # display after the above processing
        pygame.display.update()

        # move the frame on, define frame per second
        # how fast we want to update the frame
        # e.g. 30 fps
        clock.tick(60)

if __name__ == "__main__":
    game_intro()
    game_loop()
    # stop pygame
    pygame.quit()
    # quit the program
    quit()
