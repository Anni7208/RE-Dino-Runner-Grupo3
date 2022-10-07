from dino_runner.components.obstacles.obstacles  import Obstacle
import random

class Cactus():
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(self, image, self.type) 
        self.rect.y = 325
