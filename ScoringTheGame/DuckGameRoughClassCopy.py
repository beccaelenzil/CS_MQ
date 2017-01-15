
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



class duck():
    def __init__(self):
        self.x_coord = 460
        self.y_coord = 560
        self.x_speed = 0
        self.y_speed = 0
    def move(self):
        if event.type == pygame.KEYDOWN:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT and self.x_coord >= 0:
                self.x_speed += -10
            if event.key == pygame.K_RIGHT and self.x_coord <= 990:
                self.x_speed += 10
        if self.x_coord < 0:
            self.x_coord = 0
        if self.x_coord > 940:
            self.x_coord =940
        if self.y_coord != 560:
            self.y_coord = 560

daffy = duck()


class shot():
    def __init__(self):
        self.shot_x_coord = 460
        self.shot_y_coord = 560
        self.y_speed = 0
        self.SHOT = False
    def shooting(self):
        if event.key == pygame.K_SPACE:
            self.SHOT = True
            if self.shot_y_speed > -10:
                self.shot_y_speed += -10
            else:
                self.shot_y_speed = -10
            if self.SHOT == False:
                self.shot_y_coord += y_speed
                self.shot_x_coord += x_speed
            elif self.SHOT == True:
                self.shot_y_coord += shot1.y_speed
            if self.shot_y_coord <= 0:
                self.SHOT = False
                self.shot_y_coord = y_coord
                self.shot_x_coord = x_coord

shot1 = shot()
shot2 = shot()
shot3 = shot()
shot4 = shot()
shot5 = shot()




# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    def shoot():
        x = 0
        for x in range(0, 10):
            pygame.draw.circle(screen, BLUE, [x_coord, y_coord-(5*x)], 10, 10)
            x += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            #Shot code for shots
            if event.key == pygame.K_SPACE and SHOT == False:
                SHOT = True
                if shot_y_speed > -10:
                    shot_y_speed += -10
                else:
                    shot_y_speed = -10



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

    shooting_motion(screen, shot1.shot_x_coord+23, shot1.shot_y_coord-5)
    shooting_motion(screen, shot2.shot_x_coord+23, shot2.shot_y_coord-5)
    shooting_motion(screen, shot3.shot_x_coord+23, shot3.shot_y_coord-5)
    shooting_motion(screen, shot4.shot_x_coord+23, shot4.shot_y_coord-5)
    shooting_motion(screen, shot5.shot_x_coord+23, shot5.shot_y_coord-5)


    screen.blit(duck_shooter, [daffy.x_coord, daffy.y_coord])

    screen.blit(title_text, [170, 5])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


