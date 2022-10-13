from datetime import datetime, timedelta
from heapq import heappush

from observers.instrument import Instrument
from observers.sources_processor import QueryT


class LoadInstrumentDispatcher():
    def __init__(self, buffer_extract_dispatcher, instruments: list[Instrument], heap_instr):
        self.buffer_extract_dispatcher = buffer_extract_dispatcher
        self.instruments = instruments
        self.heap_instruments = heap_instr

    def push_instrument(self, query:QueryT):
        free_instr = self.__find_free_instrument()
        end_time = free_instr.run()
        new_q = QueryT(time=datetime.now() + timedelta(seconds=end_time), n_query=query.n_query, n_source=query.n_source)
        free_instr.end_time = new_q.time
        heappush(self.heap_instruments, new_q)

    def __find_free_instrument(self) -> Instrument:
        for instr in self.instruments:
            if not instr.is_busy:
                return instr
