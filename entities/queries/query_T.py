# QueryT = namedtuple('Query', 'time n_source n_query')
from datetime import datetime


class QueryT():
    def __init__(self, end_time, n_source, n_query, state=None):
        self.end_time: datetime = end_time
        self.n_source = n_source
        self.n_query = n_query
        self.n_instr = None
        self.start_time: datetime = None
        self.state = state

    def __lt__(self, other):
        return self.end_time < other.end_time

    def __str__(self):
        return f'{self.state},time left:{(self.end_time-datetime.now())}, ({self.n_source, self.n_query})'
    #.strftime("%M %S")

    def __repr__(self):
        return self.__str__()
