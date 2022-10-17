import time
from datetime import datetime
from heapq import *

import constants
from utils import Event
from dispatchers.buffer_extract_dispatcher import BufferExtractDispatcher
from dispatchers.buffer_put_dispatcher import BufferPutDispatcher
from entities.instrument import Instrument
from dispatchers.load_instrument_dispatcher import LoadInstrumentDispatcher
from utils.sources_processor import SourcesProcessor, QueryT
from entities.source import Source

sources = [Source(0.5) for _ in range(0, constants.N_SOURCES)]
instruments = [Instrument(0.5) for _ in range(0, constants.N_SOURCES)]
buffers: list[QueryT] = []
heap_que = []
sp = SourcesProcessor(sources=sources, heap_que=heap_que)
put_disp = BufferPutDispatcher(max_size=constants.N_BUFFERS, buffers=buffers)
extract_disp = BufferExtractDispatcher(buffers=buffers, instruments=instruments, heap_que=heap_que)
load_disp = LoadInstrumentDispatcher(buffer_extract_dispatcher=extract_disp, instruments=instruments,
                                     heap_queries=heap_que)

sp.set_next_handler(put_disp).set_next_handler(extract_disp).set_next_handler(load_disp)

sp.gather_queries()
# print(que)

while heap_que:
    print("HEAPQUE")
    print(heap_que)
    print("BUFFERS")
    print(buffers)
    que_query: QueryT = heappop(heap_que)
    now_time = datetime.now()
    if que_query.end_time > now_time:
        time.sleep((que_query.end_time - now_time).seconds)

    print("NEW STATE:\n", que_query)
    if que_query.state == Event.WAITING_SOURCE:
        sp.handle(que_query)
    elif que_query.state == Event.IN_INSTRUMENT:
        instruments[que_query.n_source].release()
        print("RELEASE INSTRUMENT HANDLER")
        extract_disp.handle()

    print("priority packet:", extract_disp.priority_packet)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
