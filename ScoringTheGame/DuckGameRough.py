
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653

pygame.init()

size = (1000, 650)
screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

#title import
title_text = pygame.image.load("PondDefendersTitle.png").convert()
title_text.set_colorkey(WHITE)
screen.blit(title_text, 150, 30)

#duck player image
duck_shooter = pygame.image.load("duckShooter.png").convert()
duck_shooter.set_colorkey(RED)

# Speed in pixels per frame
x_speed = 0
y_speed = 0


# Current position
x_coord = 400
y_coord = 540

LEFT = True
RIGHT = True
UP = True
DOWN = True

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True





        # User let up on a key
        elif event.type == pygame.KEYDOWN:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT and x_coord >= 0:
                x_speed += -7
            if event.key == pygame.K_RIGHT and x_coord <= 990:
                x_speed += 7
            if event.key == pygame.K_UP and y_coord >= 0:
                y_speed += -7
            if event.key == pygame.K_DOWN and y_coord <= 640:
                y_speed += 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0



    if y_coord < 0:
        UP = False
        y_speed = 0
    elif y_coord > 0:
        UP = True
    elif y_coord > 990:
        DOWN = False
        y_speed = 0
    elif y_coord < 990:
        DOWN = True

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    if x_coord < 0:
        x_coord = 0
    if x_coord > 920:
        x_coord =920
    if y_coord != 540:
        y_coord = 540

    print x_coord,y_coord

    # --- Game logic should go here
    """
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    """

    # --- Drawing code should go here
    screen.fill(WHITE)


    screen.blit(duck_shooter, [x_coord, y_coord])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


