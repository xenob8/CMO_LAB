import math
import random

from entities import QueryT


class Instrument():
    def __init__(self, speed):
        self.speed = speed
        self.is_busy = False
        self.query = None

    def release(self):
        self.is_busy = False

    def run(self, query: QueryT):
        self.is_busy = True
        self.query = query
        return -1 / self.speed * math.log(random.uniform(0, 1))
