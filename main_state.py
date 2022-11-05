from pico2d import *
import game_framework
import game_world

from ui import UI
from Player import Player
from stage import Stage


name = "MainState"
ui = None
player = None
stage = None

def enter():
    global ui, player, stage
    player = Player()
    stage = Stage()
    stage.set_stage()
    ui = UI()
    
    game_world.add_object(stage, 0)
    game_world.add_object(player, 2)
    game_world.add_object(ui, 5)
    

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
        else:
            player.handle_event(event)
    pass


def update():
    global ui
    # UI로 상태 전달
    ui.set_state(player, stage)
    
    for game_objects in game_world.all_objects():
        game_objects.update()


def draw():
    clear_canvas()
    # stage.draw()
    # ui.draw()
    # player.draw()
    for game_objects in game_world.all_objects():
        game_objects.draw()
    update_canvas()
    
    
def test_self():
    import sys
    pico2d.open_canvas(1440, 864)
    game_framework.run(sys.modules[__name__])
    pico2d.close_canvas()
    

if __name__ == '__main__':
    test_self()