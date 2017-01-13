
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 255, 0)

PI = 3.141592653

pygame.init()

size = (1000, 650)
screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

#title import
title_text = pygame.image.load("DuckGameImages/PondDefendersTitle.png").convert()
title_text.set_colorkey(WHITE)


#duck player image
duck_shooter = pygame.image.load("DuckGameImages/duckShooter.png").convert()
duck_shooter.set_colorkey(RED)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

class speed():
    def x_speed(self):
        !!!! KEEP WORKING ON THIS

shot_y_speed = 0
shot_y1_speed = 0
shot_y2_speed = 0
shot_y3_speed = 0
shot_y4_speed = 0

# Current position
x_coord = 460
y_coord = 560

# current shot position
shot_x_coord = 460
shot_y_coord = 560

shot_x1_coord = 460
shot_y1_coord = 560

shot_x2_coord = 460
shot_y2_coord = 560

shot_x3_coord = 460
shot_y3_coord = 560

shot_x4_coord = 460
shot_y4_coord = 560

LEFT = True
RIGHT = True
UP = True
DOWN = True

SHOT = False
SHOT1 = False
SHOT2 = False
SHOT3 = False
SHOT4 = False
SHOT5 = False
SHOT6 = False

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
                x_speed += -10
            if event.key == pygame.K_RIGHT and x_coord <= 990:
                x_speed += 10

            #Shot code for shots
            if event.key == pygame.K_SPACE and SHOT == False:
                SHOT = True
                if shot_y_speed > -10:
                    shot_y_speed += -10
                else:
                    shot_y_speed = -10
            elif event.key == pygame.K_SPACE and SHOT1 == False:
                SHOT1 = True
                if shot_y1_speed > -10:
                    shot_y1_speed += -10
                else:
                    shot_y1_speed = -10
            elif event.key == pygame.K_SPACE and SHOT2 == False:
                SHOT2 = True
                if shot_y2_speed > -10:
                    shot_y2_speed += -10
                else:
                    shot_y2_speed = -10
            elif event.key == pygame.K_SPACE and SHOT3 == False:
                SHOT3 = True
                if shot_y3_speed > -10:
                    shot_y3_speed += -10
                else:
                    shot_y3_speed = -10
            elif event.key == pygame.K_SPACE and SHOT4 == False:
                SHOT4 = True
                if shot_y4_speed > -10:
                    shot_y4_speed += -10
                else:
                    shot_y4_speed = -10



        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed += 10
            if event.key == pygame.K_RIGHT:
                x_speed += -10
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

    #shot
    if SHOT == False:
        shot_y_coord += y_speed
        shot_x_coord += x_speed
    elif SHOT == True:
        shot_y_coord += shot_y_speed
    if shot_y_coord <= 0:
        SHOT = False
        shot_y_coord = y_coord
        shot_x_coord = x_coord
    #shot1
    if SHOT1 == False:
        shot_y1_coord += y_speed
        shot_x1_coord += x_speed
    elif SHOT1 == True:
        shot_y1_coord += shot_y1_speed
    if shot_y1_coord <= 0:
        SHOT1 = False
        shot_y1_coord = y_coord
        shot_x1_coord = x_coord
    #shot2
    if SHOT2 == False:
        shot_y2_coord += y_speed
        shot_x2_coord += x_speed
    elif SHOT2 == True:
        shot_y2_coord += shot_y2_speed
    if shot_y2_coord <= 0:
        SHOT2 = False
        shot_y2_coord = y_coord
        shot_x2_coord = x_coord
    #shot3
    if SHOT3 == False:
        shot_y3_coord += y_speed
        shot_x3_coord += x_speed
    elif SHOT3 == True:
        shot_y3_coord += shot_y3_speed
    if shot_y3_coord <= 0:
        SHOT3 = False
        shot_y3_coord = y_coord
        shot_x3_coord = x_coord
    #shot4
    if SHOT4 == False:
        shot_y4_coord += y_speed
        shot_x4_coord += x_speed
    elif SHOT4 == True:
        shot_y4_coord += shot_y4_speed
    if shot_y4_coord <= 0:
        SHOT4 = False
        shot_y4_coord = y_coord
        shot_x4_coord = x_coord

    if x_coord < 0:
        x_coord = 0
    if x_coord > 940:
        x_coord =940
    if y_coord != 560:
        y_coord = 560
    if shot_x_coord < 0:
        shot_x_coord = 0
    if shot_x_coord > 940:
        shot_x_coord = 940
    if shot_x1_coord < 0:
        shot_x1_coord = 0
    if shot_x1_coord > 940:
        shot_x1_coord = 940
    if shot_x2_coord < 0:
        shot_x2_coord = 0
    if shot_x2_coord > 940:
        shot_x2_coord = 940
    if shot_x3_coord < 0:
        shot_x3_coord = 0
    if shot_x3_coord > 940:
        shot_x3_coord = 940
    if shot_x4_coord < 0:
        shot_x4_coord = 0
    if shot_x4_coord > 940:
        shot_x4_coord = 940

    print x_coord,y_coord
    print shot_y_coord
    if SHOT == True:
        print "SHOT"
    if SHOT1 == True:
        print "SHOT 111"
    if SHOT2 == True:
        print "SHOT 222"
    if SHOT3 == True:
        print "SHOT 333"
    if SHOT4 == True:
        print "SHOT 444"
    #defining the ball that shoots
    def shooting_motion(screen, x, y):
        #Shot
        pygame.draw.ellipse(screen, BLUE, [1+x,y,20,20], 0)
    def shooting_motion1(screen, x, y):
        #Shot
        pygame.draw.ellipse(screen, RED, [1+x,y,20,20], 0)
    def shooting_motion2(screen, x, y):
        #Shot
        pygame.draw.ellipse(screen, GREEN, [1+x,y,20,20], 0)
    def shooting_motion3(screen, x, y):
        #Shot
        pygame.draw.ellipse(screen, BLACK, [1+x,y,20,20], 0)
    def shooting_motion4(screen, x, y):
        #Shot
        pygame.draw.ellipse(screen, ORANGE, [1+x,y,20,20], 0)

    # --- Game logic should go here
    """
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    """

    # --- Drawing code should go here
    screen.fill(WHITE)

    shooting_motion(screen, shot_x_coord+23, shot_y_coord-5)
    shooting_motion1(screen, shot_x1_coord+23, shot_y1_coord-5)
    shooting_motion2(screen, shot_x2_coord+23, shot_y2_coord-5)
    shooting_motion3(screen, shot_x3_coord+23, shot_y3_coord-5)
    shooting_motion4(screen, shot_x4_coord+23, shot_y4_coord-5)


    screen.blit(duck_shooter, [x_coord, y_coord])

    screen.blit(title_text, [170, 5])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


