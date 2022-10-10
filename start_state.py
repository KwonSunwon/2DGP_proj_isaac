from pico2d import *
import game_framework

import main_state


name = "StartState"

def enter():
    global menu
    menu = load_image('./resources/ui/title_menu.png')


def exit():
    global menu
    del (menu)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            game_framework.change_state(main_state)


def update():
    pass


def draw():
    clear_canvas()
    menu.clip_composite_draw(0, 272, 480, 272, 0, '', 720, 408, 1440, 816)
    menu.clip_composite_draw(0, 0, 160, 144, 0, '', 690, 300, 480, 432)
    menu.clip_composite_draw(0, 160, 480, 100, 0, '', 720, 630, 1440, 333)
    update_canvas()
