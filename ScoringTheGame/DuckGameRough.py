
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


#duck player image
duck_shooter = pygame.image.load("duckShooter.png").convert()
duck_shooter.set_colorkey(RED)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

shot_y_speed = 0

# Current position
x_coord = 460
y_coord = 560

# current shot position
shot_x_coord = 460
shot_y_coord = 560


LEFT = True
RIGHT = True
UP = True
DOWN = True

SHOT = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    x = 0

    def shoot():
        x = 0
        for x in range(0, 10):
            pygame.draw.circle(screen, BLUE, [x_coord, y_coord-(5*x)], 10, 10)
            x += 1

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

            if event.key == pygame.K_SPACE:
                SHOT = True
                if shot_y_speed > -5:
                    shot_y_speed += -5
                else:
                    shot_y_speed = -5




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

    if SHOT == False:
        shot_y_coord += y_speed
        shot_x_coord += x_speed
    elif SHOT == True:
        shot_y_coord += shot_y_speed

    if shot_y_coord <= 40:
        SHOT = False
        shot_y_coord = y_coord
        shot_x_coord = x_coord


    if x_coord < 0:
        x_coord = 0
    if x_coord > 940:
        x_coord =940
    if y_coord != 560:
        y_coord = 560

    print x_coord,y_coord
    print shot_y_coord
    if SHOT == True:
        print "SHOT"
    #defining the ball that shoots
    def shooting_motion(screen, x, y):
        #Shot
        pygame.draw.ellipse(screen, BLUE, [1+x,y,20,20], 0)


    # --- Game logic should go here
    """
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    """

    # --- Drawing code should go here
    screen.fill(WHITE)

    shooting_motion(screen, shot_x_coord+23, shot_y_coord-15)

    screen.blit(duck_shooter, [x_coord, y_coord])

    screen.blit(title_text, [170, 5])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


