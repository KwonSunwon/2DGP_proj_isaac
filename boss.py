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
    
    def __init__(self, x, y):
        if BabyPlum.image == None:
            BabyPlum.image = load_image('resources/monsters/babyplum.png')
        super().__init__(x, y)
        
        self.frame = 0
        self.hp = 20
        self.speed = 100
        
        self.next_pattern = random.randint(0, 3)
        
        self.build_behavior_tree()
        pass
    
    def update(self):
        self.bt.run()
        
        pass
    
    def draw(self):
        
        draw_rectangle(*self.get_bb())
        pass
    
    def handle_collision(self, other, group):
        return super().handle_collision(other, group)
    
    def build_behavior_tree(self):

        self.bt = BehaviorTree(self.root_node())
        pass
    
    # behavior
    def wander(self):
        pass
    
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
    
    