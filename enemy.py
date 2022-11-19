from pico2d import *
from creature import Creature

import math
import random

import game_framework
import game_world

import server

from behavior_tree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

FRONT, BACK, LEFT, RIGHT = 0, 1, 2, 3

class Enemy(Creature):
    dead_effect = None
    DEAD = ([0, 192], [64, 192], [128, 192], [192, 192],
            [0, 128], [64, 128], [128, 128], [192, 128],
            [0, 64], [64, 64], [128, 64], [192, 64])
    
    
    def __init__(self, x, y):
        if Enemy.dead_effect == None:
            Enemy.dead_effect = load_image('resources/effect/poof.png')
        
        self.x = x * 87 + 64
        self.y = (8 - y) * 85 + 48
        self.dir = 0
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass
    
    def handle_collision(self, other, group):
        if group == 'enemy:tears':
            if self.hp > 0 and other.hp > 0:
                self.hp -= 1
                if self.hp == 0:
                    self.frame = 0


class Fly(Enemy):
    type = 'fly'
    image = None
    
    live_pos = ([0, 192], [32, 192], [64, 192], [96, 192])
    die_pos = ([0, 128], [64,128], [128, 128], [192, 128],
               [0, 64], [64, 64], [128, 64], [192, 64],
               [0, 0], [64, 0], [128, 0], [192, 0])
    FPA_live = 4
    FPA_die = 12
    TPA_live = 0.2
    TPA_die = 0.7
    
    width = 32
    height = 32
    
    draw_width = 64
    draw_height = 64
    
    def __init__(self, x, y):
        if Fly.image == None:
            Fly.image = load_image('./resources/monsters/fly.png')
        super().__init__(x, y)
        self.hp = 2
        self.frame = 0
        self.speed = 100
        
        self.build_behavior_tree()
        pass

    def add_event(self, event):
        pass

    def update(self):
        # print(self.dir)
        self.bt.run()
        
        if self.hp > 0:
            self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
            self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
            
            self.frame = (self.frame + self.FPA_live * 1.0 / self.TPA_live * game_framework.frame_time) % self.FPA_live
            
        elif self.hp == 0:
            self.frame = (self.frame + self.FPA_die * 1.0 / self.TPA_die * game_framework.frame_time) % self.FPA_die
            if self.frame >= 11:
                self.hp = -1
                game_world.remove_object(self)
                        
        pass

    def draw(self):
        if self.hp > 0:
            self.image.clip_draw(self.live_pos[int(self.frame)][0], self.live_pos[int(self.frame)][1], 32, 32, self.x, self.y, self.draw_width, self.draw_height)
        elif self.hp == 0:
            self.image.clip_draw(self.die_pos[int(self.frame)][0], self.die_pos[int(self.frame)][1], 64, 64, self.x, self.y, self.draw_width, self.draw_height)
        
        draw_rectangle(*self.get_bb())

    def handle_collision(self, other, group):
        super().handle_collision(other, group)
    
    def move_to_player(self):
        # print("Fly_move")
        self.dir = math.atan2(server.player.y - self.y, server.player.x - self.x)
        return BehaviorTree.SUCCESS
    
    def build_behavior_tree(self):
        fly_move_node = LeafNode("FlyMove", self.move_to_player)
        
        fly_node = SequenceNode("Fly")
        fly_node.add_children(fly_move_node)
        
        self.bt = BehaviorTree(fly_node)
        pass
            

class Meat(Enemy):
    image = None
    
    MOVE = ([0, 128], [64, 128], [128, 128], [192, 128],
            [0, 64], [64, 64], [192, 64], 
            [0, 128], [64, 128], [0, 128], [0, 128])
    
    ATTACK = ([0, 128], [0, 0], [64, 64], [128, 64],
            [64, 64], [64, 0], [128, 0], [64, 128],
            [0, 0], [0, 128], [0, 128])
    
    FPA = 11
    TPA = 0.5
    
    width = 64
    height = 64
    
    draw_width = 160
    draw_height = 160
    
    def __init__(self, x, y):
        if Meat.image == None:
            Meat.image = load_image('./resources/monsters/meat.png')
        
        self.build_behavior_tree()
        
        super().__init__(x, y)
        self.dir = random.random() * 2 * math.pi
        self.move_speed = 100
        self.speed = 0
        self.frame = 0

        self.hp = 6
        
        self.action = 'idle'
        self.idle_timer = 1
        pass

    def add_event(self, event):
        pass

    def update(self):
        self.bt.run()
        
        if self.hp >= 0:
            self.frame = (self.frame + self.FPA * 1.0 / self.TPA * game_framework.frame_time) % self.FPA
            self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
            self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
            
        elif self.hp == 0:
            self.frame = (self.frame + 12 * 1.0 / 0.7 * game_framework.frame_time)
            if self.frame >= 11:
                self.hp = -1
                game_world.remove_object(self)
        pass

    def draw(self):
        if abs(self.dir) >= 1.5:
            look = 'h'
        else:
            look = ''

        # print(type(self.MOVE))        
        # print(int(self.frame))
        if self.hp >= 0:
            if self.action == 'idle':
                self.image.clip_composite_draw(0, 128, 64, 64, 0, look, self.x, self.y, self.draw_width, self.draw_height)
            elif self.action == 'move':
                self.image.clip_composite_draw(self.MOVE[int(self.frame)][0], self.MOVE[int(self.frame)][1], 64, 64, 0, look, self.x, self.y, self.draw_width, self.draw_height)
            elif self.action == 'attack':
                self.image.clip_composite_draw(self.ATTACK[int(self.frame)][0], self.ATTACK[int(self.frame)][1], 64, 64, 0, look, self.x, self.y, self.draw_width, self.draw_height)
            
        elif self.hp == 0:
            self.dead_effect.clip_draw(self.DEAD[int(self.frame)][0], self.DEAD[int(self.frame)][1], 64, 64, self.x, self.y, 96, 96)

        draw_rectangle(*self.get_bb())
        pass

    def wander(self):
        # print("Meat_wander")
        self.action = 'move'
        self.speed = self.move_speed
        
        if self.frame >= self.FPA - 1:
            self.frame = 0
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    
    def idle(self):
        # print("Meat_idle")
        self.action = 'idle'
        self.speed = 0
        
        self.idle_timer -= game_framework.frame_time
        if self.idle_timer <= 0:
            self.idle_timer = 1
            self.frame = 0
            self.dir = random.random() * 2 * math.pi
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    
    def attack(self):
        # print("Meat_attack")
        self.action = 'attack'
        self.speed = 0
        
        if self.frame >= self.FPA - 1:
            self.frame = 0
            self.idle_timer = 1
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    
    def find_player(self):
        # print("Meat_find_player")
        self.speed = 0
        if self.get_distance(server.player) < 200:
            self.dir = math.atan2(server.player.y - self.y, server.player.x - self.x)
            self.speed = self.move_speed
            self.frame = 0
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL
        
    def move_to_player(self):
        # print("Meat_move_to_player")
        self.action = 'move'
        
        if self.frame >= self.FPA - 1:
            self.frame = 0
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING

    def build_behavior_tree(self):
        # leaf
        meat_wander_node = LeafNode("MeatWander", self.wander)
        meat_idle_node = LeafNode("MeatIdle", self.idle)
        meat_attack_node = LeafNode("MeatAttack", self.attack)
        meat_find_player_node = LeafNode("MeatFindPlayer", self.find_player)
        meat_move_to_player_node = LeafNode("MeatMoveToPlayer", self.move_to_player)
        
        # sequence
        meat_patrol_node = SequenceNode("MeatPatrol")
        meat_patrol_node.add_children(meat_wander_node, meat_attack_node)
        
        meat_find_attack_node = SequenceNode("MeatFindAttack")
        meat_find_attack_node.add_children(meat_find_player_node, meat_move_to_player_node, meat_attack_node)
        
        # selector
        meat_action_node = SelectorNode("MeatAction")
        meat_action_node.add_children(meat_find_attack_node, meat_patrol_node)
        
        # root
        meat_node = SequenceNode("Meat")
        meat_node.add_children(meat_idle_node, meat_action_node)
        
        # init
        self.bt = BehaviorTree(meat_node)
        
    def get_distance(self, player):
        return math.sqrt((self.x - player.x) ** 2 + (self.y - player.y) ** 2)
    
    def get_bb(self):
        return self.x - 32, self.y - 48, self.x + 32, self.y + 16

class Charger(Enemy):
    type = 'charger'
    image = None
    
    FPA_live = 4
    TPA_live = 0.8
    
    width = 64
    height = 32
    
    draw_width = 96
    draw_height = 96
    
    def __init__(self, x, y):
        if Charger.image == None:
            self.image = load_image('./resources/monsters/charger.png')
        super().__init__(x,y)
        self.hp = 5
        self.frame = 0
        self.speed = 50
        self.wander_speed = 50
        self.rush_speed = 600
        self.dir = random.randint(0, 3)
        
        self.collision = False
        self.rush = False
        
        self.wander_timer = 2
        
        self.build_behavior_tree()
        pass

    def add_event(self, event):
        pass

    def update(self):
        self.bt.run()
        
        if self.hp > 0:
            if self.dir == FRONT:
                self.y -= self.speed * game_framework.frame_time
            elif self.dir == BACK:
                self.y += self.speed * game_framework.frame_time
            elif self.dir == LEFT:
                self.x -= self.speed * game_framework.frame_time
            elif self.dir == RIGHT:
                self.x += self.speed * game_framework.frame_time
            
            self.frame = (self.frame + self.FPA_live * 1.0 / self.TPA_live * game_framework.frame_time) % self.FPA_live

        elif self.hp == 0:
            self.frame = (self.frame + 12 * 1.0 / 0.7 * game_framework.frame_time)
            if self.frame >= 11:
                self.hp = -1
                game_world.remove_object(self)
        pass

    def draw(self):
        if self.hp > 0:
            if not self.rush:
                if self.dir == FRONT:
                    self.image.clip_draw(32 * int(self.frame), 32, 32, 32, self.x, self.y, self.draw_width, self.draw_height)
                elif self.dir == BACK:
                    self.image.clip_draw(32 * int(self.frame), 64, 32, 32, self.x, self.y, self.draw_width, self.draw_height)
                elif self.dir == LEFT:
                    self.image.clip_composite_draw(32 * int(self.frame), 96, 32, 32, 0, 'h', self.x, self.y, self.draw_width, self.draw_height)
                elif self.dir == RIGHT:
                    self.image.clip_draw(32 * int(self.frame), 96, 32, 32, self.x, self.y, self.draw_width, self.draw_height)
            elif self.rush:
                if self.dir == FRONT:
                    self.image.clip_draw(0, 0, 32, 32, self.x, self.y, self.draw_width, self.draw_height)
                elif self.dir == BACK:
                    self.image.clip_draw(64, 0, 32, 32, self.x, self.y, self.draw_width, self.draw_height)
                elif self.dir == LEFT:
                    self.image.clip_composite_draw(32, 0, 32, 32, 0, 'h', self.x, self.y, self.draw_width, self.draw_height)
                elif self.dir == RIGHT:
                    self.image.clip_draw(32, 0, 32, 32, self.x, self.y, self.draw_width, self.draw_height)
        elif self.hp == 0:
            self.dead_effect.clip_draw(self.DEAD[int(self.frame)][0], self.DEAD[int(self.frame)][1], 64, 64, self.x, self.y, 96, 96)
            
        draw_rectangle(*self.get_bb())
        pass

    def handle_event(self, event):
        pass
    
    def handle_collision(self, other, group):
        if group == 'room:enemy':
            # print("charger collision")
            self.collision = True
            self.speed = 0
            return
        return super().handle_collision(other, group)
    
    def wander(self):
        self.speed = self.wander_speed
        self.wander_timer -= game_framework.frame_time
        if self.collision:
            self.wander_timer = 2
            self.dir = random.randint(0, 3)
            self.collision = False
        if self.wander_timer <= 0:
            self.wander_timer = 2
            self.dir = random.randint(0, 3)
        return BehaviorTree.SUCCESS
    
    def find_player(self):
        if self.x - 32 <= server.player.x <= self.x + 32 and self.collision == False:
            self.dir = BACK if server.player.y > self.y else FRONT
            self.rush = True
            self.wander_timer = 0.5
            self.speed = 0
            return BehaviorTree.SUCCESS
        elif self.y - 32 <= server.player.y <= self.y + 32 and self.collision == False:
            self.dir = RIGHT if server.player.x > self.x else LEFT
            self.rush = True
            self.wander_timer = 0.5
            self.speed = 0
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL
    
    def rush_ready(self):
        self.wander_timer -= game_framework.frame_time
        if self.wander_timer <= 0:
            self.speed = self.rush_speed
            return BehaviorTree.SUCCESS
        return BehaviorTree.RUNNING
    
    def rush_to_player(self):
        if self.collision:
            if self.dir == FRONT:
                self.dir = BACK
            elif self.dir == BACK:
                self.dir = FRONT
            elif self.dir == LEFT:
                self.dir = RIGHT
            elif self.dir == RIGHT:
                self.dir = LEFT
                
            self.speed = self.wander_speed
            self.wander_timer = 2
            self.rush = False
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
    
    def build_behavior_tree(self):
        charger_wander_node = LeafNode("ChargerWander", self.wander)
        
        charger_find_player = LeafNode("ChargerFindPlayer", self.find_player)
        charger_rush_ready_node = LeafNode("ChargerRushReady", self.rush_ready)
        charger_rush_node = LeafNode("ChargerRush", self.rush_to_player)
        charger_attack_node = SequenceNode("ChargerAttack")
        charger_attack_node.add_children(charger_find_player, charger_rush_ready_node, charger_rush_node)

        charger_node = SelectorNode("Charger")
        charger_node.add_children(charger_attack_node, charger_wander_node)
        
        self.bt = BehaviorTree(charger_node)


