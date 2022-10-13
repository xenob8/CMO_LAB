import math
import random

from source import Query


class Instrument():
    def __init__(self, speed):
        self.speed = speed
        self.is_busy = False
        self.end_time = None

    def run(self) :
        self.is_busy = True
        return -1 / self.speed * math.log(random.uniform(0, 1))