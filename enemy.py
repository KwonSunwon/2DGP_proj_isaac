from pico2d import *
from creature import Creature

import game_framework
import game_world

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

class Enemy(Creature):
    def __init__(self, x, y):
        self.x = x * 87 + 64
        self.y = (8 - y) * 85 + 48
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass
    
    def handle_collision(self, other, group):
        if group == 'enemy:tears':
            if self.hp > 0 and other.hp > 0:
                self.hp -= 1
                if self.hp == 0:
                    self.frame = 0
        elif group == 'room:enemy' and self.type != 'fly':
            if other.type == 'wall' or other.type == 'rock':
                self.x, self.y = self.prevX, self.prevY


class Fly(Enemy):
    type = 'fly'
    image = None
    
    live_pos = ([0, 192], [32, 192], [64, 192], [96, 192])
    die_pos = ([0, 128], [64,128], [128, 128], [192, 128],
               [0, 64], [64, 64], [128, 64], [192, 64],
               [0, 0], [64, 0], [128, 0], [192, 0])
    FPA_live = 4
    FPA_die = 12
    TPA_live = 0.2
    TPA_die = 0.7
    
    width = 64
    height = 64
    
    def __init__(self, x, y):
        if Fly.image == None:
            Fly.image = load_image('./resources/monsters/fly.png')
        super().__init__(x, y)
        self.hp = 2
        self.frame = 0
        pass

    def add_event(self, event):
        pass

    def update(self):
        if self.hp > 0:
            self.frame = (self.frame + self.FPA_live * 1.0 / self.TPA_live * game_framework.frame_time) % 4
        elif self.hp == 0:
            self.frame = (self.frame + self.FPA_die * 1.0 / self.TPA_die * game_framework.frame_time) % 12
            if self.frame >= 11:
                self.hp = -1
                game_world.remove_object(self)
        pass

    def draw(self):
        if self.hp > 0:
            self.image.clip_draw(self.live_pos[int(self.frame)][0], self.live_pos[int(self.frame)][1], 32, 32, self.x, self.y, self.width, self.height)
        elif self.hp == 0:
            self.image.clip_draw(self.die_pos[int(self.frame)][0], self.die_pos[int(self.frame)][1], 64, 64, self.x, self.y, self.width, self.height)
        
        draw_rectangle(*self.get_bb())

    def handle_collision(self, other, group):
        super().handle_collision(other, group)
    

class Meat(Enemy):
    image = None
    
    def __init__(self):
        if Meat.image == None:
            Meat.image = load_image('./resources/monsters/meat.png')
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass
    

class Charger(Enemy):
    image = None
    
    def __init__(self):
        if Charger.image == None:
            self.image = load_image('./resources/monsters/charger.png')
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass