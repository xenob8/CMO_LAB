from copy import copy
from functools import reduce

from handlers.handler import Handler
from utils import Event
from entities.instrument import Instrument
from utils.sources_processor import QueryT


class BufferExtractDispatcher(Handler):
    def __init__(self, buffers: list[QueryT], instruments: list[Instrument], heap_que: list[QueryT]):
        self.buffers = buffers
        self.instruments = instruments
        self.next_step_handler = None
        self.heap_que = heap_que

    def get_query(self):
        if self.__is_avaliable_instrument() and self.buffers:
            q = self.__find_query_by_packet() or self.__find_min_by_source_n()
            if q:  # todo get out if
                self.buffers.remove(q)
                print("FROM BUFEER EXTRACTED")
                print(q)
                return copy(q)
        return None

    def __find_query_by_packet(self):
        query = self.__find_last_query_in_instruments()
        if query:
            return self.__find_next_query_by_packet(query.n_source)

    def handle(self):
        query = self.get_query()
        if query:
            query.state = Event.READY_TO_SERVICE
            self.next_step_handler.handle(query)

    def __get_last_launched_instrument(self) -> Instrument:
        return max(self.instruments, key=lambda instr: instr.start_time, default=None)

    def __find_min_by_source_n(self):
        def comparator(a: QueryT, b: QueryT):
            if b.n_source < a.n_source:
                return b
            if b.n_source == a.n_source and b.n_query < a.n_query:
                return b
            return a

        return reduce(comparator, self.buffers)

    def __find_last_query_in_instruments(self) -> QueryT:
        return min((query for query in self.heap_que if query.state == Event.IN_INSTRUMENT),
                   key=lambda q: q.start_time,
                   default=None)

    def __is_avaliable_instrument(self):
        return any(not instr.is_busy for instr in self.instruments)

    def __find_next_query_by_packet(self, n_source):
        return min((query for query in self.buffers if query.n_source == n_source),
                   key=lambda q: q.n_query,
                   default=None)
