from pico2d import *

import character
# import stage


### test code ##############################
heart = {'max': 6, 'cur': 3}
keyCount = 3
START_ROOM = 0b00000001
stage = [[None] * 10 for i in range(10)]
stage[4][4] = START_ROOM
############################################


width = 1440
height = 816


class UI:
    hearts = None
    minimap = None
    minimapIcons = None
    key = None
    
    def __init__(self):
        if (UI.hearts == None):
            self.hearts = load_image('./resources/ui/hearts.png')
        if (UI.minimap == None):
            self.minimap = load_image('./resources/ui/minimap.png')
        if (UI.minimapIcons == None):
            self.minimapIcons = load_image('./resources/ui/minimap_icons.png')
        if (UI.key == None):
            self.key = load_image('./resources/ui/key.png')
        
        self.heartState = heart # get heart information from character class
        self.keyState = keyCount # get key information from character class
        self.stage = stage # get stage information from stage class
        
    def add_event(self, event):
        pass
    
    def update(self):
        pass
    
    def draw_hearts(self):
        full = self.heartState['cur'] // 2
        half = self.heartState['cur'] % 2
        empty = self.heartState['max'] // 2 - full - half
        pos = 0
        for i in range(full):
            self.hearts.clip_composite_draw(0, 48, 16, 16, 0, '', 50 + pos * 32, height - 50, 32, 32)
            pos += 1
        for i in range(half):
            self.hearts.clip_composite_draw(16, 48, 16, 16, 0, '', 50 + pos * 32, height - 50, 32, 32)
            pos += 1
        for i in range(empty):
            self.hearts.clip_composite_draw(32, 48, 16, 16, 0, '', 50 + pos * 32, height - 50, 32, 32)
            pos += 1
    
    def draw_minimap(self):
        
        pass
    
    def draw_key(self):
        pass
    
    def draw(self):
        self.draw_hearts()
        self.draw_minimap()
        self.draw_key()
        pass
        
    def handle_event(self, event):
        pass