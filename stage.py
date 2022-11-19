from cmath import pi
from pico2d import *
import game_world

from define import *

import player
import room_type
import static
import enemy

import server

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
        
        self.clear = False        
    
    def add_event(self, event):
        pass
    
    def update(self):
        if game_world.objects[3] == []:
            # print('room update')
            for o in self.objects:
                if o.type == 'door' or o.type == 'trapdoor':
                    o.isOpen = True
            self.clear = True
            
        pass
    
    def set_room(self, room_type):
        
        # print(self.clear)
        self.enemy = []
        self.objects = []
        
        # print(room_type)
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
                    self.objects.append(static.TrapDoor(x, y))
                elif room_type[y][x] == ROCK:
                    self.objects.append(static.Rock(x, y, ROCK))
                elif room_type[y][x] == JAR:
                    self.objects.append(static.Rock(x, y, JAR))
                elif room_type[y][x] == SPIKE:
                    self.objects.append(static.Spike(x, y))
                elif room_type[y][x] == POOP:
                    self.objects.append(static.Poop(x, y))
                
                if self.clear == False:
                    if room_type[y][x] == FLY:
                        self.enemy.append(enemy.Fly(x, y))
                    elif room_type[y][x] == CHARGER:
                        self.enemy.append(enemy.Charger(x, y))
                    elif room_type[y][x] == MEAT:
                        self.enemy.append(enemy.Meat(x, y))
                    
        server.objects = self.objects
        server.enemy = self.enemy
        
        game_world.add_objects(self.objects, 1)
        game_world.add_objects(self.enemy, 3)
        
        # print(server.enemy)
        # print(self.enemy)
        
        game_world.add_collision_group(None, self.objects, 'player:room')
        game_world.add_collision_group(None, self.enemy, 'player:enemy')
        game_world.add_collision_group(self.objects, None, 'room:tears')
        game_world.add_collision_group(self.objects, self.enemy, 'room:enemy')
        game_world.add_collision_group(self.enemy, None, 'enemy:tears')
        
        # print(server.objects)
    
            
    def draw_grid(self):
        self.background_image.draw(width / 2, height / 2, width, height)
    
    def draw(self):
        self.draw_grid();
        
    def handle_event(self, event):
        pass
    


class Stage:
    
    def __init__(self):
        self.stage = [[None] * 5 for i in range(5)]
        self.playerPos = [4, 2]
    
    def add_event(self, event):
        pass
    
    def update(self):
        self.stage[self.playerPos[0]][self.playerPos[1]].update()
        pass
    
    def draw(self):
        self.stage[self.playerPos[0]][self.playerPos[1]].draw()
        
    def handle_event(self, event):
        pass
    
    def set_stage(self):
        self.playerPos = [4, 2]
        for y in range(5):
            for x in range(5):
                if room_type.stage_01[y][x] != None:
                    self.stage[y][x] = Room()
        # print(self.stage)
        self.stage[4][2].set_room(room_type.stage_01[4][2])
        
        # print(self.stage[self.playerPos[0]][self.playerPos[1]])
        # self.stage[self.playerPos[0]][self.playerPos[1]].set_room(self.stage[self.playerPos[0]][self.playerPos[1]])
        # self.stage[2][4] = Room()
        # self.stage[2][4].set_room(room_type.type_04)
        
    def enter_room(self, direction):
        for e in self.stage[self.playerPos[0]][self.playerPos[1]].enemy:
            game_world.remove_object(e)
        for o in self.stage[self.playerPos[0]][self.playerPos[1]].objects:
            game_world.remove_object(o)
        
        # Clear effects
        game_world.objects[4] = []
        
        server.objects = []
        server.enemy = []
            
        if direction == 0: # North
            self.playerPos[0] -= 1
        elif direction == 1: # West
            self.playerPos[1] -= 1
        elif direction == 2: # East
            self.playerPos[1] += 1
        elif direction == 3: # South
            self.playerPos[0] += 1
        
        # print(self.playerPos)
        self.stage[self.playerPos[0]][self.playerPos[1]].set_room(room_type.stage_01[self.playerPos[0]][self.playerPos[1]])
        # print(self.stage[self.playerPos[0]][self.playerPos[1]].clear)
        
    def get_state(self):
        return self.get_stage()

    def get_stage(self):
        return self.stage
    
    def get_room_objects(self):
        return self.stage[self.playerPos[0]][self.playerPos[1]].objects
