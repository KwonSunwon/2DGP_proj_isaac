from pico2d import *
import game_framework

name = "MainMenuState"


def enter():
    global menu
    menu = load_image('./resources/title_menu.png')


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
        # elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
        #     game_framework.change_state('GameState')


def update():
    pass


def draw():
    clear_canvas()
    menu.clip_composite_draw(0, 272, 480, 272, 0, '', 240, 136, 480, 272)
    menu.clip_composite_draw(0, 0, 160, 144, 0, '', 0, 0, 160, 144)
    update_canvas()
