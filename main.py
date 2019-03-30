import pygame
# based on http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/
from particle import *
import random as r

# set up some vars to use
screenSize = (width, height) = (600, 400)
screen = pygame.display.set_mode((width, height))

# some colours
red = (255, 0, 0)
black = (0, 0, 0)
white = (255,255,255)
grey = (122, 122, 122)
background_colour = grey



# set the name and display
pygame.display.set_caption('Physics Simulation')

# particles
numParticles = 4
pList = []
for p in range(numParticles):
    size = r.randint(10,20)
    x = r.randint(size, width - size)
    y = r.randint(size, height - size)
    particle = Particle(x,y,size,screen)
    particle.speed = r.random()
    particle.angle = r.uniform(0, math.pi * 2)
    pList.append(particle)






running = True
# main event loop
while running:
    # detect quit and leave main loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_colour)
    for particle in pList:
        particle.move()
        particle.display()

    pygame.display.flip()

