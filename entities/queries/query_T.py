# QueryT = namedtuple('Query', 'time n_source n_query')
from datetime import datetime


class QueryT():
    def __init__(self, time, n_source, n_query):
        self.time:datetime = time
        self.n_source = n_source
        self.n_query = n_query

    def __lt__(self, other):
        return self.time < other.time

    def __str__(self):
        return f'{self.time.strftime("%M %S")}, ({self.n_source, self.n_query})'

    def __repr__(self):
        return f'{self.time.strftime("%M %S")}, ({self.n_source, self.n_query})'