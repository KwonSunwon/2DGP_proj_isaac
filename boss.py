from pico2d import *

from enemy import Enemy
from tears import Tear

import game_framework
import game_world

import server

from behavior_tree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

import random
import math

Headless_image = None

class Head(Enemy):
    image = None
    
    IDLE_HEAD = ([0, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1],
            [0, 208, 0, 2, 1, 1], [0, 208, 0, 1, 1.03, 0.97], [0, 208, 0, 1, 1.03, 0.97], [0, 208, 0, 1, 1.03, 0.97], [0, 208, 0, 1, 1.03, 0.97],
            [0, 208, 0, 1, 1.03, 0.97], [0, 208, 0, 1, 1.03, 0.97], [0, 208, 0, 0, 0.95, 1.05], [0, 208, 0, 0, 0.95, 1.05], [0, 208, 0, 0, 0.95, 1.05],
            [0, 208, 0, 0, 0.95, 1.05], [0, 208, 0, 0, 0.95, 1.05], [0, 208, 0, 0, 0.95, 1.05], [0, 208, 0, 1, 0.96, 1.04], [0, 208, 0, 1, 0.96, 1.04],
            [0, 208, 0, 1, 0.96, 1.04], [0, 208, 0, 1, 0.96, 1.04], [0, 208, 0, 1, 0.96, 1.04], [0, 208, 0, 1, 0.96, 1.04], [0, 208, 0, 2, 1, 1],
            [0, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1])
    CHARGE_READY = ([0, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1], [48, 208, 0, 2, 1, 1], [48, 208, 0, 2, 1, 1], [128, 96, 0, -2, 1, 1],
                [128, 96, 0, -2, 1, 1], [0, 96, -2, 0, 1.2, 0.8], [0, 96, -2, 0, 1.2, 0.8], [0, 96, 0, 2, 1, 1], [0, 96, 0, 2, 1, 1],
                [0, 96, 0, 2, 1, 1], [0, 96, 0, 2, 1, 1], [0, 96, 0, 2, 1, 1], [0, 96, 0, 2, 1, 1], [0, 96, 0, 2, 1, 1],
                [0, 96, 0, 2, 1, 1], [0, 96, 0, 2, 1, 1], [128, 96, -8, 0, 1, 1], [128, 96, -8, 0, 1, 1], [0, 96, -14, 6, 0.7, 1.3],
                [0, 96, -14, 6, 0.7, 1.3], [48, 96, -16, 2, 1, 1], [48, 96, -16, 2, 1, 1])
    CHARGE_SHAKE = ([0, 96, 0, 2, 1, 1], [0, 96, 0, 2, 1, 1], [0, 96, 0, 4, 1, 1], [0, 96, 0, 4, 1, 1])
    ATTACK_HEAD = ([0, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1], [48, 208, 0, 4, 1, 1], [48, 208, 0, 4, 1, 1], [96, 208, 0, -2, 1, 1],
                [96, 208, 0, -2, 1, 1], [48, 208, 0, -6, 1, 1], [48, 208, 0, -6, 1, 1], [0, 208, 0, -4, 1, 1], [0, 208, 0, -4, 1, 1],
                [0, 208, 0, -4, 1, 1], [0, 208, 0, -4, 1, 1], [96, 160, 0, 0, 1, 1], [96, 160, 0, 0, 1, 1], [48, 160, 0, 10, 1, 1],
                [48, 160, 0, 10, 1, 1], [0, 160, -2, 6, 1.05, 0.95], [0, 160, -2, 6, 0.95, 1.05], [0, 160, -2, 6, 1.05, 0.95], [0, 160, -2, 6, 0.95, 1.05],
                [0, 160, -2, 6, 1.05, 0.95], [0, 160, -2, 6, 0.95, 1.05], [0, 160, -2, 6, 1.05, 0.95], [0, 160, -2, 6, 0.95, 1.05], [0, 160, -2, 6, 1.05, 0.95],
                [0, 160, -2, 6, 0.95, 1.05], [0, 160, -2, 6, 1.05, 0.95], [0, 160, 0, 6, 1, 1], [0, 160, 0, 6, 1, 1], [48, 208, 0, 7, 1.1, 0.8],
                [48, 208, 0, 7, 1.1, 0.8], [96, 208, 0, 2, 1, 1], [96, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1],
                [0, 208, 0, 2, 1, 1], [0, 208, 0, 2, 1, 1])
    HEAD_CLIP = {'idle': IDLE_HEAD, 'charge_ready': CHARGE_READY, 'charge_shake': CHARGE_SHAKE, 'attack': ATTACK_HEAD}
    HEAD_FPA = {'idle': len(IDLE_HEAD), 'charge_ready': len(CHARGE_READY), 'charge_shake': len(CHARGE_SHAKE), 'attack': len(ATTACK_HEAD)}
    HEAD_TPA = {'idle': 0.5, 'charge_ready': 1, 'charge_shake': 0.5, 'attack': 2}
    
    SPEED = {'idle': 30, 'charge_ready': 0, 'charge_shake': 700, 'attack': 0}
    
    width = 192
    height = 192
    
    CLIP_SIZE = 48
    
    def __init__(self, x, y):
        global Headless_image
        if Headless_image == None:
            Headless_image = load_image('resources/monsters/headlesshorseman.png')
            Head.image = Headless_image
        super().__init__(x, y)
        
        self.hp = 1
        self.speed = Head.SPEED['idle']
        self.direction = random.random() * 2 * math.pi
        self.action = 'idle'
        self.frame = 0
        
        self.charge_start = 0
        
        self.wander_timer = 2
        
        self.build_behavior_tree()
        
        self.shadow_opacify = 0.4
        
    def update(self):
        self.bt.run()
        self.frame = (self.frame + Head.HEAD_FPA[self.action] * 1.0 / Head.HEAD_TPA[self.action] * game_framework.frame_time) % Head.HEAD_FPA[self.action]
        
        if self.hp > 0:
            self.x += self.speed * math.cos(self.direction) * game_framework.frame_time
            self.y += self.speed * math.sin(self.direction) * game_framework.frame_time
        elif self.hp == 0:
            if self.frame == 0:
                Enemy.dead_sfx.set_volume(5)
                Enemy.dead_sfx.play()
            self.frame = (self.frame + 12 * 1.0 / 0.7 * game_framework.frame_time)
            if self.frame >= 11:
                self.hp = -1
                game_world.remove_object(self)
    
    def draw(self):
        if self.hp > 0:
            Enemy.shadow.opacify(self.shadow_opacify)
            Enemy.shadow.draw(self.x, self.y - 20)
            self.image.clip_draw(Head.HEAD_CLIP[self.action][int(self.frame)][0],
                                Head.HEAD_CLIP[self.action][int(self.frame)][1],
                                Head.CLIP_SIZE, Head.CLIP_SIZE,
                                self.x + Head.HEAD_CLIP[self.action][int(self.frame)][2],
                                self.y + Head.HEAD_CLIP[self.action][int(self.frame)][3],
                                int(Head.width * Head.HEAD_CLIP[self.action][int(self.frame)][4]),
                                int(Head.height * Head.HEAD_CLIP[self.action][int(self.frame)][5]))
        elif self.hp == 0:
            self.dead_effect.clip_draw(self.DEAD[int(self.frame)][0], self.DEAD[int(self.frame)][1], 64, 64, self.x, self.y, 196, 196)
        
    def handle_collision(self, other, group):
        if group == 'enemy:tears':
            if self.hp > 0 and other.hp > 0:
                self.hp -= 1
                if self.hp == 0:
                    self.frame = 0
                    self.speed = self.SPEED[self.action]
                    return
    
    def build_behavior_tree(self):
        wander = LeafNode("Wander", self.wander)
        charge_ready = LeafNode("ChargeReady", self.charge_ready)
        charge = LeafNode("Charge", self.charge)
        attack = LeafNode("Attack", self.attack)
        
        headless_head = SequenceNode("Head")
        headless_head.add_children(wander, charge_ready, charge, attack)
        
        self.bt = BehaviorTree(headless_head)

    def wander(self):
        self.action = 'idle'
        self.speed = Head.SPEED['idle']
        self.wander_timer -= game_framework.frame_time
        self.direction = 0
        if self.wander_timer <= 0:
            self.wander_timer = 2
            self.frame = 0
            self.charge_start = self.x
            self.direction = 0
            self.speed = Head.SPEED['charge_ready']
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    
    def charge_ready(self):
        self.action = 'charge_ready'
        if self.frame >= Head.HEAD_FPA['charge_ready'] - 1:
            self.action = 'charge_shake'
            self.speed = Head.SPEED['charge_shake']
            self.frame = 0
            self.screen_out = False
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    
    def charge(self):
        self.action = 'charge_shake'
        if self.x >= 1540:
            self.x = -100
            self.screen_out = True
        elif self.x <= -100:
            self.x = 1540
            self.screen_out = True
            
        if abs(self.x - self.charge_start) < 100 and self.screen_out == True:
            self.speed = Head.SPEED['attack']
            self.frame = 0
            self.is_shoot = [False, False, False]
            return BehaviorTree.SUCCESS
        
        return BehaviorTree.RUNNING
    
    def attack(self):
        self.action = 'attack'
        if self.frame >= Head.HEAD_FPA['attack'] - 1:
            self.action = 'idle'
            self.speed = Head.SPEED['idle']
            self.frame = 0
            return BehaviorTree.SUCCESS
        
        if int(self.frame) == 20 and self.is_shoot[0] == False:
            self.shoot()
            self.is_shoot[0] = True
        if int(self.frame) == 25 and self.is_shoot[1] == False:
            self.shoot()
            self.is_shoot[1] = True
        if int(self.frame) == 30 and self.is_shoot[2] == False:
            self.shoot()
            self.is_shoot[2] = True
            
        return BehaviorTree.RUNNING

    def shoot(self):
        tears = []
        direction = math.atan2(server.player.y - self.y, server.player.x - self.x)
        for i in [-1, 0, 1]:
            tears.append(Tear(self.x, self.y, direction + i * 0.1, 1, 400))
        game_world.add_objects(tears, 4)
        game_world.add_collision_group(None, tears, 'player:bullet')
        game_world.add_collision_group(None, tears, 'room:tears')

class Body(Enemy):
    image = None
    
    IDLE_BODY = ([0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1],
                [0, 48, 0, 0, 1, 1], [0, 48, 0, -1, 1, 1], [0, 48, 0, -1, 1, 1], [0, 48, 0, -1, 1, 1], [0, 48, 0, -1, 1, 1],
                [0, 48, 0, -1, 1, 1], [0, 48, 0, -1, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1],
                [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 6, 1, 1], [0, 48, 0, -1, 1, 1], [0, 48, 0, -1, 1, 1],
                [0, 48, 0, -1, 1, 1], [0, 48, 0, -1, 1, 1], [0, 48, 0, -1, 1, 1], [0, 48, 0, -1, 1, 1], [0, 48, 0, 0, 1, 1],
                [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1])
    ATTACK_BODY = ([0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [80, 48, 0, 0, 1, 1], [80, 48, 0, 0, 1, 1], [80, 48, -8, 8, 1.1, 0.8],
                [80, 48, -8, 8, 1.1, 0.8], [80, 48, -8, 15, 1.2, 0.7], [80, 48, -8, 15, 1.2, 0.7], [160, 48, 18, -9, 0.9, 1.2], [160, 48, 18, -9, 0.9, 1.2],
                [160, 48, 16, -8, 0.95, 1.1], [160, 48, 16, -8, 0.95, 1.1], [0, 48, -5, 8, 1.1, 0.8], [0, 48, -5, 8, 1.1, 0.8], [0, 48, 0, 0, 1, 1.1],
                [0, 48, 0, 0, 1, 1.1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1],
                [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1],
                [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1], [0, 48, 0, 0, 1, 1])
    BODY_CLIP = {'idle': IDLE_BODY, 'attack': ATTACK_BODY}
    BODY_FPA = {'idle': len(IDLE_BODY), 'attack': len(ATTACK_BODY)}
    BODY_TPA = {'idle': 1, 'attack': 1}
    
    SPEED = {'idle': 80, 'attack': 0}
    
    width = 160
    height = 96
    
    CLIP_SIZE = (80, 48)
    
    def __init__(self, x, y):
        global Headless_image
        if Headless_image == None:
            Headless_image = load_image('resources/monsters/headlesshorseman.png')
            Body.image = Headless_image
        super().__init__(x, y)
        
        self.hp = 1
        self.speed = Body.SPEED['idle']
        self.direction = random.random() * 2 * math.pi
        self.action = 'idle'
        self.frame = 0
        
        self.build_behavior_tree()
        self.wander_timer = 2
        
        self.shadow_opacify = 0.4
        
    def update(self):
        self.bt.run()
        self.frame = (self.frame + Body.BODY_FPA[self.action] * 1.0 / Body.BODY_TPA[self.action] * game_framework.frame_time) % Body.BODY_FPA[self.action]

        if self.hp > 0:
            self.x += self.speed * math.cos(self.direction) * game_framework.frame_time
            self.y += self.speed * math.sin(self.direction) * game_framework.frame_time
        elif self.hp == 0:
            if self.frame == 0:
                Enemy.dead_sfx.set_volume(5)
                Enemy.dead_sfx.play()
            self.frame = (self.frame + 12 * 1.0 / 0.7 * game_framework.frame_time)
            if self.frame >= 11:
                self.hp = -1
                game_world.remove_object(self)
    
    def draw(self):
        if self.hp > 0:
            Enemy.shadow.opacify(self.shadow_opacify)
            Enemy.shadow.draw(self.x, self.y - 20)
            self.image.clip_draw(Body.BODY_CLIP[self.action][int(self.frame)][0],
                                Body.BODY_CLIP[self.action][int(self.frame)][1],
                                Body.CLIP_SIZE[0], Body.CLIP_SIZE[1],
                                self.x + Body.BODY_CLIP[self.action][int(self.frame)][2],
                                self.y + Body.BODY_CLIP[self.action][int(self.frame)][3],
                                int(Body.width * Body.BODY_CLIP[self.action][int(self.frame)][4]),
                                int(Body.height * Body.BODY_CLIP[self.action][int(self.frame)][5]))
        elif self.hp == 0:
            self.dead_effect.clip_draw(self.DEAD[int(self.frame)][0], self.DEAD[int(self.frame)][1], 64, 64, self.x, self.y, 196, 196)
        
        
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
                    self.speed = self.SPEED[self.action]
                    return
    
    def build_behavior_tree(self):
        wander_node = LeafNode("Wander", self.wander)
        attack_node = LeafNode("Attack", self.attack)
        
        Headless = SequenceNode("Headless")
        Headless.add_children(wander_node, attack_node)
    
        self.bt = BehaviorTree(Headless)
        
    def wander(self):
        self.action = 'idle'
        self.speed = Body.SPEED['idle']
        self.direction = random.random() * 2 * math.pi
        self.wander_timer -= game_framework.frame_time
        if self.wander_timer <= 0:
            self.wander_timer = random.randint(2, 5)
            self.frame = 0
            self.is_shoot = False
            self.speed = Body.SPEED['attack']
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    
    def attack(self):
        self.action = 'attack'
        if self.frame >= Body.BODY_FPA['attack'] - 1:
            self.action = 'idle'
            self.speed = Body.SPEED['idle']
            self.frame = 0
            return BehaviorTree.SUCCESS
        
        if int(self.frame) == 10 and self.is_shoot == False:
            self.shoot()
            self.is_shoot = True
            
        return BehaviorTree.RUNNING

    def shoot(self):
        tears = []
        step = 2 * math.pi / 8
        for i in range(8):
            tears.append(Tear(self.x, self.y, self.direction + step * i, 1, 350))
        game_world.add_objects(tears, 4)
        game_world.add_collision_group(None, tears, 'player:bullet')
        game_world.add_collision_group(None, tears, 'room:tears')

    
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

        self.shadow_opacify = 0.4
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
        self.shadow.opacify(self.shadow_opacify)
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
