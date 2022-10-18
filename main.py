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
import collections

random.seed(10)

instruments = [Instrument(0.3) for _ in range(0, constants.N_INSTUMENTS)]

heap_que = []
sp = SourcesProcessor(heap_que=heap_que)
put_disp = BufferPutDispatcher()
extract_disp = BufferExtractDispatcher(buffers=put_disp.buffers, instruments=instruments, heap_que=heap_que)
load_disp = LoadInstrumentDispatcher(instruments=instruments, heap_queries=heap_que)
manager = HandlerManager(sp=sp, put_disp=put_disp, extract_disp=extract_disp, load_disp=load_disp)

sp.set_next_handler(put_disp).set_next_handler(extract_disp).set_next_handler(load_disp)

sp.init()


def update():
    response = collections.defaultdict(dict)
    print("HEAPQUE")
    print(heap_que)
    print("BUFFERS")
    print(put_disp.buffers)
    que_query: QueryT = heappop(heap_que)
    que_input = copy(que_query)
    response["inputs"]["n_source"] = que_input.n_source
    response["inputs"]["n_query"] = que_input.n_query
    if que_query.end_time > my_time.time:
        # sleep(que_query.end_time - my_time.time)
        my_time.time = que_query.end_time

    print("NEW STATE:\n", que_query)
    manager.process_new_event(que_query)

    print("priority packet:", extract_disp.priority_packet)

    response["buffers"] = [q.point_to_str() for q in put_disp.buffers]
    response["instruments"] = [instr.query.point_to_str() if instr.is_busy else '-' for instr in instruments]
    response["cancel"] = put_disp.refused_query.point_to_str() if put_disp.refused_query else "-"
    print(response)
    # return que_input
    return response
