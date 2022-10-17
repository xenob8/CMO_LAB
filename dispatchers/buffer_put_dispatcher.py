from collections import namedtuple

from handlers.handler import Handler
from utils import Event
from utils.sources_processor import QueryT



class BufferPutDispatcher(Handler):
    def __init__(self, buffers: list[QueryT], max_size):
        self.buffers = buffers
        self.max_size = max_size
        self.next_step_handler = None
        self.refused_query = None

    def handle(self, query: QueryT):
        self.refused_query = None
        if query.state == Event.READY_SOURCE:
            if self.add(query):
                query.state = Event.IN_BUFFER
                self.next_step_handler.handle()
            else:
                query.state = Event.CANCELED
                self.refused_query = query

    def add(self, query: QueryT):
        if len(self.buffers) < self.max_size:
            self.buffers.append(query)
            return True
        else:
            return False