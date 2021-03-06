
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
duck_character_list = pygame.sprite.Group()
duck_bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
enemy_bullet_list = pygame.sprite.Group()

#actual list to put enemies
enemy_actual_list = []


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

#death screm
death_scream = pygame.mixer.Sound("DuckGameSoundEffects/starwarsscrem.ogg")

#duck quack
duck_quack = pygame.mixer.Sound("DuckGameSoundEffects/Quack2.ogg")

#song track
song_track = pygame.mixer.Sound("DuckGameSoundEffects/ThemeSong.ogg")

song_track.set_volume(.1)

#High quack
high_quack = pygame.mixer.Sound("DuckGameSoundEffects/ThemeSong.ogg")

class duck(pygame.sprite.Sprite):
    def __init__(self):
        super(duck, self).__init__()
        self.image = duck_shooter
        self.rect = self.image.get_rect()
        self.x_coord = 460
        self.y_coord = 560
        self.x_speed = 0
        self.y_speed = 0



daffy = duck()
all_sprites_list.add(daffy)
duck_character_list.add(daffy)
daffy.rect.x = 450

class Duck_bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Duck_bullet,self).__init__()

        self.image = pygame.Surface([25,20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += -20

class Basic_enemy_bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(Basic_enemy_bullet,self).__init__()

        self.image = pygame.Surface([15,25])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y += 10

class Basic_enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Basic_enemy, self).__init__()
        self.image = duck_hunter_enemy
        self.rect = self.image.get_rect()
        self.x_coord = 460
        self.y_coord = 60
        self.x_speed = random.randint(-7,7)
        self.y_speed = 0
        self.LIVES = 2

    def update(self):
        if self.x_speed == 0:
            self.x_speed = 5
        if self.rect.x < 5:
            self.x_speed = random.randint(3,8)
        elif self.rect.x > 950:
            self.x_speed = random.randint(-8,-3)
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

    def shot(self):
        Basic_enemy_bullet()


def enemies_list_for_random():
    basic_enemy = Basic_enemy()

    basic_enemy.rect.x = random.randrange(1000)
    basic_enemy.rect.y = random.randint(50,100)

    all_sprites_list.add(basic_enemy)
    enemy_list.add(basic_enemy)

    enemy_actual_list.append(basic_enemy)


def instructions():
    print "welcome to pond defenders"

def levelOne():
    print "level 1"

def main():
    instructions()
    levelOne()


SHOT = False

ENEMY_SPAWN = False
ENEMY_SHOOT1 = False

YOU_DEAD = False

SUPPOSED_SECOND_COUNT = 5
SUPPOSED_ENEMY_COUNT = 4

number_of_enemies = 0

def restartMenu():
    screen.fill(WHITE)
    screen.blit(title_text, [170,100])
    pygame.display.flip()

song_track.play()

def menu():
    START = False
    screen.fill(WHITE)
    screen.blit(title_text, [170,100])
    pygame.display.flip()
    while START == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    START = True


menu()

initial_second_count = time.time()

duck_spawn = 0

# -------- Main Program Loop -----------
while not done:

        #time methods
    second_count = round(abs(initial_second_count - time.time()), 0)

    second_count_with_decimals = round(abs(initial_second_count - time.time()), 1)


    # --- Main event loop
    if YOU_DEAD == True:
        secondCountReset = second_count
        while YOU_DEAD == True:
            restartMenu()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        all_sprites_list.add(daffy)
                        pause_done = round(time.time(),1)
                        second_count = secondCountReset
                        hit_count = 0
                        daffy.x_speed = 0
                        YOU_DEAD = False
                        duck_spawn = second_count + 3


    if duck_spawn == second_count:
        duck_character_list.add(daffy)

    # --- Game logic should go here
    if SUPPOSED_SECOND_COUNT < second_count:
        SUPPOSED_SECOND_COUNT = second_count +2


    print second_count
    print SUPPOSED_SECOND_COUNT

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and SHOT == False and shot_count > 0 and YOU_DEAD == False:
                duck_bullet = Duck_bullet()
                SHOT = True
                shot_count += -1
                duck_bullet.rect.x = daffy.rect.x + 20
                duck_bullet.rect.y = daffy.rect.y
                all_sprites_list.add(duck_bullet)
                duck_bullet_list.add(duck_bullet)
                duck_quack.play()
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                #if daffy.x_speed != -8:
                daffy.x_speed += -8
            if event.key == pygame.K_RIGHT:
                #daffy.x_speed != 8:
                daffy.x_speed += 8
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                #if daffy.x_speed == -8:
                daffy.x_speed += 8
            if event.key == pygame.K_RIGHT:
                #daffy.x_speed == 8:
                daffy.x_speed += -8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                SHOT = False

    daffy.rect.x += daffy.x_speed
    daffy.rect.y += daffy.y_speed

    #make sure duck stays on screen
    if daffy.rect.x < -5:
        daffy.rect.x = -5
    if daffy.rect.x > 940:
        daffy.rect.x = 940
    if daffy.rect.y != 550:
        daffy.rect.y = 550


    #spawn enemies
    if second_count == SUPPOSED_SECOND_COUNT and len(enemy_actual_list) > 0:
        ENEMY_SHOOT1 = True
        SUPPOSED_SECOND_COUNT += 1


    if second_count == SUPPOSED_ENEMY_COUNT and number_of_enemies < 31:
        ENEMY_SPAWN = True
        SUPPOSED_ENEMY_COUNT += 2

    if ENEMY_SHOOT1 == True:
        for z in range(0, (number_of_enemies - int(round(.30*number_of_enemies, 0)))):
            z += 1
            basic_enemy_bullet = Basic_enemy_bullet()

            listLength = len(enemy_actual_list)
            current_shooter = enemy_actual_list[random.randint(0, listLength-1)]

            basic_enemy_bullet.rect.x = current_shooter.rect.x
            basic_enemy_bullet.rect.y = current_shooter.rect.y

            all_sprites_list.add(basic_enemy_bullet)
            enemy_bullet_list.add(basic_enemy_bullet)
        ENEMY_SHOOT1 = False


    if ENEMY_SPAWN == True:
        for x in range(6):
            x += 1

            number_of_enemies += 1

            #add them to list, not group
            enemies_list_for_random()

        ENEMY_SPAWN = False





    #Enemy shooting (at duck)


    minute_count = 37-second_count


    all_sprites_list.update()

    #duck bullets
    for bullet in duck_bullet_list:
        enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
        bullets_hit_list = pygame.sprite.spritecollide(bullet, enemy_bullet_list, True)

        if bullet.rect.y < -10:
            duck_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

        for enemy in enemy_hit_list:
            duck_bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            hit_count += 1
            number_of_enemies += -1
            hit_sound.play()
            print(hit_count)

    #enemy bullets

    for basic_enemy_bullet in enemy_bullet_list:
        duck_hit_list = pygame.sprite.spritecollide(basic_enemy_bullet, duck_character_list, True)

        if basic_enemy_bullet.rect.y > 600:
            enemy_bullet_list.remove(basic_enemy_bullet)
            all_sprites_list.remove(basic_enemy_bullet)

        for daffy in duck_hit_list:
            hit_sound.play()
            YOU_DEAD = True
            all_sprites_list.remove(daffy)


    print daffy.x_speed

    # --- Drawing cod   e should go here
    screen.fill(WHITE)

    all_sprites_list.draw(screen)

    if second_count > second_count_limit:
        shot_count += 3
        second_count_limit += 1

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font2 = pygame.font.SysFont('Calibri', 40, True, False)
    shot_count_text = font.render("Shot count: " + str(shot_count),True,BLACK)
    hit_count_text = font.render("Hit count: " + str(hit_count),True,BLACK)
    second_count_text = font2.render(str(round((second_count_with_decimals),1)),True,BLACK)
    zero_text = font2.render("0",True, BLACK)
    screen.blit(shot_count_text, [830,5])
    screen.blit(hit_count_text, [20, 5])
    screen.blit(second_count_text, [475,5])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


