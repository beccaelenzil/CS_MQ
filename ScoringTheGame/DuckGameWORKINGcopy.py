
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

hit_count = 0

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

#hit sound temporary
hit_sound = pygame.mixer.Sound("DuckGameSoundEffects/laser5.ogg")


class duck(pygame.sprite.Sprite):
    def __init__(self):
        super(duck, self).__init__()
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


class basic_enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(basic_enemy, self).__init__()
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


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Bullet,self).__init__()

        self.image = pygame.Surface([6,15])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += -15

"""
class duck_shot(pygame.sprite.Sprite):
    def __init__(self):
        super(duck_shot, self).__init__()
        self.shot_x_coord = 460
        self.shot_y_coord = 560
        self.shot_y_speed = 0
        self.SHOT = False
        self.OKAY = False
        self.hit_count = 0
    def shot_moving(self):
        if self.SHOT == False:
            self.shot_x_coord = daffy.x_coord
            self.shot_y_coord = daffy.y_coord
    def shooting(self):
        if self.SHOT == True:
            self.shot_y_coord += -25
        if self.SHOT == False:
            self.shot_y_coord += daffy.y_speed
            self.shot_x_coord += daffy.x_speed
        elif self.SHOT == True:
            self.shot_y_coord += self.shot_y_speed
        if self.shot_y_coord <= 0:
            self.SHOT = False
            self.OKAY = False
            self.shot_y_coord = daffy.y_coord
            self.shot_x_coord = daffy.x_coord
        if self.shot_y_coord == 60 and self.shot_x_coord in range(enemy1.x_coord-35, enemy1.x_coord+30):
            hit_sound.play()
            self.hit_count += 1

shot1 = duck_shot()
shot2 = duck_shot()
shot3 = duck_shot()
shot4 = duck_shot()
shot5 = duck_shot()
"""

all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()


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



        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and shot1.SHOT == False:
                shot1.SHOT = True
            elif event.key == pygame.K_SPACE and shot1.SHOT == True:
                shot2.SHOT = True
        """



    if event.type == pygame.KEYDOWN and shot_count > 0:
        if event.key == pygame.K_SPACE:
            bullet = Bullet()
            bullet.rect.x = daffy.x_coord + 32
            bullet.rect.y = daffy.y_coord
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)





    minute_count = 37-second_count

    all_sprites_list.update()

    for bullet in bullet_list:

        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


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

    all_sprites_list.draw(screen)



    screen.blit(duck_shooter, [daffy.x_coord, daffy.y_coord])

    if second_count > 7:
        screen.blit(duck_hunter_enemy, [enemy1.x_coord, enemy1.y_coord])

    if second_count < 5:
        screen.blit(title_text, [170, 5])

    if second_count > second_count_limit:
        shot_count += 2
        second_count_limit += 1

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font2 = pygame.font.SysFont('Calibri', 40, True, False)
    shot_count_text = font.render("Shot count: " + str(shot_count),True,BLACK)
    hit_count_text = font.render("Hit count: " + str(hit_count),True,BLACK)
    minute_count_text = font2.render(str(round((minute_count),1)),True,BLACK)
    zero_text = font2.render("0",True, BLACK)
    screen.blit(shot_count_text, [830,5])
    screen.blit(hit_count_text, [20, 5])

    if minute_count < 30.5 and minute_count > 0:
        screen.blit(minute_count_text, [475,5])
    elif minute_count < 0:
        screen.blit(zero_text, [475,5])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


