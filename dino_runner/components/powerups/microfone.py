from dino_runner.utils.constants import MICROFONE, MICROFONE_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Microfone(PowerUp):
    def __init__(self):
        self.image = MICROFONE
        self.type = MICROFONE_TYPE
        super().__init__(self.image, self.type) 