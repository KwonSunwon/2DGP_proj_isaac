from pico2d import *
import game_framework
import game_world

from stage import Stage
from stage import Room
from player import Player

class StageManager:
    
    def __init__(self, player, ui):
        player = player
        ui = ui
        
        stage = Stage()
        
        stage.make_stage()
        
        