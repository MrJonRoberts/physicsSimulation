import pygame
# based on http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/
from particle import *
import random as r

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

# particles
numParticles = 10
pList = []
for p in range(numParticles):
    size = r.randint(10,20)
    x = r.randint(size, width - size)
    y = r.randint(size, height - size)
    pList.append(Particle(x,y,size,screen))

for particle in pList:
    particle.display()


pygame.display.flip()

running = True
# main event loop
while running:
    # detect quit and leave main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

