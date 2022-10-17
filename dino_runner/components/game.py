import pygame

from dino_runner.utils.constants import BG, ICON_MIKU, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, ICON_MIKU_OPEN, MICROFONE_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager

GAME_SPEED = 20
MIKU_SONG = "dino_runner/assets/Miku/miku_song.wav"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON_MIKU)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.game_speed = GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
   
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = GAME_SPEED
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def song_miku(self):
        pygame.mixer.music.load(MIKU_SONG)
        pygame.mixer.music.set_volume == 20
        pygame.mixer.music.play(2)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2
    
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((173, 216, 230)) # "#FFFFFF"
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_score(self):
         draw_message_component(
            f"Score: {self.score}",
            self.screen,
            pos_x_center=1000,
            pos_y_center=50
        )   

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 40
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()
                self.song_miku()
    
    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        
        if self.death_count == 0:
           draw_message_component("-HI! Wellcome! I'm Miku and I'm so happy becase you here!", self.screen,(10,186,181), pos_y_center = half_screen_height - 80, pos_x_center = half_screen_width - 210)
           draw_message_component("Today i'm going for a walk around! Do you go with me?", self.screen,(10,186,181), pos_y_center = half_screen_height - 50, pos_x_center = half_screen_width - 210)
           draw_message_component("Press any key to start", self.screen, pos_y_center = half_screen_height + 100, pos_x_center = half_screen_width - 210)
           self.screen.blit(ICON_MIKU_OPEN, (half_screen_width + 50, half_screen_height - 200))
        else:
            draw_message_component("-Oh...You died... Miku is sorry for you, but... you can:", self.screen,(10,186,181), pos_y_center=half_screen_height + 140)
            draw_message_component("Press any key to restart", self.screen, pos_y_center=half_screen_height + 180)
            draw_message_component(
                f"Your Score: {self.score}",
                self.screen,
                pos_y_center=half_screen_height - 150
            )            
            draw_message_component(
                f"Death count: {self.death_count}",
                self.screen,(163,55,27),
                pos_y_center=half_screen_height - 100
            )
            self.screen.blit(ICON_MIKU, (half_screen_width - 40, half_screen_height - 30))

        pygame.display.flip()

        self.handle_events_on_menu()
