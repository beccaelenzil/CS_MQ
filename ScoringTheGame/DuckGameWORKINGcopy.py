
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

all_sprites_list = pygame.sprite.Group()
duck_bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()


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
        self.image = duck_shooter
        self.rect = self.image.get_rect()
        self.x_coord = 460
        self.y_coord = 560
        self.x_speed = 0
        self.y_speed = 0
    def update(self):
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
all_sprites_list.add(daffy)

class Basic_enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Basic_enemy, self).__init__()
        self.image = duck_hunter_enemy
        self.rect = self.image.get_rect()
        self.x_coord = 460
        self.y_coord = 60
        self.x_speed = random.randint(-7,-1) or random.randint(1,7)
        self.y_speed = 0
        self.LIVES = 2
    def update(self):
        if self.rect.x < 5:
            self.x_speed = random.randint(3,8)
        elif self.rect.x > 950:
            self.x_speed = random.randint(-8,-3)
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed






class Duck_bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Duck_bullet,self).__init__()

        self.image = pygame.Surface([10,20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += -20

SHOT = False




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



    if event.type == pygame.KEYDOWN and shot_count > 0:
        if event.key == pygame.K_SPACE and SHOT == False:
            duck_bullet = Duck_bullet()
            SHOT = True
            shot_count += -1
            duck_bullet.rect.x = daffy.x_coord + 32
            duck_bullet.rect.y = daffy.y_coord
            all_sprites_list.add(duck_bullet)
            duck_bullet_list.add(duck_bullet)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            SHOT = False

    #spawn enemies



    if round(second_count, 1)% 5 == 0:
        basic_enemy = Basic_enemy()
        basic_enemy.rect.x = random.randrange(1000)
        basic_enemy.rect.y = random.randint(50,100)
        all_sprites_list.add(basic_enemy)
        enemy_list.add(basic_enemy)

    if round(second_count,1)%5 == 0:
        print "ENEMY!!!!"

    minute_count = 37-second_count


    all_sprites_list.update()


    for bullet in duck_bullet_list:
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        

        if bullet.rect.y < -10:
            duck_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

        for block in enemy_hit_list:
            duck_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            hit_count += 1
            hit_sound.play()
            print(hit_count)




    print daffy.x_coord, daffy.y_coord


    # --- Drawing code should go here
    screen.fill(WHITE)

    all_sprites_list.draw(screen)



    screen.blit(duck_shooter, [daffy.x_coord, daffy.y_coord])



    if second_count < 5:
        screen.blit(title_text, [170, 250])

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


