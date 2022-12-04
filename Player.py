from pico2d import *
from creature import Creature
import game_framework
import game_world

from math import pi

from tears import Tear

import static
import server

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

HIT_CLIP_POS = ([128, 256])

# Crop X, Y, Position X, Y, SCALE X, Y, ROTATE
DEAD = ([0, 256, 0, 1, 1, 1, 0], [0, 256, 0, 1, 1, 1, 0], [0, 256, 0, 1, 1, 1, 0], [0, 256, 0, 2, 1.1, 0.9, 0], [0, 320, 0, 2, 1.2, 0.8, 0], 
        [0, 320, 0, 2, 1.2, 0.8, 0], [0, 320, 0, 1, 0.8, 1.2, 0], [0, 320, 0, 1, 0.8, 1.2, 0], [128, 256, 0, 1, 0.8, 1.2, 0], [128, 256, 0, 1, 0.8, 1.2, 0],
        [128, 256, 4, 1, 1, 1, 16], [128, 256, 4, 1, 1, 1, 35], [192, 320, 21, 5, 1.1, 0.9, 0], [192, 320, 21, 5, 1.1, 0.9, 0], [192, 320, 21, 5, 1, 1, 0],
        [192, 320, 19, 5, 1, 1, 0], [192, 320, 21, 5, 1, 1, 0], [192, 320, 19, 5, 1, 1, 0], [192, 320, 21, 5, 1, 1, 0], [192, 320, 19, 5, 1, 1, 0],
        [192, 320, 21, 5, 1, 1, 0], [192, 320, 20, 5, 1, 1, 0])
# Crop X, Y, Position X, Y, SCALE X, Y, OPACITY
GHOST = ([0, 16, 22, 19, 1, 1, 0], [0, 16, 22, 19, 1, 1, 0], [0, 16, 22, 19, 1, 1, 0], [32, 16, 25, 30, 0.9, 1.1, 0.4], [32, 16, 25, 30, 0.9, 1.1, 0.4],
        [32, 16, 25, 30, 0.9, 1.1, 0.4], [64, 16, 25, 41, 1, 1.1, 0.6], [64, 16, 25, 41, 1, 1.1, 0.6], [64, 16, 25, 41, 1, 1.1, 0.6], [96, 16, 22, 53, 1.1, 0.9, 0.6],
        [96, 16, 22, 53, 1.1, 0.9, 0.6], [96, 16, 22, 53, 1.1, 0.9, 0.6], [128, 16, 18, 65, 1, 1, 0.6], [128, 16, 18, 65, 1, 1, 0.6], [128, 16, 18, 65, 1, 1, 0.6],
        [0, 16, 18, 78, 1, 1, 0.6], [0, 16, 18, 78, 1, 1, 0.6], [32, 16, 16, 86, 0.9, 1.1, 0.6], [32, 16, 16, 86, 0.9, 1.1, 0.6], [64, 16, 18, 94, 1, 1, 0.6],
        [64, 16, 18, 94, 1, 1, 0.6], [96, 16, 21, 103, 1.1, 0.9, 0.6], [96, 16, 21, 103, 1.1, 0.9, 0.6], [128, 16, 23, 111, 1, 1, 0.6], [128, 16, 23, 111, 1, 1, 0.6],
        [0, 16, 19, 117, 1, 1, 0.45], [0, 16, 19, 117, 1, 1, 0.45], [32, 16, 16, 124, 0.9, 1.1, 0.35], [32, 16, 16, 124, 0.9, 1.1, 0.35], [64, 16, 18, 136, 1, 1, 0.23],
        [64, 16, 18, 136, 1, 1, 0.23], [96, 16, 26, 144, 1.1, 0.9, 0.11], [96, 16, 26, 144, 1.1, 0.9, 0.11], [128, 16, 18, 180, 1, 1, 0], [128, 16, 18, 180, 1, 1, 0])

CLIP_DEAD = {'body': DEAD, 'ghost': GHOST}
CLIP_SIZE_DEAD = 64
FPA = {'body': len(DEAD), 'ghost': len(GHOST)}
TPA = {'body': 0.5, 'ghost': 0.5}

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 10

class Player(Creature):
    image = None
    image_ghost = None
    
    def __init__(self):
        if Player.image == None:
            Player.image = load_image('./resources/character.png')
        if Player.image_ghost == None:
            Player.image_ghost = load_image('./resources/ghost.png')
        
        self.lookHead = FRONT
        self.lookBody = FRONT
        self.directionMove = IDLE
        self.directionAttack = IDLE
        self.frame = 0
        
        self.prevX = 0
        self.prevY = 0
        
        self.x = 720
        self.y = 408
        # self.x = 720
        # self.y = 715

        self.height = 96
        self.width = 96
        
        self.speed = 300
        
        self.max_hp = 6
        self.hp = 6
        
        self.key = 0
        
        self.shootSpeed = 5
        self.shootCoolTime = 0
        self.shootFrame = 0

        self.hitCoolTime = 0

    def add_event(self, event):
        pass

    def update(self):
        if self.hp > 0:
            self.update_body()
            self.update_head()
            self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10   
            if self.hitCoolTime > 0:
                self.hitCoolTime -= 1000 * game_framework.frame_time / 2
        elif self.hp == 0:
            self.frame = self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
            if self.frame >= FPA['body'] + FPA['ghost'] - 1:
                self.hp = -1
                # game_framework.change_state(game_over_state)
    
    def draw(self):
        if self.hp > 0:
            if self.hitCoolTime <= 0:
                self.image.opacify(1)
                self.draw_body()
                self.draw_head()
            elif self.hitCoolTime > 0:
                self.draw_hit()
        elif self.hp == 0:
            frame_ghost = int(self.frame)
            frame_body = clamp(0, int(self.frame), len(DEAD) - 1)
            self.image.clip_composite_draw(CLIP_DEAD['body'][frame_body][0],
                                            CLIP_DEAD['body'][frame_body][1],
                                            CLIP_SIZE_DEAD, CLIP_SIZE_DEAD,
                                            CLIP_DEAD['body'][frame_body][6] * pi / 180, ' ',
                                            self.x + CLIP_DEAD['body'][frame_body][2],
                                            self.y + CLIP_DEAD['body'][frame_body][3],
                                            int(160 * CLIP_DEAD['body'][frame_body][4]),
                                            int(160 * CLIP_DEAD['body'][frame_body][5]))
            if frame_ghost >= 22:
                frame_ghost -= 22
                self.image_ghost.opacify(CLIP_DEAD['ghost'][frame_ghost][6])
                self.image_ghost.clip_draw(CLIP_DEAD['ghost'][frame_ghost][0],
                                            CLIP_DEAD['ghost'][frame_ghost][1],
                                            32, 48,
                                            self.x + CLIP_DEAD['ghost'][frame_ghost][2],
                                            self.y + CLIP_DEAD['ghost'][frame_ghost][3],
                                            int(IMAGE_SIZE * CLIP_DEAD['ghost'][frame_ghost][4]),
                                            int(IMAGE_SIZE * CLIP_DEAD['ghost'][frame_ghost][5]))
            
        draw_rectangle(*self.get_bb())
        
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
    
    # def get_state(self):
    #     return self.get_player_heart(), self.get_player_key()
    
    def get_heart(self):
        return [self.max_hp, self.hp]
    
    def get_key(self):
        return self.key
    
    def get_bb(self):
        return self.x - 20, self.y - 24, self.x + 20, self.y + 12
    
    def handle_collision(self, other, group):
        if group == 'player:room':
            # print(other.type)
            if other.type == 'wall' or other.type == 'rock':
                # print("wall")
                self.x, self.y = self.prevX, self.prevY
                
            elif other.type == 'door':
                if other.isOpen:
                    self.x, self.y = other.get_position()
                    server.stage.enter_room(other.get_direction())
                else:
                    self.x, self.y = self.prevX, self.prevY
            
            elif other.type == 'spike' and self.hitCoolTime <= 0:
                self.hp -= 1
                self.hitCoolTime = 250
                self.frame = 0
                if self.hp <= 0:
                    pass
            elif other.type == 'poop' and other.hp != 0:
                self.x, self.y = self.prevX, self.prevY
                
            elif other.type == 'trapdoor':
                server.stage.changeStage(server.stage.level + 1)
                self.x, self.y = 720, 408
                pass
                    
        elif group == 'player:enemy' and self.hitCoolTime <= 0:
            self.hp -= 1
            self.hitCoolTime = 250
            self.frame = 0
            if self.hp <= 0:
                # game_framework.change_state(static.game_over)
                pass
        elif group == 'player:bullet':
            self.hp -= 1
            self.hitCoolTime = 250
            self.frame = 0
            if self.hp <= 0:
                # game_framework.change_state(static.game_over)
                pass
    
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

    def draw_hit(self):
        if int(self.frame) % 2 == 0:
            self.image.opacify(0.5)
        else:
            self.image.opacify(1)
        self.image.clip_draw(HIT_CLIP_POS[0], HIT_CLIP_POS[1], CLIP_SIZE * 2, CLIP_SIZE * 2, self.x, self.y + 32, IMAGE_SIZE * 2, IMAGE_SIZE * 2)
    ######################
    
    ### Player Update Functions ###
    def update_body(self):
        self.prevX, self.prevY = self.x, self.y
        
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
        
        # self.x = clamp(144 + 32, self.x, 1440 - 144 - 32)
        # self.y = clamp(144 + 32, self.y, 864 - 144)
        pass
    
    def update_head(self):
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
                if self.lookHead == LEFT:
                    tear_direction = pi
                elif self.lookHead == RIGHT:
                    tear_direction = 0.0
                elif self.lookHead == FRONT:
                    tear_direction = 3 * pi / 2
                elif self.lookHead == BACK:
                    tear_direction = pi / 2
                    
                tear = Tear(self.x, self.y, tear_direction, 0)
                game_world.add_object(tear, 4)
                game_world.add_collision_group(None, tear, 'room:tears')
                game_world.add_collision_group(None, tear, 'enemy:tears')
                
                self.shootCoolTime = self.shootSpeed * 50
                self.shootFrame = 100
            
        if self.shootCoolTime > 0:
                # print("game_framework.frame_time : ", int(game_framework.frame_time * 1000))
                self.shootCoolTime -= 1000 * game_framework.frame_time / 2
        if self.shootFrame > 0:
            self.shootFrame -= 1000 * game_framework.frame_time / 2
        pass
    ##############################