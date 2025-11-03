from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.03)
RUN_SPEED_KMPH = 45.0 #참새의 평균 속도
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 3600.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:
    image = None

    def __init__(self, x = 100, y = 500):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, = x, y

    def draw(self):
        self.image.clip_draw(0, 0, 150, 150, self.x, self.y,80,80)


    def update(self):
        if self.x > 1600:
            game_world.remove_object(self)

