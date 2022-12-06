from pico2d import *
import game_framework
import game_world

import main_state

import server

name = 'ClearState'

def enter():
    # print('enter game over state')
    
    if server.clear_ui == None:
        server.clear_ui = load_image('./resources/ui/clear.png')
    if server.clear_font == None:
        server.clear_font = load_font('./resources/DungGeunMo.ttf', 180)

def exit():
    server.player.state_clear()
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
        
    server.clear_ui.clip_draw(0, 0, 384, 256, 720, 432, 1152, 768)
    server.clear_font.draw(400, 680, 'CLEAR!', (55, 43, 45))
    server.clear_font.draw(400, 500, 'Restart?', (55, 43, 45))
    server.ui.font.draw(450 + 500, 380, '( Esc )', (55, 43, 45))
    server.ui.font.draw(450 - 100, 380, '( R )', (55, 43, 45))

    
    update_canvas()
