import pygame
import random
from circleshape import CircleShape

from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw (self, screen_obj):
        pygame.draw.circle(screen_obj, "white", self.position, self.radius, 2) 

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            offset = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(offset)
            velocity2 = self.velocity.rotate(-offset)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = velocity1 * 1.2
            asteroid2.velocity = velocity2 * 1.2