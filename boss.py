from pico2d import *

from enemy import Enemy
from tears import Tear

import game_framework
import game_world

import server

from behavior_tree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

import random
import math


class Monstro(Enemy):
    type = 'monstro'
    image = None

    def __init__(self, x, y):
        if Monstro.image == None:
            Monstro.image = load_image('resources/monsters/monstro.png')
        super().__init__(x, y)
        
    
class BabyPlum(Enemy):
    type = 'babyplum'
    image = None
    
    IDLE = ([0, 256], [256, 320])
    SLAMS = ([])
    
    CLIP = {'idle' : IDLE, 'slams' : SLAMS}
    FPA = {'idle' : 2, 'slams' : 0}
    TPA = {'idle' : 0.2, 'slams' : 0.2}

    CLIP_SIZE = 64
    
    draw_width = 192
    draw_height = 192
    
    width = 128
    height = 128
    
    IDLE_SPEED = 100
    
    def __init__(self, x, y):
        if BabyPlum.image == None:
            BabyPlum.image = load_image('resources/monsters/babyplum.png')
        super().__init__(x, y)
        
        self.hp = 20
        
        self.speed = 100
        self.direction = random.random() * 2 * math.pi
        
        self.next_pattern = random.randint(0, 1)
        
        self.frame = 0
        self.action = 'idle'
        self.idle_timer = 1
        
        self.build_behavior_tree()

        self.shadow.opacify(0.4)
        pass
    
    def update(self):
        self.bt.run()
        
        self.frame = (self.frame + self.FPA[self.action] * 1.0 / self.TPA[self.action] * game_framework.frame_time) % self.FPA[self.action]
        
        pass
    
    def draw(self):
        self.shadow.draw(self.x, self.y - 64)
        self.image.clip_draw(self.CLIP[self.action][int(self.frame)][0], self.CLIP[self.action][int(self.frame)][1], self.CLIP_SIZE, self.CLIP_SIZE, self.x, self.y, self.draw_width, self.draw_height)
        
        draw_rectangle(*self.get_bb())
        pass
    
    def handle_collision(self, other, group):
        return super().handle_collision(other, group)
    
    def build_behavior_tree(self):
        plum_wander = LeafNode("PlumWander", self.wander)
        
        #pattern 1
        plum_short_dash = LeafNode("PlumShortDash", self.short_dash)
        plum_shoot_12way = LeafNode("PlumShoot12Way", self.shoot_12way)

        plum_pattern1 = SequenceNode("PlumPattern1")
        plum_pattern1.add_children(plum_short_dash, plum_shoot_12way)
        
        #pattern 2
        plum_slams = LeafNode("PlumSlams", self.slams)
        plum_shoot_8way = LeafNode("PlumShoot8Way", self.shoot_8way)
        plum_shoot_14way = LeafNode("PlumShoot14Way", self.shoot_14way)
        
        plum_pattern2 = SequenceNode("PlumPattern2")
        plum_pattern2.add_children(plum_slams, plum_shoot_8way, plum_shoot_14way)
        
        # selector
        plum_action_selector = SelectorNode("PlumActionSelector")
        plum_action_selector.add_children(plum_pattern1, plum_pattern2)
        
        # root
        plum = SequenceNode("Plum")
        plum.add_children(plum_wander, plum_action_selector)

        self.bt = BehaviorTree(plum)
        pass
    
    # behavior
    def wander(self):
        self.action = 'idle'
        self.speed = self.IDLE_SPEED
        
        self.idle_timer -= game_framework.frame_time
        
        if self.idle_timer <= 0:
            self.idle_timer -= game_framework.frame_time
            self.idle_timer = 1
            self.direction = random.random() * 2 * math.pi
            self.next_pattern = random.randint(0, 1)
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    
    # pattern 1
    def short_dash(self):
        pass
    
    def shoot_12way(self):
        pass
    
    # pattern 2
    def slams(self):
        pass
    
    def shoot_8way(self):
        pass
    
    def shoot_14way(self):
        pass
    
    