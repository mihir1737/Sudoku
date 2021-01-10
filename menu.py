import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((540, 590))


class StartMenu:
    def __init__(self):
        self.level = 1
        self.name = None
        self.game_running = False
        self.menu = pygame_menu.Menu(
            590, 540, "Welcome to the Sudoku Game.", theme=pygame_menu.themes.THEME_BLUE
        )
        self.nameinput = self.menu.add_text_input("Name :")
        self.menu.add_selector(
            "Difficulty :",
            [("Easy", 1), ("Medium", 2), ("Hard", 3)],
            onchange=self.__set_difficulty,
        )
        self.menu.add_button("Play", self.start_the_game)
        self.menu.add_button("Quit", pygame_menu.events.EXIT)

    def __set_difficulty(self, value, difficulty):
        # Do the job here !
        self.level = difficulty

    def start_the_game(self):
        # Do the job here !
        print("Start")
        self.game_running = True
        self.menu.disable()
        self.menu.reset(1)

    def run_menu(self):
        self.menu.mainloop(surface, disable_loop=False)
