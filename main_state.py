from pico2d import *
import game_framework
import game_world

from ui import UI


name = "MainState"
ui = None


def enter():
    global ui
    ui = UI()
    

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
    update_canvas()
    