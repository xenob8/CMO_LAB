import math
import random
from collections import namedtuple

Query = namedtuple("Query", "time, n_query")


class Source():
    def __init__(self, speed):
        self.speed = speed
        self.n_query = 0

    def gen_query(self) -> Query:
        self.n_query += 1
        return Query(time=-1 / self.speed * math.log(random.uniform(0, 1)), n_query=self.n_query)
