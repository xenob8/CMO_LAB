from copy import copy
from heapq import *
import random

import constants
import my_time
from dispatchers.buffer_extract_dispatcher import BufferExtractDispatcher
from dispatchers.buffer_put_dispatcher import BufferPutDispatcher
from entities.instrument import Instrument
from dispatchers.load_instrument_dispatcher import LoadInstrumentDispatcher
from utils.sources_processor import SourcesProcessor, QueryT
from entities.source import Source
from handler_manager import HandlerManager

random.seed(10)
sources = [Source(0.3) for _ in range(0, constants.N_SOURCES)]
instruments = [Instrument(0.3) for _ in range(0, constants.N_INSTUMENTS)]
buffers: list[QueryT] = []
heap_que = []
sp = SourcesProcessor(sources=sources, heap_que=heap_que)
put_disp = BufferPutDispatcher(max_size=constants.N_BUFFERS, buffers=buffers)
extract_disp = BufferExtractDispatcher(buffers=buffers, instruments=instruments, heap_que=heap_que)
load_disp = LoadInstrumentDispatcher(buffer_extract_dispatcher=extract_disp, instruments=instruments,
                                     heap_queries=heap_que)
manager = HandlerManager(sp=sp, put_disp=put_disp, extract_disp=extract_disp, load_disp=load_disp)

sp.set_next_handler(put_disp).set_next_handler(extract_disp).set_next_handler(load_disp)

sp.gather_queries()

def update():
    print("HEAPQUE")
    print(heap_que)
    print("BUFFERS")
    print(buffers)
    que_query: QueryT = heappop(heap_que)
    que_input = copy(que_query)
    if que_query.end_time > my_time.time:
        # sleep(que_query.end_time - my_time.time)
        my_time.time = que_query.end_time

    print("NEW STATE:\n", que_query)
    manager.process_new_event(que_query)

    print("priority packet:", extract_disp.priority_packet)
    return que_input

