from posixpath import isabs
from tkinter import Frame
from turtle import back
from pico2d import *

from math import pi

MAX_HP = 24

X, Y = 0, 1
CLIP_SIZE = 32
IMAGE_SIZE = 96
IDLE = 0
FRONT, BACK, LEFT, RIGHT = 0b0001, 0b0010, 0b0100, 0b1000

MOVE_CLIP_POS = [[0, 448], [32, 448], [64, 448], [96, 448], [128, 448], [160, 448], [192, 448], [224, 448], [192, 480], [224, 480]]
MOVE_SIDE_CLIP_POS = [[0, 416], [32, 416], [64, 416], [96, 416], [128, 416], [160, 416], [192, 416], [224, 416], [0, 384], [32, 384]]
HEAD_GAP = 29 

class Character:
    image = None

    def __init__(self):
        if Character.image == None:
            self.image = load_image('./resources/character.png')
        
        self.lookHead = FRONT
        self.lookBody = FRONT
        self.directionMove = IDLE
        self.directionAttack = IDLE
        self.frame = 0
        self.x = 720
        self.y = 408
        self.max_hp = 6
        self.cur_hp = 6

    def add_event(self, event):
        pass

    def update(self):
        if self.directionMove == IDLE:
            self.lookBody = FRONT
        elif self.directionMove & LEFT:
            if self.directionMove & FRONT:
                self.lookBody = FRONT
            elif self.directionMove & BACK:
                self.lookBody = BACK
            else:
                self.lookBody = LEFT
        elif self.directionMove & RIGHT:
            if self.directionMove & FRONT:
                self.lookBody = FRONT
            elif self.directionMove & BACK:
                self.lookBody = BACK
            else:
                self.lookBody = RIGHT
        
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
        
        self.frame = (self.frame + 1) % 10

    ### Draw Functions ###
    def draw_head(self):
        if self.lookHead == FRONT:
            self.image.clip_composite_draw(0, 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookHead == BACK:
            self.image.clip_composite_draw(128, 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookHead == LEFT:
            self.image.clip_composite_draw(64, 480, CLIP_SIZE, CLIP_SIZE, pi, 'v', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookHead == RIGHT:
            self.image.clip_composite_draw(64, 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
            
        # if self.lookBody == FRONT or self.lookBody == IDLE:
        #     self.image.clip_composite_draw(0, 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        # elif self.lookBody == LEFT:
        #     self.image.clip_composite_draw(64, 480, CLIP_SIZE, CLIP_SIZE, pi, 'v', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        # elif self.lookBody == RIGHT:
        #     self.image.clip_composite_draw(64, 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        # elif self.lookBody == BACK:
        #     self.image.clip_composite_draw(128, 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
    
    def draw_body(self):
        if self.directionMove == IDLE:
            self.image.clip_composite_draw(MOVE_CLIP_POS[0][X], MOVE_CLIP_POS[0][Y], CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookBody == FRONT or self.lookBody == BACK:
            self.image.clip_composite_draw(MOVE_CLIP_POS[self.frame][X], MOVE_CLIP_POS[self.frame][Y], CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookBody == LEFT:
            self.image.clip_composite_draw(MOVE_SIDE_CLIP_POS[self.frame][X], MOVE_SIDE_CLIP_POS[self.frame][Y], CLIP_SIZE, CLIP_SIZE, pi, 'v', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
        elif self.lookBody == RIGHT:
            self.image.clip_composite_draw(MOVE_SIDE_CLIP_POS[self.frame][X], MOVE_SIDE_CLIP_POS[self.frame][Y], CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
    ######################
    
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
                    # self.lookBody = LEFT
                    return
                case pico2d.SDLK_d:
                    self.directionMove |= RIGHT
                    # self.lookBody = RIGHT
                    return
                case pico2d.SDLK_w:
                    self.directionMove |= BACK
                    # self.lookBody = BACK
                    return
                case pico2d.SDLK_s:
                    self.directionMove |= FRONT
                    # self.lookBody = FRONT
                    return
        ### Key Up ###
        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    # print("test - left")
                    self.directionAttack &= ~LEFT
                    return
                case pico2d.SDLK_RIGHT:
                    # print("test - right")
                    self.directionAttack &= ~RIGHT
                    return
                case pico2d.SDLK_UP:
                    # print("test - up")
                    self.directionAttack &= ~BACK
                    return
                case pico2d.SDLK_DOWN:
                    # print("test - down")
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