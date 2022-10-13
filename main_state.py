from pico2d import *
import game_framework
import game_world

from ui import UI
from character import Character


name = "MainState"
ui = None
character = None

def enter():
    global ui, character
    ui = UI()
    character = Character()
    

def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    pass


def update():
    ui.update()


def draw():
    clear_canvas()
    ui.draw()
    character.draw()
    update_canvas()
    
    
def test_self():
    import sys
    pico2d.open_canvas(1440, 816)
    game_framework.run(sys.modules[__name__])
    pico2d.close_canvas()
    

if __name__ == '__main__':
    test_self()