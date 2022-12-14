import pico2d
import game_framework
import game_world

FRONT, BACK, LEFT, RIGHT = 0b0001, 0b0010, 0b0100, 0b1000

class Creature:

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
        if self.hp <= 0:
            return -100, -100, -100, -100
        return self.x - self.width // 2, self.y - self.height // 2, self.x + self.width // 2, self.y + self.height // 2
    
    def handle_collision(self, other, group):
        pass