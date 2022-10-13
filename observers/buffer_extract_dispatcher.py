from copy import copy
from functools import reduce

import constants
from observers.sources_processor import QueryT



class BufferExtractDispatcher():
    def __init__(self, buffers: list[QueryT], instruments_heap: list[QueryT]):
        self.buffers = buffers
        self.instruments_heap = instruments_heap

    def get_query(self):
        if self.__is_avaliable_instrument() and self.buffers:
            q = self.__find_min_by_source()
            if q: # todo get out if
                self.buffers.remove(q)
                return copy(q)
        return None


    def __find_min_by_source(self):
        def comparator(a: QueryT, b: QueryT):
            if b.n_source < a.n_source:
                return b
            if b.n_source == a.n_source and b.n_query < a.n_query:
                return b
            return a

        return reduce(comparator, self.buffers)

    def __is_avaliable_instrument(self):
        return len(self.instruments_heap) < constants.N_INSTUMENTS