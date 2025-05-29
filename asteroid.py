import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"green",self.position,self.radius,width=2)
    
    def update(self, dt):
        self.position += (self.velocity *dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_angle_1 = self.velocity.rotate(random_angle)
        new_angle_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast = Asteroid(self.position.x, self.position.y, new_radius)
        ast.velocity = new_angle_1 * 1.2
        ast = Asteroid(self.position.x, self.position.y, new_radius)
        ast.velocity = new_angle_2 * 1.2