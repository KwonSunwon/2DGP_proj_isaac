import pico2d
import game_framework
import game_world

class Static:
    x, y = 0, 0
    WIDTH, HEIGHT = 96, 96
    
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

    def get_bb(self):
        return self.x - self.WIDTH // 2, self.y - self.HEIGHT // 2, self.x + self.WIDTH // 2, self.y + self.HEIGHT // 2
    
    def handle_collision(self, other, group):
        pass
    

class Wall(Static):
    pass

class Rock(Static):
    image = None
    
    def __init__(self):
        if Rock.image == None:
            Rock.image = pico2d.load_image('resource\\image\\rock.png')
        
    pass


class Spike(Static):
    image = None
    
    def __init__(self):
        if Spike.image == None:
            Spike.image = pico2d.load_image('resource\\image\\spike.png')
    pass


class Poop(Static):
    image = None
    
    def __init__(self):
        if Poop.image == None:
            Poop.image = pico2d.load_image('resource\\image\\spike.png')
    pass


class Door(Static):
    image = None
    
    
    def __init__(self):
        if Door.image == None:
            Door.image = pico2d.load_image('resource\\image\\spike.png')
    pass


class Pit(Static):
    image = None
    
    def __init__(self):
        if Pit.image == None:
            Pit.image = pico2d.load_image('resource\\image\\spike.png')
    pass