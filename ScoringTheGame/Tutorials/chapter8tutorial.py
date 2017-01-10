
import pygame

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653

# Set the height and width of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Matt's Sick Box Rider Game")

done = False

clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_change_x = 15
rect_change_y = 15

while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GREEN)


    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > 450:
        rect_change_y = rect_change_y * -1
    if rect_x > 650:
        rect_change_x = rect_change_x * -1
    if rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x < 0:
        rect_change_x = rect_change_x * -1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()



    # --- Limit to 60 frames per second
    clock.tick(60)
