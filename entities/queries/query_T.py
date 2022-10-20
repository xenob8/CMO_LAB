# QueryT = namedtuple('Query', 'time n_source n_query')
from datetime import datetime

import my_time


class QueryT():
    def __init__(self, end_time, n_source, n_query, state=None):
        self.end_time = end_time
        self.n_source = n_source
        self.n_query = n_query
        self.n_instr = None
        self.state = state

    def __lt__(self, other):
        return self.end_time < other.end_time

    def __str__(self):
        return f'{self.state},time left:{self.end_time - my_time.time}, ({self.n_source, self.n_query}, end time: {self.end_time})'
    #.strftime("%M %S")

    def __repr__(self):
        return self.__str__()

    def point_to_str(self):
        return f'({self.n_source}, {self.n_query})'