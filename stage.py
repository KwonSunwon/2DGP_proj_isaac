from cmath import pi
from logging import root
from pico2d import *

import Player

width = 1440
height = 864

OPEN, CLOSE, LOCK = 1, 2, 3
NORTH, SOUTH, EAST, WEST = range(4)

BASEMENT, CAVES = 0, 1
WALL = 20
DOOR_NORMAL = 21
DOOR_TREASURE = 22
DOOR_BOSS = 23

DOOR_TRAP = 24

# start room
room_type_01 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [DOOR_NORMAL, None, None, None, None, None, None, None, None, None,None, None, None, WALL, DOOR_BOSS],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_TREASURE, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

class Room:
    room_background_image = [None, None]
    door_normal = None
    door_treasure = None
    door_boss = None
    door_trap = None
    
    def __init__(self):
        if Room.room_background_image[BASEMENT] == None:
            Room.room_background_image[BASEMENT] = load_image('./resources/BG/basement_bg.png')
        if Room.room_background_image[CAVES] == None:
            Room.room_background_image[CAVES] = load_image('./resources/BG/02_caves.png')
        if Room.door_normal == None:
            Room.door_normal = load_image('./resources/grid/door_01_normaldoor.png')
        if Room.door_treasure == None:
            Room.door_treasure = load_image('./resources/grid/door_02_treasureroomdoor.png')
        if Room.door_boss == None:
            Room.door_boss = load_image('./resources/grid/door_03_bossroomdoor.png')
        if Room.door_trap == None:
            Room.door_trap = load_image('./resources/grid/door_04_trapdoor.png')
            
        self.background = None
        self.grid = [[None] * 15 for i in range(9)]
        self.door_state = [None, None, None, None]
        
    
    def add_event(self, event):
        pass
    
    def update(self):
        pass
    
    def set_room(self, room_type):
        self.background = BASEMENT
        for y in range(9):
            for x in range(15):
                self.grid[y][x] = room_type[y][x]
            
    def draw_door(self, door, x, y, direction):
        if direction == NORTH:
            door.clip_composite_draw(0, 144, 64, 48, 0, '', 7 * 96 + 48, 8 * 96, 192, 128)
            door.clip_composite_draw(64, 144, 64, 48, 0, '', 7 * 96 + 48, 8 * 96, 192, 128)
            door.clip_composite_draw(0, 192, 64, 48, 0, '', 7 * 96 + 48, 8 * 96, 192, 128)
        elif direction == WEST:
            door.clip_composite_draw(0, 144, 64, 48, pi / 2, 'w', 96 + 16, 4 * 96 + 48, 192, 144)
            door.clip_composite_draw(64, 144, 64, 48, pi / 2, 'w', 96 + 16, 4 * 96 + 48, 192, 144)
            door.clip_composite_draw(0, 192, 64, 48, pi / 2, 'w', 96 + 16, 4 * 96 + 48, 192, 144)
        elif direction == SOUTH:
            door.clip_composite_draw(0, 144, 64, 48, -pi / 2, 'h', 14 * 96 - 16, 4 * 96 + 48, 192, 144)
            door.clip_composite_draw(64, 144, 64, 48, -pi / 2, 'h', 14 * 96 - 16, 4 * 96 + 48, 192, 144)
            door.clip_composite_draw(0, 192, 64, 48, -pi / 2, 'h', 14 * 96 - 16, 4 * 96 + 48, 192, 144)
        elif direction == EAST:
            door.clip_composite_draw(0, 144, 64, 48, pi, 'h', 7 * 96 + 48, 96, 192, 128)
            door.clip_composite_draw(64, 144, 64, 48, pi, 'h', 7 * 96 + 48, 96, 192, 128)
            door.clip_composite_draw(0, 192, 64, 48, pi, 'h', 7 * 96 + 48, 96, 192, 128)
            
    def draw_grid(self):
        self.room_background_image[self.background].draw(width / 2, height / 2, 1440, 864)
        for y in range(9):
            for x in range(15):
                if self.grid[y][x] == DOOR_NORMAL:
                    door = Room.door_normal
                elif self.grid[y][x] == DOOR_TREASURE:
                    door = Room.door_treasure
                elif self.grid[y][x] == DOOR_BOSS:
                    door = Room.door_boss
                    
                if self.grid[y][x] == DOOR_NORMAL or self.grid[y][x] == DOOR_TREASURE or self.grid[y][x] == DOOR_BOSS:
                    if y == 0 and x == 7: # north
                        self.draw_door(door, x, y, NORTH)
                    elif y == 4 and x == 0: # west
                        self.draw_door(door, x, y, WEST)
                    elif y == 4 and x == 14: # east
                        self.draw_door(door, x, y, EAST)
                    elif y == 8 and x == 7: # south
                        self.draw_door(door, x, y, SOUTH)
    
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
        self.stage[4][4].set_room(room_type_01)
        
    def get_stage(self):
        return self.stage