from heapq import heappush as insert
import constants
import my_time
from entities import QueryState
from handlers.handler import Handler
from entities.source import Source
from entities.queries import QueryT

from stats.stats_collector import stats_collector


class SourcesProcessor(Handler):
    def __init__(self, heap_que: list[QueryT], max_queries):
        self.sources: list[Source] = [Source(0.3) for _ in range(0, constants.N_SOURCES)]
        self.heap_que = heap_que
        self.MAX_N_QUERIES = max_queries
        self.total_gen_queries = 0
        self.next_step_handler = None

    def init(self):
        for pos, source in enumerate(self.sources):
            if self.total_gen_queries == self.MAX_N_QUERIES:
                return
            query = source.gen_query()
            stats_collector.add_query(pos)
            self.total_gen_queries += 1
            insert(self.heap_que,
                   QueryT(end_time=query.time + my_time.time,
                          n_source=pos,
                          n_query=query.n_query,
                          state=QueryState.FROM_SOURCE))

    def gen_new_query(self, n_source):
        q = self.sources[n_source].gen_query()
        print("new query, launched")
        new_query = QueryT(end_time=my_time.time + q.time,
                           n_source=n_source,
                           n_query=q.n_query,
                           state=QueryState.FROM_SOURCE)
        insert(self.heap_que, new_query)

    def handle(self, query: QueryT):  # handle query from heap
        if self.total_gen_queries == self.MAX_N_QUERIES:
            self.next_step_handler.handle(query)
        else:
            stats_collector.add_query(query.n_source)
            self.gen_new_query(query.n_source)
            self.total_gen_queries += 1
            self.next_step_handler.handle(query)
