from heapq import heappush

import my_time
from entities import QueryState
from entities.instrument import Instrument
from handlers.handler import Handler
from stats import stats_collector
from utils.sources_processor import QueryT


class LoadInstrumentDispatcher(Handler):
    def __init__(self, instruments: list[Instrument], heap_queries):
        self.instruments = instruments
        self.heap_queries = heap_queries

    def handle(self, query: QueryT):
        self.push_instrument(query)
        query.state = QueryState.FROM_INSTRUMENT

    def push_instrument(self, query: QueryT):
        free_instr, n_instr = self.__find_free_instrument()
        end_time = free_instr.run(query)
        query.n_instr = n_instr
        query.end_time = my_time.time + end_time
        stats_collector.add_time_in_instr(query.n_source, query.end_time - my_time.time)
        stats_collector.add_instrument_time(query.n_instr, query.end_time - my_time.time)
        # print(f"INSTRUMENT END TIME: {query.n_instr}, {query.end_time}")
        # print(f"INSTRUMENT START TIME: {query.n_instr}, {query.start_time}")
        # print(f"INSTRUMENT TIME: {query.n_instr}, {query.end_time - query.start_time}")
        # print("Current time:",my_time.time)
        # todo надо брать разницу не с началом генерации сигнала, а с текущим временем,
        # некоторое время он лежал в буфере
        heappush(self.heap_queries, query)

    def __find_free_instrument(self) -> (Instrument, int):
        for i, instr in enumerate(self.instruments):
            if not instr.is_busy:
                return instr, i
