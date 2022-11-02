from pico2d import *
from creature import Creature


class Enemy(Creature):
    def __init__(self):

        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass


class Fly(Enemy):
    image = None
    
    def __init__(self):
        if Fly.image == None:
            self.image = load_image('./resources/monsters/fly.png')
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass
    

class Meat(Enemy):
    image = None
    
    def __init__(self):
        if Meat.image == None:
            self.image = load_image('./resources/monsters/meat.png')
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass
    

class Charger(Enemy):
    image = None
    
    def __init__(self):
        if Charger.image == None:
            self.image = load_image('./resources/monsters/charger.png')
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass