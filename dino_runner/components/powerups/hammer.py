from dino_runner.utils.constants import LEEK, HAMMER_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Hammer(PowerUp):
    def __init__(self):
        self.image = LEEK
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type) 