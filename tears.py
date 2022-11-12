from pico2d import *
import game_framework
import game_world

from creature import *

class Tear(Creature):
    image = None
    
    def __init__(self, x, y, direction):
        if Tear.image == None:
            Tear.image = load_image('resources/effect/bulletatlas.png')

        self.x, self.y = x, y + 16
        self.direction = direction
        self.hp = 1
        self.speed = 600
        self.width, self.height = 64, 64
        # print('Add Tear')
    
    def update(self):
        if self.direction == FRONT:
            self.y -= self.speed * game_framework.frame_time
        elif self.direction == BACK:
            self.y += self.speed * game_framework.frame_time
        elif self.direction == LEFT:
            self.x -= self.speed * game_framework.frame_time
        elif self.direction == RIGHT:
            self.x += self.speed * game_framework.frame_time
    
    def draw(self):
        if self.hp == 1:
            self.image.clip_draw(224, 480, 32, 32, self.x, self.y, self.width, self.height)