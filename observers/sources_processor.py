from collections import namedtuple
from datetime import datetime, timedelta
from heapq import heappop as extractNext, heappush as insert

from source import Source
from entities.queries import QueryT
# QueryT = namedtuple('Query', 'time n_source n_query')


class SourcesProcessor():
    def __init__(self, sources: list[Source], que: list[QueryT]):
        self.sources = sources
        self.que = que

    def gather_queries(self):
        for pos, source in enumerate(self.sources):
            query = source.gen_query()
            insert(self.que,
                   QueryT(time=datetime.now() + timedelta(seconds=query.time), n_source=pos, n_query=query.n_query))

    def gen_new_query(self, n_source):
        q = self.sources[n_source].gen_query()
        print("new query, launched")
        new_query = QueryT(time=datetime.now() + timedelta(seconds=q.time), n_source=n_source, n_query=q.n_query)
        insert(self.que, new_query)