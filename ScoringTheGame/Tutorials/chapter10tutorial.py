
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

# Speed in pixels per frame
x_speed = 0
y_speed = 0


# Current position
x_coord = 10
y_coord = 10

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
                x_speed += -3
            if event.key == pygame.K_RIGHT and x_coord <= 990:
                x_speed += 3
            if event.key == pygame.K_UP and y_coord >= 0:
                y_speed += -3
            if event.key == pygame.K_DOWN and y_coord <= 640:
                y_speed += 3

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
    if x_coord > 980:
        x_coord =980
    if y_coord < 0:
        y_coord = 0
    if y_coord > 620:
        y_coord = 620

    print x_coord,y_coord

    # --- Game logic should go here
    """
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    """

    # --- Drawing code should go here
    screen.fill(WHITE)
    """
    def draw_snowman(screen, x, y):
        # Draw a circle for the head
        pygame.draw.ellipse(screen, WHITE, [35 + x, y, 25, 25])
        # Draw the middle snowman circle
        pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
        # Draw the bottom snowman circle
        pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])

    # Snowman in upper left
    draw_snowman(screen, 10, 10)

    # Snowman in upper right
    draw_snowman(screen, 300, 10)

    # Snowman in lower left
    draw_snowman(screen, 10, 300)
    """

    def draw_stick_figure(screen, x, y):
        # Head
        pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)

        # Legs
        pygame.draw.line(screen, BLACK ,[5+x,17+y], [10+x,27+y], 2)
        pygame.draw.line(screen, BLACK, [5+x,17+y], [x,27+y], 2)

        # Body
        pygame.draw.line(screen, RED, [5+x,17+y], [5+x,7+y], 2)

        # Arms
        pygame.draw.line(screen, RED, [5+x,7+y], [9+x,17+y], 2)
        pygame.draw.line(screen, RED, [5+x,7+y], [1+x,17+y], 2)

    draw_stick_figure(screen, x_coord, y_coord)


    """
    draw_stick_figure(screen, x, y)
    """

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


