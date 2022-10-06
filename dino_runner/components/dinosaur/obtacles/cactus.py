import pygame
from dino_runner.components.obtacles.obstable  import Obstacle
import random

class Cactus():
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type) 
        self.rect.y = 350
