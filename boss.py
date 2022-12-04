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
    
    # Crop X, Y, Scale X, Y, Position X, Y
    IDLE = ([0, 256, 1, 1, 0, 0], [256, 320, 1, 1, 0, 0])
    
    PATTERN1 = ([0, 256, 1, 1, 0, 0], [256, 320, 1.05, 0.95, 0, 0], [0, 128, 1.1, 0.9, 0, 0], [64, 128, 1.13, 0.87, 0, 0], [0, 128, 1.15, 0.85, 0, 0],
                [64, 128, 1.15, 0.85, 0, 0], [64, 128, 1.12, 0.88, 0, 0], [128, 128, 1.05, 0.95, 0, 0], [192, 128, 1, 1, 0, 0], [256, 128, 0.95, 1.05, 0, 0],
                [320, 128, 0.9, 1.1, 0, 0], [320, 128, 0.9, 1.1, 0, 0], [0, 64, 0.95, 1.05, 0, 0], [0, 64, 0.95, 1.05, 0, 0], [64, 64, 1.1, 0.9, 0, 0],
                [64, 64, 1.1, 0.9, 0, 0], [128, 64, 1.15, 0.85, 0, 0], [192, 64, 1, 1, 0, 0], [256, 64, 0.85, 1.15, 0, 0], [192, 64, 0.98, 1.02, 0, 0],
                [256, 64, 1.1, 0.9, 0, 0], [192, 64, 1.02, 0.98, 0, 0], [256, 64, 0.95, 1.05, 0, 0], [192, 64, 0.97, 1.03, 0, 0], [256, 64, 1, 1, 0, 0],
                [192, 64, 1, 1, 0, 0], [256, 64, 1, 1, 0, 0], [192, 64, 0.95, 1.05, 0, 0], [256, 64, 0.90, 1.1, 0, 0], [192, 64, 1, 1, 0, 0],
                [0, 256, 1.1, 0.9, 0, 0], [256, 320, 1.05, 0.95, 0, 0], [0, 256, 0.98, 1.02, 0, 0])
    
    PATTERN2 = ([0, 256, 1, 1, 0, 0], [256, 320, 1.05, 0.95, 0, -1], [0, 256, 1.1, 0.9, 0, -2], [256, 320, 1.13, 0.87, 0, -3], [0, 256, 1.15, 0.85, 0, -4],
                [256, 320, 1, 1, 0, 2], [320, 64, 0.8, 1.2, 0, 7], [384, 64, 0.95, 1.14, 0, 12], [320, 64, 1.1, 0.9, 0, 17], [384, 64, 1.2, 0.8, 0, 16],
                [320, 64, 0.95, 1.05, 0, 16], [384, 64, 0.98, 1.02, 0, 16], [320, 64, 1, 1, 0, 17], [384, 64, 1, 1, 0, 18], [320, 64, 1, 1, 0, 18],
                [384, 64, 0.9, 1.1, 0, 18], [320, 64, 0.8, 1.2, 0, 17], [384, 64, 0.7, 1.3, 0, 17], [320, 64, 0.6, 1.4, 0, -6], [448, 64, 0.9, 1.1, -2, -28],
                [448, 64, 1.15, 0.85, 2, -28], [448, 64, 1.2, 0.8, -2, -28], [448, 64, 1.22, 0.78, 2, -28], [448, 64, 1.23, 0.77, -2, -28], [448, 64, 1.24, 0.76, 1, -28],
                [448, 64, 1.25, 0.75, -1, -28], [448, 64, 1.26, 0.74, 1, -28], [448, 64, 1.26, 0.74, -1, -28], [448, 64, 1.27, 0.73, 0, -28], [448, 64, 1, 1, 0, -28],
                [0, 384, 0.8, 1.2, 0, -6], [0, 384, 0.95, 1.05, 0, 1], [0, 384, 1.1, 0.9, 0, 8], [64, 384, 1, 1, 0, 8], [64, 384, 0.9, 1.1, 0, 7],
                [0, 384, 0.98, 1.02, 0, 2], [0, 256, 1.05, 0.95, 0, -3], [256, 320, 1.02, 0.98, 0, 1], [0, 256, 1, 1, 0, 0], [256, 320, 1, 1, 0, 0])
    
    DEATH = ([0, 0, 0.9, 1.1, 0, -1], [64, 0, 1, 1, 0, 3], [0, 0, 1.1, 0.9, 0, 6], [64, 0, 1, 1, 0, 7], [0, 0, 0.9, 1.1, 0, 8],
            [64, 0, 1, 1, 0, 8], [0, 0, 1.1, 0.9, 0, 8], [0, 0, 0.9, 1.1, 0, 8], [64, 0, 0.7, 1.3, 0, 2], [64, 0, 0.7, 1.3, 0, -8],
            [384, 128, 1.3, 0.7, -2, -28], [384, 128, 1, 1, 2, 0], [384, 128, 0.8, 1.2, 0, -24], [384, 128, 0.95, 1.05, 0, -20], [384, 128, 1, 1, 0, -20],
            [384, 128, 0.8, 1.2, 0, -24], [384, 128, 1, 1, -3, -28], [384, 128, 1.15, 0.85, -3, -28], [384, 128, 1.08, 0.92, 3, -28], [384, 128, 1, 1, -3, -28],
            [384, 128, 1.08, 0.92, 3, -28], [384, 128, 1.09, 0.91, -2, -28], [384, 128, 1.1, 0.9, 2, -28], [384, 128, 1.11, 0.89, -2, -28], [384, 128, 1.12, 0.88, 2, -28],
            [384, 128, 1.12, 0.88, -1, -28], [384, 128, 1.13, 0.87, 1, -28], [384, 128, 1.13, 0.87, -1, -28], [384, 128, 1.14, 0.86, 1, -28], [384, 128, 1.14, 0.86, -1, -28],
            [384, 128, 1.14, 0.86, 1, -28], [384, 128, 1.15, 0.85, -1, -28], [384, 128, 1.15, 0.85, 1, -28], [384, 128, 1.15, 0.85, -1, -28], [384, 128, 1.15, 0.85, 1, -28],
            [384, 128, 1.15, 0.85, 0, -28], [384, 128, 1.15, 0.85, 0, -28], [384, 128, 1.15, 0.85, 0, -28], [384, 128, 1.15, 0.85, 0, -28], [384, 128, 1.15, 0.85, 0, -28],
            [384, 128, 1.15, 0.85, 0, -28], [384, 128, 1.15, 0.85, 0, -28], [384, 128, 1.15, 0.85, 0, -28], [384, 128, 1.16, 0.84, 0, -28], [384, 128, 1.16, 0.84, 0, -28],
            [384, 128, 0.8, 1.2, 0, -28], [384, 128, 0.8, 1.2, 0, -28], [384, 128, 0.75, 1.25, 0, -28], [384, 128, 0.75, 1.25, 0, -28], [384, 128, 2.0, 0.5, 0, -28],
            [384, 128, 2.0, 0.5, 0, -28], [384, 128, 3.0, 0.2, 0, -28])
    
    CLIP = {'idle' : IDLE, 'pattern1' : PATTERN1, 'pattern2' : PATTERN2, 'death' : DEATH}
    FPA = {'idle' : len(IDLE), 'pattern1' : len(PATTERN1), 'pattern2' : len(PATTERN2), 'death' : len(DEATH)}
    TPA = {'idle' : 0.2, 'pattern1' : 1, 'pattern2' : 1.5, 'death' : 2}
    SPEED = {'idle' : 100, 'pattern1' : 200, 'pattern2' : 0, 'death' : 0}    

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
        
        self.is_shoot = [False, False]
        
        self.build_behavior_tree()

        self.shadow.opacify(0.4)
        pass
    
    def update(self):
        self.bt.run()
        
        if self.hp > 0:
            self.x += self.speed * math.cos(self.direction) * game_framework.frame_time
            self.y += self.speed * math.sin(self.direction) * game_framework.frame_time
            
        elif self.hp == 0:
            self.action = 'death'
            if self.frame >= self.FPA[self.action] - 1:
                self.hp = -1
                game_world.remove_object(self)
                
        self.frame = (self.frame + self.FPA[self.action] * 1.0 / self.TPA[self.action] * game_framework.frame_time) % self.FPA[self.action]
    
    def draw(self):
        self.shadow.draw(self.x, self.y - 64)
        self.image.clip_draw(self.CLIP[self.action][int(self.frame)][0], # Crop X
                            self.CLIP[self.action][int(self.frame)][1], # Crop Y
                            self.CLIP_SIZE, self.CLIP_SIZE, # Crop Width, Height
                            self.x + self.CLIP[self.action][int(self.frame)][4], # Position X 
                            self.y + self.CLIP[self.action][int(self.frame)][5], # Position Y
                            int(self.draw_width * self.CLIP[self.action][int(self.frame)][2]), # Scale X 
                            int(self.draw_height * self.CLIP[self.action][int(self.frame)][3])) # Scale Y
        
        if self.action == 'death':
            dead_effect_frame = int(self.frame % len(self.DEAD))
            self.dead_effect.clip_draw(self.DEAD[dead_effect_frame][0], self.DEAD[dead_effect_frame][1], 64, 64, self.x, self.y - 28, 160, 160)
        
        draw_rectangle(*self.get_bb())
        pass
    
    def handle_collision(self, other, group):
        if group == 'room:enemy':
            if other.type == 'wall' or other.type == 'door':
                self.direction = (self.direction + math.pi)
                return
        if group == 'enemy:tears':
            if self.hp > 0 and other.hp > 0:
                self.hp -= 1
                if self.hp == 0:
                    self.frame = 0
                    self.action = 'death'
                    self.speed = self.SPEED[self.action]
                    return
            
    
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
        if self.hp <= 0:
            return BehaviorTree.SUCCESS
        
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
        if self.hp <= 0:
            return BehaviorTree.SUCCESS
        
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
            self.shoot(12)
            
        return BehaviorTree.RUNNING
    
    # pattern 2
    def pattern2(self):
        if self.hp <= 0:
            return BehaviorTree.SUCCESS
        
        self.action = 'pattern2'
        self.speed = self.SPEED['pattern2']
        
        if self.frame >= self.FPA[self.action] - 1:
            self.frame = 0
            self.direction = random.random() * 2 * math.pi
            return BehaviorTree.SUCCESS
        
        if int(self.frame) == 19 and not self.is_shoot:
            self.is_shoot = True
            self.shoot(14, 300)
            self.shoot(8)

        return BehaviorTree.RUNNING
    
    def shoot(self, way, speed = 600):
        # print('shoot')
        tears = []
        step = 2 * math.pi / way
        for i in range(way):
            tears.append(Tear(self.x, self.y, self.direction + step * i, 1, speed))
        game_world.add_objects(tears, 4)
        game_world.add_collision_group(None, tears, 'player:bullet')
        game_world.add_collision_group(None, tears, 'room:tears')
        pass
