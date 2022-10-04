from pico2d import *
import game_framework

import main_menu_state as startState

if __name__ == '__main__':
    open_canvas(480, 272)
    game_framework.run(startState)
    close_canvas()
