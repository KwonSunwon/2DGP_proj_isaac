from cmath import pi
from pico2d import *
import game_world

from define import *

import player
import room_type
import static
import enemy

width = 1440
height = 864


OPEN, CLOSE, LOCK = 1, 2, 3

NORTH, SOUTH, EAST, WEST = range(4)

class Room:
    background_image = None
    
    def __init__(self):
        if Room.background_image == None:
            Room.background_image = load_image('resources/BG/basement_bg.png')
        self.grid = [[None] * 15 for i in range(9)]
        self.door_state = [None, None, None, None]
        self.objects = []
        self.enemy = []
        
    
    def add_event(self, event):
        pass
    
    def update(self):
        pass
    
    def set_room(self, room_type):
        for y in range(9):
            for x in range(15):
                # self.grid[y][x] = room_type[y][x]
                # print(room_type[y][x])
                if room_type[y][x] == WALL:
                    self.objects.append(static.Wall(x, y))
                elif room_type[y][x] == DOOR_NORMAL:
                    self.objects.append(static.Door(x, y, DOOR_NORMAL))
                elif room_type[y][x] == DOOR_TREASURE:
                    self.objects.append(static.Door(x, y, DOOR_TREASURE))
                elif room_type[y][x] == DOOR_BOSS:
                    self.objects.append(static.Door(x, y, DOOR_BOSS))
                elif room_type[y][x] == DOOR_TRAP:
                    self.objects.append(static.Door(x, y, DOOR_TRAP))
                elif room_type[y][x] == ROCK:
                    self.objects.append(static.Rock(x, y, ROCK))
                elif room_type[y][x] == JAR:
                    self.objects.append(static.Rock(x, y, JAR))
                elif room_type[y][x] == SPIKE:
                    self.objects.append(static.Spike(x, y))
                elif room_type[y][x] == POOP:
                    self.objects.append(static.Poop(x, y))
                elif room_type[y][x] == FLY:
                    self.enemy.append(enemy.Fly(x, y))
                    
                
        game_world.add_objects(self.objects, 1)
        game_world.add_objects(self.enemy, 3)

            
    def draw_grid(self):
        self.background_image.draw(width / 2, height / 2, width, height)
    
    def draw(self):
        self.draw_grid();
        
    def handle_event(self, event):
        pass
    


class Stage:
    
    def __init__(self):
        self.stage = [[None] * 10 for i in range(10)]
        self.playerPos = [4, 4]
    
    def add_event(self, event):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        self.stage[self.playerPos[0]][self.playerPos[1]].draw()
        
    def handle_event(self, event):
        pass
    
    def set_stage(self):
        self.stage[4][4] = Room()
        self.stage[4][4].set_room(room_type.type_02)
        

    def get_state(self):
        return self.get_stage()

    def get_stage(self):
        return self.stage
    
    def get_room_objects(self):
        return self.stage[self.playerPos[0]][self.playerPos[1]].objects
