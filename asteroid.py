import pygame
from circleshape import CircleShape
from constants import * 
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            first_vel = self.velocity.rotate(new_angle) * 1.2
            second_vel = self.velocity.rotate(-new_angle) * 1.2
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            child_1 = Asteroid(self.position.x, self.position.y, new_rad)
            child_2 = Asteroid(self.position.x, self.position.y, new_rad)

            child_1.velocity = first_vel
            child_2.velocity = second_vel
