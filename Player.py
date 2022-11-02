from pico2d import *
from creature import Creature
import game_framework

from math import pi

MAX_HP = 24

X, Y = 0, 1
CLIP_SIZE = 32
IMAGE_SIZE = 96
IDLE = 0
FRONT, BACK, LEFT, RIGHT = 0b0001, 0b0010, 0b0100, 0b1000

# character image resource info
MOVE_CLIP_POS = ([0, 448], [32, 448], [64, 448], [96, 448], [128, 448], [160, 448], [192, 448], [224, 448], [192, 480], [224, 480])
MOVE_SIDE_CLIP_POS = ([0, 416], [32, 416], [64, 416], [96, 416], [128, 416], [160, 416], [192, 416], [224, 416], [0, 384], [32, 384])
HEAD_GAP = 29 

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 10

class Player(Creature):
    image = None
    
    def __init__(self):
        if Player.image == None:
            self.image = load_image('./resources/character.png')
        
        self.lookHead = FRONT
        self.lookBody = FRONT
        self.directionMove = IDLE
        self.directionAttack = IDLE
        self.frame = 0
        
        self.x = 720
        self.y = 408
        self.height = 96
        self.width = 96
        
        self.speed = 300
        
        self.max_hp = 6
        self.hp = 6
        
        self.key = 0
        
        self.shootSpeed = 10
        self.shootCoolTime = 0
        self.shootFrame = 0

    def add_event(self, event):
        pass

    def update(self):
        ### Move body ###
        self.move_body()
        ### Move head ###
        self.move_head()
    
        # print("shootFrame : ", self.shootFrame)
        
        # self.shootFrame = (self.shootFrame + (FRAME_PER_ACTION * self.shootSpeed)* ACTION_PER_TIME * game_framework.frame_time) % 200
        # if self.directionAttack == IDLE:
            # self.shootFrame = 0
    
    def draw(self):
        self.draw_body()
        self.draw_head()
        
    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            ### Key Down ###
            match event.key:
                case pico2d.SDLK_LEFT:
                    self.directionAttack |= LEFT
                    return
                case pico2d.SDLK_RIGHT:
                    self.directionAttack |= RIGHT
                    return
                case pico2d.SDLK_UP:
                    self.directionAttack |= BACK
                    return
                case pico2d.SDLK_DOWN:
                    self.directionAttack |= FRONT
                    return
                
                case pico2d.SDLK_a:
                    self.directionMove |= LEFT
                    return
                case pico2d.SDLK_d:
                    self.directionMove |= RIGHT
                    return
                case pico2d.SDLK_w:
                    self.directionMove |= BACK
                    return
                case pico2d.SDLK_s:
                    self.directionMove |= FRONT
                    return
        ### Key Up ###
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    self.directionAttack &= ~LEFT
                    return
                case pico2d.SDLK_RIGHT:
                    self.directionAttack &= ~RIGHT
                    return
                case pico2d.SDLK_UP:
                    self.directionAttack &= ~BACK
                    return
                case pico2d.SDLK_DOWN:
                    self.directionAttack &= ~FRONT
                    return
                
                case pico2d.SDLK_a:
                    self.directionMove &= ~LEFT
                    return
                case pico2d.SDLK_d:
                    self.directionMove &= ~RIGHT
                    return
                case pico2d.SDLK_w:
                    self.directionMove &= ~BACK
                    return
                case pico2d.SDLK_s:
                    self.directionMove &= ~FRONT
                    return
    
    def get_player_heart(self):
        return [self.max_hp, self.hp]
    
    def get_player_key(self):
        return self.key
    
    ### Player extra functions ###
    
    ### Draw Functions ###
    def draw_head(self):
        if self.lookHead == FRONT:
            self.image.clip_composite_draw(0 + (clamp(0, int(self.shootFrame), 1) * 32), 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookHead == BACK:
            self.image.clip_composite_draw(128 + (clamp(0, int(self.shootFrame), 1) * 32), 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookHead == LEFT:
            self.image.clip_composite_draw(64 + (clamp(0, int(self.shootFrame), 1) * 32), 480, CLIP_SIZE, CLIP_SIZE, pi, 'v', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookHead == RIGHT:
            self.image.clip_composite_draw(64 + (clamp(0, int(self.shootFrame), 1) * 32), 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
    
    def draw_body(self):
        if self.directionMove == IDLE:
            self.image.clip_composite_draw(MOVE_CLIP_POS[0][X], MOVE_CLIP_POS[0][Y], CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookBody == FRONT or self.lookBody == BACK:
            self.image.clip_composite_draw(MOVE_CLIP_POS[int(self.frame)][X], MOVE_CLIP_POS[int(self.frame)][Y], CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookBody == LEFT:
            self.image.clip_composite_draw(MOVE_SIDE_CLIP_POS[int(self.frame)][X], MOVE_SIDE_CLIP_POS[int(self.frame)][Y], CLIP_SIZE, CLIP_SIZE, pi, 'v', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookBody == RIGHT:
            self.image.clip_composite_draw(MOVE_SIDE_CLIP_POS[int(self.frame)][X], MOVE_SIDE_CLIP_POS[int(self.frame)][Y], CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
    ######################
    
    ### Player Move Functions ###
    def update_head(self):
        if self.directionMove == IDLE:
            self.lookBody = FRONT
        elif self.directionMove & LEFT:
            if self.directionMove & FRONT:
                self.lookBody = FRONT
                self.x -= self.speed // 1.5 * game_framework.frame_time
                self.y -= self.speed // 1.5 * game_framework.frame_time
            elif self.directionMove & BACK:
                self.lookBody = BACK
                self.x -= self.speed // 1.5 * game_framework.frame_time
                self.y += self.speed // 1.5 * game_framework.frame_time
            else:
                self.lookBody = LEFT
                self.x -= self.speed * game_framework.frame_time
                
        elif self.directionMove & RIGHT:
            if self.directionMove & FRONT:
                self.lookBody = FRONT
                self.x += self.speed // 1.5 * game_framework.frame_time
                self.y -= self.speed // 1.5 * game_framework.frame_time
            elif self.directionMove & BACK:
                self.lookBody = BACK
                self.x += self.speed // 1.5 * game_framework.frame_time
                self.y += self.speed // 1.5 * game_framework.frame_time
            else:
                self.lookBody = RIGHT
                self.x += self.speed * game_framework.frame_time
        elif self.directionMove & FRONT:
            self.lookBody = FRONT
            self.y -= self.speed * game_framework.frame_time
        elif self.directionMove & BACK:
            self.lookBody = BACK
            self.y += self.speed * game_framework.frame_time
        
        self.x = clamp(144 + 32, self.x, 1440 - 144 - 32)
        self.y = clamp(144 + 32, self.y, 864 - 144)
        
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        pass
    
    def update_body(self):
        if self.directionAttack == IDLE:
            self.lookHead = self.lookBody
        else:
            if self.directionAttack & LEFT:
                self.lookHead = LEFT
            elif self.directionAttack & RIGHT:
                self.lookHead = RIGHT
            elif self.directionAttack & FRONT:
                self.lookHead = FRONT
            elif self.directionAttack & BACK:
                self.lookHead = BACK
            
            # print("shootCoolTime : ", self.shootCoolTime)
            if self.shootCoolTime <= 0:
                # print("shoot")
                self.shootCoolTime = self.shootSpeed * 50
                self.shootFrame = 100
            
        if self.shootCoolTime > 0:
                # print("game_framework.frame_time : ", int(game_framework.frame_time * 1000))
                self.shootCoolTime -= 1
        if self.shootFrame > 0:
            self.shootFrame -= 1
        pass