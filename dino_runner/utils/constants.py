import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

ICON_MIKU = pygame.image.load(os.path.join(IMG_DIR, "Other/miku_icon.png"))
ICON_MIKU_OPEN = pygame.image.load(os.path.join(IMG_DIR, "Other/miku_open.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_MIKU = [
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_6.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD_MIKU = [
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_shield_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_shield_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_shield_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_6.png")),
]

RUNNING_LEEK_MIKU = [
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_leek_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_leek_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_leek_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_leek_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_leek_5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_leek_6.png")),
]

RUNNING_MICROFONE_MIKU = [
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_microfone_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_microfone_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_microfone_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_microfone_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_microfone_5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_microfone_6.png")),
]

JUMPING_MICROFONE_MIKU = pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_microfone_2.png"))

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_SHIELD_MIKU = pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_jump_shield.png"))
JUMPING_LEEK_MIKU = pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_leek_jump.png"))

JUMPING_MIKU = pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_run_jump.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_MIKU = [
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_chibi_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_chibi_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_chibi_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_chibi_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_chibi_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_chibi_3.png")),
]


DUCKING_SHIELD_MIKU = [
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_duck_shield_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_chibi_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_duck_shield_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_duck_shield_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_chibi_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_duck_shield_2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

MOBS = [
    pygame.image.load(os.path.join(IMG_DIR, "Mobs/stone_eye.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mobs/toucan.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mobs/goat.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

MUSHROOM = [
    pygame.image.load(os.path.join(IMG_DIR, "Mushroom/mushroom_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mushroom/mushroom_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mushroom/mushroom_3.png")),
]

BUTTERFLY = [
    pygame.image.load(os.path.join(IMG_DIR, "Butterfly/butterfly_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Butterfly/butterfly_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Butterfly/butterfly_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Butterfly/butterfly_4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Butterfly/butterfly_5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Butterfly/butterfly_6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Butterfly/butterfly_7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Butterfly/butterfly_8.png")),
]

SMASH_LEEK_MIKU = [
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_smash_leek_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_smash_leek_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_smash_leek_3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_smash_leek_1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_smash_leek_2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Miku/miku_smash_leek_3.png"))
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

LEEK = pygame.image.load(os.path.join(IMG_DIR, 'Other/leek.png'))
MICROFONE = pygame.image.load(os.path.join(IMG_DIR, 'Other/microfone.png'))
MUSICAL_NOTE = pygame.image.load(os.path.join(IMG_DIR, 'Other/musical_note.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

FLOOR = pygame.image.load(os.path.join(IMG_DIR, 'Other/floor.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "leek"
MICROFONE_TYPE = "microfone"

# pygame.mixer.music.load("Miku/miku_song.wav")
# pygame.mixer.music.play(-1)

#adicionado as constants "miku's" e mushroom