from datetime import datetime, timedelta
from heapq import heappush

from handlers.handler import Handler
from utils import Event
from entities.instrument import Instrument
from utils.sources_processor import QueryT


class LoadInstrumentDispatcher(Handler):
    def __init__(self, buffer_extract_dispatcher, instruments: list[Instrument], heap_queries):
        self.buffer_extract_dispatcher = buffer_extract_dispatcher
        self.instruments = instruments
        self.heap_queries = heap_queries

    def handle(self, query: QueryT):
        if query.state == Event.READY_TO_SERVICE:
            self.push_instrument(query)
            query.state = Event.IN_INSTRUMENT

    def push_instrument(self, query: QueryT):
        free_instr = self.__find_free_instrument()
        end_time = free_instr.run(start_time=query.end_time)
        query.start_time = query.end_time
        query.end_time = datetime.now() + timedelta(seconds=end_time)
        heappush(self.heap_queries, query)

    def __find_free_instrument(self) -> Instrument:
        for instr in self.instruments:
            if not instr.is_busy:
                return instr
