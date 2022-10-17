from copy import copy
from functools import reduce

from handlers.handler import Handler
from entities.instrument import Instrument
from utils.sources_processor import QueryT


class BufferExtractDispatcher(Handler):
    def __init__(self, buffers: list[QueryT], instruments: list[Instrument], heap_que: list[QueryT]):
        self.buffers = buffers
        self.instruments = instruments
        self.next_step_handler = None
        self.heap_que = heap_que
        self.priority_packet = None

    def get_query(self):
        if not self.buffers:
            self.priority_packet = None
            return

        if self.__is_avaliable_instrument():
            print("is aval instr? True")
            print("Instruments", [i.is_busy for i in self.instruments])
            q = self.__find_query_by_packet(self.priority_packet) or self.__find_min_by_source_n()
            self.priority_packet = q.n_source
            self.buffers.remove(q)
            print("FROM BUFEER EXTRACTED")
            print(q)
            return copy(q)


    def __find_query_by_packet(self, priority_packet):
        if priority_packet:
            return self.__find_next_query_by_packet(priority_packet)

    def handle(self):
        query = self.get_query()
        if query:
            self.next_step_handler.handle(query)


    def __find_min_by_source_n(self):
        def comparator(a: QueryT, b: QueryT):
            if b.n_source < a.n_source:
                return b
            if b.n_source == a.n_source and b.n_query < a.n_query:
                return b
            return a

        return reduce(comparator, self.buffers)


    def __is_avaliable_instrument(self):
        return any(instr.is_busy==False for instr in self.instruments)

    def __find_next_query_by_packet(self, n_source):
        return min((query for query in self.buffers if query.n_source == n_source),
                   key=lambda q: q.n_query,
                   default=None)
