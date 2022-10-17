import math
import random


class Instrument():
    def __init__(self, speed):
        self.speed = speed
        self.is_busy = False

    def release(self):
        self.is_busy = False

    def run(self):
        self.is_busy = True
        return -1 / self.speed * math.log(random.uniform(0, 1))

