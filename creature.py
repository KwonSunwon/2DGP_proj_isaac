import pico2d
import game_framework
import game_world

class Creature:
    x, y = 0, 0
    width, height = 0, 0
    speed = 0
    hp = 0
    frame = 0
    
    flying = False
    
    def __init__(self):    
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - self.width // 2, self.y - self.height // 2, self.x + self.width // 2, self.y + self.height // 2
    