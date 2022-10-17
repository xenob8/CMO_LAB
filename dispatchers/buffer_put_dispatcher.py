from collections import namedtuple

from handlers.handler import Handler
from utils.sources_processor import QueryT



class BufferPutDispatcher(Handler):
    def __init__(self, buffers: list[QueryT], max_size):
        self.buffers = buffers
        self.max_size = max_size
        self.next_step_handler = None
        self.refused_query = None

    def handle(self, query: QueryT):
        if self.add(query):
            self.next_step_handler.handle()
        else:
            self.refused_query = query

    def add(self, query: QueryT):
        if len(self.buffers) < self.max_size:
            self.buffers.append(query)
            return True
        else:
            return False