from pico2d import *


class Character:
    image = None

    def __init__(self):
        if Character.image == None:
            self.image = load_image('./resource/character.png')
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def handle_event(self, event):
        pass
