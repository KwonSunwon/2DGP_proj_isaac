from pico2d import *
import game_framework
import game_world

from creature import *

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 12

PLAYER_TEAR = ([256, 192],[320, 192], [384, 192], [448, 192],
            [256, 128], [320, 128], [384, 128], [448, 128],
            [256, 64], [320, 64], [384, 64], [448, 64],
            [256, 0], [320, 0], [384, 0], [448, 0])

ENEMY_BULLET = ([576, 448], [640, 448], [704, 448], [768, 448],
                [576, 384], [640, 384], [704, 384], [768, 384],
                [576, 320], [640, 320], [704, 320], [768, 320],
                [576, 256], [640, 256], [704, 256], [768, 256])

class Tear(Creature):
    image = None
    
    def __init__(self, x, y, direction, type):
        if Tear.image == None:
            Tear.image = load_image('resources/effect/bulletatlas.png')

        # game_world.add_collision_group(None, self, 'room:tears')
        # game_world.add_collision_group(None, self, 'enemy:tears')

        self.type = type
        # print(type)
        self.CLIP_POS = PLAYER_TEAR if self.type == 0 else ENEMY_BULLET

        self.x, self.y = x, y + 16
        self.direction = direction
        self.hp = 1
        self.speed = 600
        self.draw_width, self.draw_height = 64, 64
        self.width, self.height = 32, 32
        
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
            # print(self.kill_frame)
        
        
    
    def draw(self):
        if self.hp == 1:
            if self.type == 0:
                # print('Player Tear')
                self.image.clip_draw(224, 480, 32, 32, self.x, self.y, self.draw_width, self.draw_height)
            elif self.type == 1:
                self.image.clip_draw(self.CLIP_POS[0][0], self.CLIP_POS[0][1], 64, 64, self.x, self.y, self.draw_width + 64, self.draw_height + 64)
        elif self.hp == 0:
            self.image.clip_draw(self.CLIP_POS[int(self.kill_frame)][0], self.CLIP_POS[int(self.kill_frame)][1], 64, 64, self.x, self.y, self.draw_width + 64, self.draw_height + 64)
        
        draw_rectangle(*self.get_bb())
            
            
    def handle_collision(self, other, group):
        # print('Tear collision')
        if group == 'room:tears':
            self.hp = 0
        elif group == 'enemy:tears':
            self.hp = 0
        elif group == 'player:bullet':
            self.hp = 0