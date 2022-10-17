import random

from dino_runner.utils.constants import BUTTERFLY
from dino_runner.components.obstacles.obstacle import Obstacle

HEIGHT = [250, 200, 330]

class Bird(Obstacle):
    def __init__(self):
        super().__init__(BUTTERFLY, 0)
        self.rect.y = HEIGHT[random.randint(0,2)]
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 4], self.rect)
        self.step_index += 1

        if self.step_index >= 32:
            self.step_index = 0