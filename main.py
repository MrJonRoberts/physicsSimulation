import pygame
# based on http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/
from particle import *


# set up some vars to use
screenSize = (width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))

# some colours
red = (255, 0, 0)
black = (0, 0, 0)
white = (255,255,255)
grey = (122, 122, 122)
background_colour = grey

screen.fill(background_colour)

# set the name and display
pygame.display.set_caption('Physics Simulation')

my_first_particle = Particle(150, 50, 50, screen)
my_first_particle.display()

pygame.display.flip()

running = True
# main event loop
while running:
    # detect quit and leave main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

