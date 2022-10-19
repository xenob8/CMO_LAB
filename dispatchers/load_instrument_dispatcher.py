from datetime import datetime, timedelta
from heapq import heappush

import my_time
from entities import QueryState
from handlers.handler import Handler
from my_time import time
from entities.instrument import Instrument
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
        query.start_time = query.end_time
        query.end_time = my_time.time + end_time
        stats_collector.add_time_in_instr(query.n_source, query.end_time - query.start_time)
        heappush(self.heap_queries, query)

    def __find_free_instrument(self) -> (Instrument, int):
        for i, instr in enumerate(self.instruments):
            if not instr.is_busy:
                return instr, i
