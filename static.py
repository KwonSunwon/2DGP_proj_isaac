from pico2d import *
import game_framework
import game_world

import random

from cmath import pi

CLIP_SIZE = 32

class Static:
    x, y = 0, 0
    WIDTH, HEIGHT = 87, 85
    
    def __init__(self, x, y):
        self.x = x * self.WIDTH + 64
        self.y = (8 - y) * self.HEIGHT + 48
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        draw_rectangle(*self.get_bb())
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x, self.y, self.x + self.WIDTH, self.y + self.HEIGHT
    
    def handle_collision(self, other, group):
        pass
    

class Wall(Static):
    pass

class Rock(Static):
    image = None
    
    def __init__(self, x, y, type):
        if Rock.image == None:
            Rock.image = pico2d.load_image('resources/objects/rock.png')
        super().__init__(x, y)
        self.type = type
    
        self.rock_type = random.randint(0, 2)
        self.jar_type = random.randint(0, 2)
        
        # print(self.x, self.y)
        
    def draw(self):
        if self.type == 30:
            if self.rock_type == 0:
                self.image.clip_draw(0, 224, CLIP_SIZE, CLIP_SIZE, self.x + self.WIDTH//2, self.y + self.WIDTH//2, self.WIDTH + 4, self.HEIGHT + 4)
            elif self.rock_type == 1:
                self.image.clip_draw(32, 224, CLIP_SIZE, CLIP_SIZE, self.x + self.WIDTH//2, self.y + self.WIDTH//2, self.WIDTH + 4, self.HEIGHT + 4)
            elif self.rock_type == 2:
                self.image.clip_draw(64, 224, CLIP_SIZE, CLIP_SIZE, self.x + self.WIDTH//2, self.y + self.WIDTH//2, self.WIDTH + 4, self.HEIGHT + 4)
        elif self.type == 31:
            if self.rock_type == 0:
                self.image.clip_draw(64, 192, CLIP_SIZE, CLIP_SIZE, self.x + self.WIDTH//2, self.y + self.WIDTH//2, self.WIDTH + 4, self.HEIGHT + 4)
            elif self.rock_type == 1:
                self.image.clip_draw(64, 160, CLIP_SIZE, CLIP_SIZE, self.x + self.WIDTH//2, self.y + self.WIDTH//2, self.WIDTH + 4, self.HEIGHT + 4)
            elif self.rock_type == 2:
                self.image.clip_draw(64, 128, CLIP_SIZE, CLIP_SIZE, self.x + self.WIDTH//2, self.y + self.WIDTH//2, self.WIDTH + 4, self.HEIGHT + 4)
        
        draw_rectangle(*self.get_bb())
    pass


class Spike(Static):
    image = None
    
    def __init__(self, x, y):
        if Spike.image == None:
            Spike.image = pico2d.load_image('resources/objects/spike.png')
        super().__init__(x, y)
    pass


class Poop(Static):
    image = None
    
    def __init__(self, x, y):
        if Poop.image == None:
            Poop.image = pico2d.load_image('resources/objects/poop.png')
        super().__init__(x, y)
    pass

# Normal Door 21
# Treasure Door 22
# Boss Door 23

class Door(Static):
    normal_image = None
    treasure_image = None
    boss_image = None
    
    def __init__(self, x, y, type):
        if Door.normal_image == None:
            Door.normal_image = pico2d.load_image('resources/objects/normal_door.png')
        if Door.treasure_image == None:
            Door.treasure_image = pico2d.load_image('resources/objects/treasure_door.png')
        if Door.boss_image == None:
            Door.boss_image = pico2d.load_image('resources/objects/boss_door.png')
        self.x = x
        self.y = y
        
        if self.y == 0 and self.x == 7: # north
            self.direction = 0
        elif self.y == 4 and self.x == 0: # west
            self.direction = 1
        elif self.y == 4 and self.x == 14: # east
            self.direction = 2
        elif self.y == 8 and self.x == 7: # south
            self.direction = 3
        
        self.type = type
        
    def draw(self):
        if self.type == 21:
            door = Door.normal_image
        elif self.type == 22:
            door = Door.treasure_image
        elif self.type == 23:
            door = Door.boss_image
        
        if self.direction == 0:
            door.clip_composite_draw(0, 144, 64, 48, 0, '', 7 * 96 + 48, 8 * 96, 192, 128)
            door.clip_composite_draw(64, 144, 64, 48, 0, '', 7 * 96 + 48, 8 * 96, 192, 128)
            door.clip_composite_draw(0, 192, 64, 48, 0, '', 7 * 96 + 48, 8 * 96, 192, 128)
        elif self.direction == 1:
            door.clip_composite_draw(0, 144, 64, 48, pi / 2, 'w', 96 + 16, 4 * 96 + 48, 192, 144)
            door.clip_composite_draw(64, 144, 64, 48, pi / 2, 'w', 96 + 16, 4 * 96 + 48, 192, 144)
            door.clip_composite_draw(0, 192, 64, 48, pi / 2, 'w', 96 + 16, 4 * 96 + 48, 192, 144)
        elif self.direction == 2:
            door.clip_composite_draw(0, 144, 64, 48, -pi / 2, 'h', 14 * 96 - 16, 4 * 96 + 48, 192, 144)
            door.clip_composite_draw(64, 144, 64, 48, -pi / 2, 'h', 14 * 96 - 16, 4 * 96 + 48, 192, 144)
            door.clip_composite_draw(0, 192, 64, 48, -pi / 2, 'h', 14 * 96 - 16, 4 * 96 + 48, 192, 144)
        elif self.direction == 3:
            door.clip_composite_draw(0, 144, 64, 48, pi, 'h', 7 * 96 + 48, 96, 192, 128)
            door.clip_composite_draw(64, 144, 64, 48, pi, 'h', 7 * 96 + 48, 96, 192, 128)
            door.clip_composite_draw(0, 192, 64, 48, pi, 'h', 7 * 96 + 48, 96, 192, 128)
            
    def get_bb(self):
        if self.direction == 0:
            return 7 * 96 + 48, 8 * 96, 192, 128
        elif self.direction == 1:
            return 96 + 16, 4 * 96 + 48, 192, 144
        elif self.direction == 2:
            return 14 * 96 - 16, 4 * 96 + 48, 192, 144
        elif self.direction == 3:
            return 7 * 96 + 48, 96, 192, 128
    pass