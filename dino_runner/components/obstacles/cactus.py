import random

from dino_runner.utils.constants import MOBS, MUSHROOM #MUSHROOM adicionado 
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):

    CACTUS = [
        (MOBS, 300),
        (MUSHROOM, 325),
    ]

    def __init__(self):
        image, cactus_pos = self.CACTUS[random.randint(0, 1)]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = cactus_pos