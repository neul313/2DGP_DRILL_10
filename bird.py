from pico2d import *
import game_world
import game_framework


class Bird:
    image = None

    def __init__(self, x = 100, y = 500):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, = x, y

    def draw(self):
        self.image.clip_draw(0, 0, 150, 150, self.x, self.y,100,100)

    def update(self):
        if self.x > 1600:
            game_world.remove_object(self)

