from pico2d import *
import game_framework
import game_world

from ui import UI
from player import Player
from stage import Stage

import server

name = "MainState"

def enter():
    server.player = Player()
    server.stage = Stage()
    server.ui = UI()
    
    server.stage.set_stage()
    
    game_world.add_object(server.stage, 0)
    game_world.add_object(server.player, 2)
    game_world.add_object(server.ui, 5)

    game_world.add_collision_group(server.player, server.objects, 'player:room')
    game_world.add_collision_group(server.player, server.enemy, 'player:enemy')
    game_world.add_collision_group(server.objects, None, 'room:tears')
    game_world.add_collision_group(server.objects, server.enemy, 'room:enemy')
    game_world.add_collision_group(server.enemy, None, 'enemy:tears')
    

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
            server.player.handle_event(event)
    pass


def update():
    for game_objects in game_world.all_objects():
        game_objects.update()
    
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            # print('collide')
            a.handle_collision(b, group)
            b.handle_collision(a, group)


def draw():
    clear_canvas()
    # stage.draw()
    # ui.draw()
    # player.draw()
    for game_objects in game_world.all_objects():
        game_objects.draw()
    update_canvas()
    
    
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True
    
    
def test_self():
    import sys
    pico2d.open_canvas(1440, 864)
    game_framework.run(sys.modules[__name__])
    pico2d.close_canvas()
    

if __name__ == '__main__':
    test_self()