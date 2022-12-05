from pico2d import *
import game_framework
import game_world

import server

import main_state

name = "StageChangeState"

player_stage_position = None

player_draw_position = -10
player_icon_draw_position = -48

def enter():
    if server.change_ui['bg'] == None:
        server.change_ui['bg'] = load_image('./resources/ui/change_ui_bg.png')
    if server.change_ui['player'] == None:
        server.change_ui['player'] = load_image('./resources/ui/change_ui_player.png')
    if server.change_ui['progress'] == None:
        server.change_ui['progress'] = load_image('./resources/ui/change_ui_progress.png')
    if server.change_ui['spotlight'] == None:
        server.change_ui['spotlight'] = load_image('./resources/ui/change_ui_spotlight.png')
    if server.bg_black == None:
        server.bg_black = load_image('./resources/ui/bg_black.png')
    if server.bg_caves == None:
        server.bg_caves = load_image('./resources/ui/bg_caves.png')
    
    global player_stage_position
    player_stage_position = server.stage.level
    

def exit():
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
    pass


def update():
    global player_draw_position, player_icon_draw_position
    player_draw_position += 0.1
    if player_draw_position > 2:
        player_draw_position = -2
    
    player_icon_draw_position += 0.1
    
    if player_icon_draw_position > 48:
        server.player.state_clear()
        
        game_framework.pop_state()
    


def draw():
    clear_canvas()
    server.bg_caves.clip_draw(50, 50, 300, 100, 720, 200, 1440, 864)
    server.change_ui['bg'].clip_draw(0, 0, 480, 270, 720, 432, 1440, 864)
    server.change_ui['spotlight'].clip_draw(0, 0, 256, 480, 720, 432, 1440, 864)
    server.change_ui['player'].clip_draw(0, 0, 144, 144, 720 + player_draw_position, 232, 432, 432)
    server.change_ui['progress'].clip_draw(0, 192, 32, 32, 720, 670, 96, 96)
    server.change_ui['progress'].clip_draw(0, 160, 32, 32, 720 - 48, 670, 96, 96)
    server.change_ui['progress'].clip_draw(32, 160, 32, 32, 720 + 48, 670, 96, 96)
    
    server.change_ui['progress'].clip_draw(32, 192, 32, 32, 720 + player_icon_draw_position, 670, 96, 96)
    update_canvas()

def test_self():
    import sys
    pico2d.open_canvas(1440, 864)
    game_framework.run(sys.modules[__name__])
    pico2d.close_canvas()
    

if __name__ == '__main__':
    test_self()