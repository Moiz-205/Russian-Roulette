from interface.window import init_window, main_menu
from core.game import game_loop

if __name__ == "__main__":
    screen = init_window()
    if main_menu(screen) == 'start':
        game_loop(screen)
