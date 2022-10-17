from dino_runner.utils.constants import MUSICAL_NOTE, SHIELD_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Shield(PowerUp):
    def __init__(self):
        self.image = MUSICAL_NOTE
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type) 