
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




class duck():
    def __init__(self):
        self.x_coord = 460
        self.y_coord = 560
        self.x_speed = 0
        self.y_speed = 0
    def duck_move(self):
        if event.type == pygame.KEYDOWN  and -11< self.x_speed < 11:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT and self.x_coord >= 0:
                if self.x_speed != -10:
                    self.x_speed += -10
            if event.key == pygame.K_RIGHT and self.x_coord <= 990:
                if self.x_speed != 10:
                    self.x_speed += 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if self.x_speed == -10:
                    self.x_speed += 10
            if event.key == pygame.K_RIGHT:
                if self.x_speed == 10:
                    self.x_speed += -10
        if self.x_coord < 0:
            self.x_coord = 0
        if self.x_coord > 940:
            self.x_coord =940
        if self.y_coord != 560:
            self.y_coord = 560

        self.x_coord += self.x_speed
        self.y_coord += self.y_speed

daffy = duck()


class shot():
    def __init__(self):
        self.shot_x_coord = 460
        self.shot_y_coord = 560
        self.y_speed = 0
        self.SHOT = False
    def shot_moving(self):
        if self.SHOT == False:
            self.shot_x_coord = daffy.x_coord
            self.shot_y_coord = daffy.y_coord
    def shooting(self):
        if event.key == pygame.K_SPACE:
            self.SHOT = True
            if self.shot_y_speed > -10:
                self.shot_y_speed += -10
            else:
                self.shot_y_speed = -10
            if self.SHOT == False:
                self.shot_y_coord += daffy.y_speed
                self.shot_x_coord += daffy.x_speed
            elif self.SHOT == True:
                self.shot_y_coord += shot1.y_speed
            if self.shot_y_coord <= 0:
                self.SHOT = False
                self.shot_y_coord = daffy.y_coord
                self.shot_x_coord = daffy.x_coord

shot1 = shot()
shot2 = shot()
shot3 = shot()
shot4 = shot()
shot5 = shot()




# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    #defining the ball that shoots
    def shooting_motion(screen, x, y, color):
        #Shot
        pygame.draw.ellipse(screen, color, [1+x,y,20,20], 0)


    # --- Game logic should go here


    daffy.duck_move()
    shot1.shot_moving()
    shot2.shot_moving()
    shot3.shot_moving()
    shot4.shot_moving()
    shot5.shot_moving()
    shot1.shooting()

    print daffy.x_coord, daffy.y_coord

    # --- Drawing code should go here
    screen.fill(WHITE)

    shooting_motion(screen, shot1.shot_x_coord+23, shot1.shot_y_coord-5, BLUE)
    shooting_motion(screen, shot2.shot_x_coord+23, shot2.shot_y_coord-5, RED)
    shooting_motion(screen, shot3.shot_x_coord+23, shot3.shot_y_coord-5, BLACK)
    shooting_motion(screen, shot4.shot_x_coord+23, shot4.shot_y_coord-5, ORANGE)
    shooting_motion(screen, shot5.shot_x_coord+23, shot5.shot_y_coord-5, GREEN)


    screen.blit(duck_shooter, [daffy.x_coord, daffy.y_coord])

    screen.blit(title_text, [170, 5])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


