from logging import root
from pico2d import *

import Player

width = 1440
height = 816

WALL = 0b00000001
DOOR_NORMAL = 0b00000010

room_type_01 = [[WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [DOOR_NORMAL, None, None, None, None, None, None, None, None, None,None, None, None, WALL, DOOR_NORMAL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, None, None, None, None, None, None, None, None, None,None, None, None, None, WALL],
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, DOOR_NORMAL, WALL, WALL,WALL, WALL, WALL, WALL, WALL]]

class Room:
    room_background_image01 = None
    room_background_image02 = None
    door_normal = None
    door_treasure = None
    door_boss = None
    door_trap = None
    
    def __init__(self):
        if Room.room_background_image01 == None:
            Room.room_background_image01 = load_image('./resources/BG/01_basement.png')
        if Room.room_background_image02 == None:
            Room.room_background_image02 = load_image('./resources/BG/02.caves.png')
        if Room.door_normal == None:
            Room.door_normal = load_image('./resources/grid/door_01_normaldoor.png')
        if Room.door_treasure == None:
            Room.door_treasure = load_image('./resources/grid/door_02_treasureroomdoor.png')
        if Room.door_boss == None:
            Room.door_boss = load_image('./resources/grid/door_03_bossroomdoor.png')
        if Room.door_trap == None:
            Room.door_trap = load_image('./resources/grid/door_04_trapdoor.png')
            
        self.room = [[None] * 15 for i in range(9)]
    
    def add_event(self, event):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
        
    def handle_event(self, event):
        pass
    


class Stage:
    
    def __init__(self):
        self.stage = [[Room()] * 10 for i in range(10)]
    
    def add_event(self, event):
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
        
    def handle_event(self, event):
        pass
    