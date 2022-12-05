from pico2d import *
import game_framework

import start_state as startState
# import stage_change_state as startState

if __name__ == '__main__':
    open_canvas(1440, 864)
    game_framework.run(startState)
    close_canvas()