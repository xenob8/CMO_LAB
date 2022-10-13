from datetime import datetime, timedelta
from heapq import heappush as insert

from handlers.handler import Handler
from utils import Event
from entities.source import Source
from entities.queries import QueryT


class SourcesProcessor(Handler):
    def __init__(self, sources: list[Source], heap_que: list[QueryT]):
        self.sources = sources
        self.heap_que = heap_que
        self.next_step_handler = None


    def gather_queries(self):
        for pos, source in enumerate(self.sources):
            query = source.gen_query()
            insert(self.heap_que,
                   QueryT(end_time=datetime.now() + timedelta(seconds=query.time),
                          n_source=pos,
                          n_query=query.n_query,
                          state=Event.WAITING_SOURCE))

    def gen_new_query(self, n_source):
        q = self.sources[n_source].gen_query()
        print("new query, launched")
        new_query = QueryT(end_time=datetime.now() + timedelta(seconds=q.time),
                           n_source=n_source,
                           n_query=q.n_query,
                           state=Event.WAITING_SOURCE)
        insert(self.heap_que, new_query)

    def handle(self, query: QueryT):
        if query.state == Event.WAITING_SOURCE:
            self.gen_new_query(query.n_source)
            query.state = Event.READY_SOURCE
            self.next_step_handler.handle(query)