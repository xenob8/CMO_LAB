import constants
from handlers.handler import Handler
from stats import singleton
from utils.sources_processor import QueryT


class BufferPutDispatcher(Handler):
    def __init__(self, size):
        self.buffers: list[QueryT] = []
        self.max_size = size
        self.next_step_handler = None
        self.refused_query = None
        self.n_refused = 0

    def handle(self, query: QueryT):
        if self.add(query):
            self.next_step_handler.handle()
        else:
            self.refused_query = query
            self.n_refused += 1
            singleton.stats_collector.add_cancel(query.n_source)

    def add(self, query: QueryT):
        if len(self.buffers) < self.max_size:
            self.buffers.append(query)
            return True
        else:
            return False
