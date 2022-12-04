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
    
    IDLE = ()
    
    CLIP = {'idle': IDLE}

    def __init__(self, x, y):
        if Monstro.image == None:
            Monstro.image = load_image('resources/monsters/monstro.png')
        super().__init__(x, y)
        
    def update(self):
        self.bt.run()
    
    def draw(self):
        pass    
        
    def handle_collision(self, other, group):
        return super().handle_collision(other, group)
    
    def build_behavior_tree(self):
        
        monstro = SequenceNode("Monstro")
        
        self.bt = BehaviorTree(monstro)

    
class BabyPlum(Enemy):
    type = 'babyplum'
    image = None
    
    ATTACK_LIST = ['pattern1', 'pattern2']
    
    IDLE = ([0, 256], [256, 320])
    PATTERN1 = ([0, 256], [256, 320], [0, 128], [64, 128], [0, 128],
                [64, 128], [64, 128], [128, 128], [192, 128], [256, 128],
                [320, 128], [320, 128], [0, 64], [0, 64], [64, 64],
                [64, 64], [128, 64], [192, 64], [256, 64], [192, 64],
                [256, 64], [192, 64], [256, 64], [192, 64], [256, 64],
                [192, 64], [256, 64], [192, 64], [256, 64], [192, 64],
                [0, 256], [256, 320], [0, 256])
    PATTERN2 = ()
    
    CLIP = {'idle' : IDLE, 'pattern1' : PATTERN1, 'pattern2' : PATTERN2}
    FPA = {'idle' : 2, 'pattern1' : 33, 'pattern2' : 0}
    TPA = {'idle' : 0.2, 'pattern1' : 1, 'pattern2' : 1}
    SPEED = {'idle' : 100, 'pattern1' : 200, 'pattern2' : 0}    

    CLIP_SIZE = 64
    
    draw_width = 192
    draw_height = 192
    
    width = 128
    height = 128
    
    
    def __init__(self, x, y):
        if BabyPlum.image == None:
            BabyPlum.image = load_image('resources/monsters/babyplum.png')
        super().__init__(x, y)
        
        self.hp = 20
        
        self.speed = self.SPEED['idle']
        self.direction = random.random() * 2 * math.pi
        
        self.next_pattern = random.randint(0, 1)
        
        self.frame = 0
        self.action = 'idle'
        self.idle_timer = 1
        
        self.is_shoot = False
        
        self.build_behavior_tree()

        self.shadow.opacify(0.4)
        pass
    
    def update(self):
        self.bt.run()
        
        if self.hp:
            self.x += self.speed * math.cos(self.direction) * game_framework.frame_time
            self.y += self.speed * math.sin(self.direction) * game_framework.frame_time
        
        self.frame = (self.frame + self.FPA[self.action] * 1.0 / self.TPA[self.action] * game_framework.frame_time) % self.FPA[self.action]
        
        pass
    
    def draw(self):
        self.shadow.draw(self.x, self.y - 64)
        self.image.clip_draw(self.CLIP[self.action][int(self.frame)][0], self.CLIP[self.action][int(self.frame)][1], self.CLIP_SIZE, self.CLIP_SIZE, self.x, self.y, self.draw_width, self.draw_height)
        
        draw_rectangle(*self.get_bb())
        pass
    
    def handle_collision(self, other, group):
        if group == 'room:enemy':
            if other.type == 'wall' or other.type == 'door':
                self.direction = (self.direction + math.pi)
                return
        return super().handle_collision(other, group)
    
    def build_behavior_tree(self):
        plum_wander = LeafNode("PlumWander", self.wander)
        plum_pattern1 = LeafNode("PlumPattern1", self.pattern1)
        plum_pattern2 = LeafNode("PlumPattern2", self.pattern2)
        
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
        self.speed = self.SPEED['idle']
        
        self.idle_timer -= game_framework.frame_time
        
        if self.idle_timer <= 0:
            self.idle_timer -= game_framework.frame_time
            self.idle_timer = 1
            self.next_pattern = random.choice(self.ATTACK_LIST)
            self.direction = math.atan2(server.player.y - self.y, server.player.x - self.x)
            self.is_shoot = False
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    
    # pattern 1
    def pattern1(self):
        if self.next_pattern != 'pattern1':
            return BehaviorTree.FAIL
        
        self.action = 'pattern1'
        
        if self.frame >= self.FPA[self.action] - 1:
            self.frame = 0
            self.direction = random.random() * 2 * math.pi
            return BehaviorTree.SUCCESS
        
        if self.frame <= 7:
            self.speed = 0
        else:
            self.speed = self.SPEED['pattern1']
        
        if int(self.frame) == 7 and not self.is_shoot:
            self.is_shoot = True
            self.shoot_12way()
            
        return BehaviorTree.RUNNING
    
    # pattern 2
    def pattern2(self):
        # self.action = 'pattern2'
        # self.speed = self.SPEED['pattern2']
        pass
    
    def shoot_12way(self):
        print('shoot')
        tears = []
        step = 2 * math.pi / 12
        for i in range(12):
            tears.append(Tear(self.x, self.y, self.direction + step * i, 1))
        game_world.add_objects(tears, 4)
        game_world.add_collision_group(None, tears, 'player:bullet')
        game_world.add_collision_group(None, tears, 'room:tears')
        pass