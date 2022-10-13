import math
import random


class Instrument():
    def __init__(self, speed):
        self.speed = speed
        self.is_busy = False
        self.start_time = None
        self.end_time = None

    def release(self):
        self.is_busy = False

    def run(self, start_time):
        self.is_busy = True
        self.start_time = start_time
        self.end_time = -1 / self.speed * math.log(random.uniform(0, 1))
        return self.end_time
