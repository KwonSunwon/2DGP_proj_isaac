from tkinter import Frame
from pico2d import *

from math import pi

MAX_HP = 24

X, Y = 0, 1
CLIP_SIZE = 32
IMAGE_SIZE = 96
FRONT, BACK, LEFT, RIGHT = range(4)

MOVE_CLIP_POS = [[0, 448], [32, 448], [64, 448], [96, 448], [128, 448], [160, 448], [192, 448], [224, 448], [192, 480], [224, 480]]
MOVE_SIDE_CLIP_POS = [[0, 416], [32, 416], [64, 416], [96, 416], [128, 416], [160, 416], [192, 416], [224, 416], [0, 384], [32, 384]]
HEAD_GAP = 29

class Character:
    image = None

    def __init__(self):
        if Character.image == None:
            self.image = load_image('./resources/character.png')
        
        self.direction_head = LEFT
        self.direction_body = FRONT
        self.frame = 0
        self.x = 720
        self.y = 408
        self.max_hp = 6
        self.cur_hp = 6

    def add_event(self, event):
        pass

    def update(self):
        pass

    ### Draw Functions ###
    def draw_head(self):
        if self.direction_head == FRONT:
            self.image.clip_composite_draw(0, 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        elif self.direction_head == LEFT:
            self.image.clip_composite_draw(64, 480, CLIP_SIZE, CLIP_SIZE, pi, 'v', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        elif self.direction_head == RIGHT:
            self.image.clip_composite_draw(64, 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
        elif self.direction_head == BACK:
            self.image.clip_composite_draw(128, 480, CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y + HEAD_GAP, IMAGE_SIZE, IMAGE_SIZE)
    
    def draw_body(self):
        if self.direction_body == FRONT or self.direction_body == BACK:
            self.image.clip_composite_draw(MOVE_CLIP_POS[self.frame][X], MOVE_CLIP_POS[self.frame][Y], CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
        elif self.direction_body == LEFT:
            self.image.clip_composite_draw(MOVE_SIDE_CLIP_POS[self.frame][X], MOVE_SIDE_CLIP_POS[self.frame][Y], CLIP_SIZE, CLIP_SIZE, pi, 'v', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
        elif self.direction_body == RIGHT:
            self.image.clip_composite_draw(MOVE_SIDE_CLIP_POS[self.frame][X], MOVE_SIDE_CLIP_POS[self.frame][Y], CLIP_SIZE, CLIP_SIZE, 0, '', self.x, self.y, IMAGE_SIZE, IMAGE_SIZE)
            
    ######################
    
    def draw(self):
        self.draw_body()
        self.draw_head()
        
    def handle_event(self, event):
        pass
