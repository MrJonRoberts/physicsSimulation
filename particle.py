import pygame
import math
# our main particle class
class Particle:

    def __init__(self, x, y, size, screen):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 0, 255)
        self.thickness = 2
        self.screen = screen
        self.speed = 0.01
        self.angle = 0

    def display(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, self.thickness)


    def move(self):


        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.x = int(self.x)
        self.y = int(self.y)