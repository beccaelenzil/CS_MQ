
import pygame
import random
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 255, 0)

PI = 3.141592653

initial_second_count = time.time()

pygame.init()

size = (1000, 650)
screen = pygame.display.set_mode(size)

done = False

shot_count = 4
second_count_limit = 4

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

#title import
title_text = pygame.image.load("DuckGameImages/PondDefendersTitle.png").convert()
title_text.set_colorkey(WHITE)


#duck player image
duck_shooter = pygame.image.load("DuckGameImages/duckShooter.png").convert()
duck_shooter.set_colorkey(RED)

#duck shooter enemy image
duck_hunter_enemy = pygame.image.load("DuckGameImages/duck_hunter.png").convert()
duck_hunter_enemy.set_colorkey(WHITE)


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


class basic_enemy():
    def __init__(self):
        self.x_coord = 460
        self.y_coord = 60
        self.x_speed = random.randint(-7,-1) or random.randint(1,7)
        self.y_speed = 0
    def enemy_move(self):
        if self.x_coord < 5:
            self.x_speed = random.randint(3,8)
        elif self.x_coord > 950:
            self.x_speed = random.randint(-8,-3)
        self.x_coord += self.x_speed
        self.y_coord += self.y_speed

enemy1 = basic_enemy()


class duck_shot():
    def __init__(self):
        self.shot_x_coord = 460
        self.shot_y_coord = 560
        self.shot_y_speed = 0
        self.SHOT = False
    def shot_moving(self):
        if self.SHOT == False:
            self.shot_x_coord = daffy.x_coord
            self.shot_y_coord = daffy.y_coord
    def shooting(self):
        if self.SHOT == True:
            self.shot_y_coord += -10
        if self.SHOT == False:
            self.shot_y_coord += daffy.y_speed
            self.shot_x_coord += daffy.x_speed
        elif self.SHOT == True:
            self.shot_y_coord += self.shot_y_speed
        if self.shot_y_coord <= 0:
            self.SHOT = False
            self.shot_y_coord = daffy.y_coord
            self.shot_x_coord = daffy.x_coord

shot1 = duck_shot()
shot2 = duck_shot()
shot3 = duck_shot()
shot4 = duck_shot()
shot5 = duck_shot()




# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #time methods
    second_count = abs(initial_second_count - time.time())
    print second_count

    #defining the ball that shoots
    def shooting_motion(screen, x, y, color):
        #Shot
        pygame.draw.ellipse(screen, color, [1+x,y,20,20], 0)


    # --- Game logic should go here
    if second_count > 1:
        daffy.duck_move()

        shot1.shot_moving()
        shot2.shot_moving()
        shot3.shot_moving()
        shot4.shot_moving()
        shot5.shot_moving()

        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and shot1.SHOT == False:
                shot1.SHOT = True
            elif event.key == pygame.K_SPACE and shot1.SHOT == True:
                shot2.SHOT = True
        """


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and shot1.SHOT == False:
                shot1.SHOT = True
                shot_count += -1

            if event.key == pygame.K_SPACE and shot1.SHOT == True:
                shot2.SHOT = True
                shot_count += -1
        shot1.shooting()
        shot2.shooting()
        shot3.shooting()

        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and shot1.SHOT == True:
                shot2.SHOT = True
        shot2.shooting()
        """

        """
        if shot1.SHOT == False:
            shot1.shooting()
        if shot1.SHOT == True:
            shot2.shooting()
        if shot2.SHOT == True:
            shot3.shooting()

        shot2.shot_moving()
        shot2.shooting()

        shot3.shot_moving()
        shot3.shooting()

        shot4.shot_moving()
        shot4.shooting()

        shot5.shot_moving()
        shot5.shooting()
        """
        enemy1.enemy_move()

    print daffy.x_coord, daffy.y_coord

    # --- Drawing code should go here
    screen.fill(WHITE)

    shooting_motion(screen, shot1.shot_x_coord+23, shot1.shot_y_coord-5, BLUE)
    shooting_motion(screen, shot2.shot_x_coord+23, shot2.shot_y_coord-5, RED)
    shooting_motion(screen, shot3.shot_x_coord+23, shot3.shot_y_coord-5, BLACK)
    shooting_motion(screen, shot4.shot_x_coord+23, shot4.shot_y_coord-5, ORANGE)
    shooting_motion(screen, shot5.shot_x_coord+23, shot5.shot_y_coord-5, GREEN)


    screen.blit(duck_shooter, [daffy.x_coord, daffy.y_coord])

    if second_count > 7:
        screen.blit(duck_hunter_enemy, [enemy1.x_coord, enemy1.y_coord])

    if second_count < 5:
        screen.blit(title_text, [170, 5])

    if second_count > second_count_limit:
        shot_count += 4
        second_count_limit += 4

    font = pygame.font.SysFont('Calibri', 25, True, False)
    shot_count_text = font.render("Shot count: " + str(shot_count),True,BLACK)
    screen.blit(shot_count_text, [830,5])

    print "SHOT COUNT =" + str(shot_count)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


