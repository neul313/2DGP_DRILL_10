from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (1.0 / 0.03)
RUN_SPEED_KMPH = 45.0 #참새의 평균 속도
#RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 3600.0)
RUN_SPEED_MPS = (RUN_SPEED_KMPH * 1000.0 / 3600.0)
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
        self.dir = 1 # 1: 오른쪽, -1: 왼쪽
        self.frame = 0
        self.animation_time = 0

    def draw(self):

        self.image.clip_draw(0, 0, 150, 150, self.x, self.y,80,80)


    def update(self):
        self.animation_time += game_framework.frame_time
        self.frame = int(self.animation_time * FRAMES_PER_ACTION * ACTION_PER_TIME) % FRAMES_PER_ACTION
        D = RUN_SPEED_PPS * game_framework.frame_time
        self.x += self.dir * D
        if self.x > 1600 - 80:
            flip = 'h'
            self.dir = -1
            self.image.clip_composite_draw(0, 0, 150, 150, 0, flip, self.x, self.y,80,80)
        elif self.x < 80:
            self.dir = 1
            self.image.clip_draw(0, 0, 150, 150, self.x, self.y,80,80)
