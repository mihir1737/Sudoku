from sudoku import Sudoku
from menu import StartMenu


def main():
    """Runs the main Sudoku GUI/Game"""
    menu = StartMenu()
    menu.run_menu()
    while not menu.game_running:
        """
        this is for cheking that user has started the game or not.
        """
        pass
    game = Sudoku(level=menu.level)
    while game.running:
        game.game_loop()


if __name__ == "__main__":
    main()
