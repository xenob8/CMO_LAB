from collections import namedtuple

from observers.sources_processor import QueryT



class BufferPutDispatcher:
    def __init__(self, buffers: list[QueryT], max_size):
        self.buffers = buffers
        self.max_size = max_size

    def add(self, query: QueryT):
        if len(self.buffers) < self.max_size:
            self.buffers.append(query)
            return True
        else:
            return False