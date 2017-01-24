import pygame
import random

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
    """
    Ellipse Constructor. Pass in the color of the ellipse,
    and its size
    """
    # Call the parent class (Sprite) constructor
    super().__init__()

    # Set the background color and set it to be transparent
    self.image = pygame.Surface([width, height])
    self.image.fill(WHITE)
    self.image.set_colorkey(WHITE)

    # Draw the ellipse
    pygame.draw.ellipse(self.image, color, [0, 0, width, height])
