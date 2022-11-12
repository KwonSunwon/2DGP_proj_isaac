from pico2d import *
import game_framework
import game_world

from creature import *

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 12

CLIP_POS = ([256, 192],[320, 192], [384, 192], [448, 192],
            [256, 128], [320, 128], [384, 128], [448, 128],
            [256, 64], [320, 64], [384, 64], [448, 64],
            [256, 0], [320, 0], [384, 0], [448, 0])

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
        
        self.kill_frame = 0
        # print('Add Tear')
    
    def update(self):
        if self.hp == 1:
            if self.direction == FRONT:
                self.y -= self.speed * game_framework.frame_time
            elif self.direction == BACK:
                self.y += self.speed * game_framework.frame_time
            elif self.direction == LEFT:
                self.x -= self.speed * game_framework.frame_time
            elif self.direction == RIGHT:
                self.x += self.speed * game_framework.frame_time
        elif self.hp == 0:
            if self.kill_frame >= 15:
                self.hp = -1
                game_world.remove_object(self)
                
            self.kill_frame = self.kill_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
            print(self.kill_frame)
        
        
    
    def draw(self):
        if self.hp == 1:
            self.image.clip_draw(224, 480, 32, 32, self.x, self.y, self.width, self.height)
        elif self.hp == 0:
            self.image.clip_draw(CLIP_POS[int(self.kill_frame)][0], CLIP_POS[int(self.kill_frame)][1], 64, 64, self.x, self.y, self.width + 64, self.height + 64)
            
            
    def handle_collision(self, other, group):
        print('Tear collision')
        if group == 'room:tears':
            if self.hp == 1:
                self.hp = 0