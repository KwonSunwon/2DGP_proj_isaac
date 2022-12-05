from pico2d import *
import game_framework
import game_world

import main_state

import server

name = "GameOverState"

def enter():
    print('enter game over state')
    
    if server.death_ui['portraits'] == None:
        server.death_ui['portraits'] = load_image('./resources/ui/death_portraits.png')
    if server.death_ui['select'] == None:
        server.death_ui['select'] = load_image('./resources/ui/death_select.png')
    

def exit():
    game_world.clear()
    pass

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.change_state(main_state)
            


def update():
    pass


def draw():
    clear_canvas()
    for game_objects in game_world.all_objects():
        game_objects.draw()
        
    server.death_ui['portraits'].clip_draw(208, 0, 208, 256, 720, 432, 624, 768)
    server.death_ui['portraits'].clip_draw(0, 112, 64, 16, 790, 145, 180, 48)
    server.death_ui['portraits'].clip_draw(128, 192, 48, 32, 610, 460, 144, 96)
    server.death_ui['portraits'].clip_draw(0, 128, 32, 32, 810, 460, 96, 96)

    server.death_ui['select'].clip_draw(0, 0, 96, 128, 96, 0, 288, 384)
    server.ui.font.draw(40, 50, 'Esc', (55, 43, 45))
    server.death_ui['select'].clip_draw(96, 0, 128, 128, 1440 - 96, 30, 384, 384)
    server.ui.font.draw(1440 - 50 - 64, 50, 'R', (55, 43, 45))
    
    update_canvas()
