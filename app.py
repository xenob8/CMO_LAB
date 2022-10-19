import collections
import random
from copy import copy
from heapq import heappop

import constants
import my_time
from dispatchers.buffer_extract_dispatcher import BufferExtractDispatcher
from dispatchers.buffer_put_dispatcher import BufferPutDispatcher
from dispatchers.load_instrument_dispatcher import LoadInstrumentDispatcher
from entities import QueryT
from entities.instrument import Instrument
from handler_manager import HandlerManager
from utils.sources_processor import SourcesProcessor

#todo bug with sp init from file and run with num_q as arg
class App():
    def __init__(self, max_queries=constants.MAX_N_QUERIES):
        random.seed(10)
        self.instruments = [Instrument(0.3) for _ in range(0, constants.N_INSTUMENTS)]
        self.heap_que = []
        self.sp = SourcesProcessor(heap_que=self.heap_que, max_queries=max_queries)
        self.put_disp = BufferPutDispatcher()
        self.extract_disp = BufferExtractDispatcher(buffers=self.put_disp.buffers, instruments=self.instruments,
                                                    heap_que=self.heap_que)
        self.load_disp = LoadInstrumentDispatcher(instruments=self.instruments, heap_queries=self.heap_que)
        self.manager = HandlerManager(sp=self.sp, put_disp=self.put_disp, extract_disp=self.extract_disp,
                                      load_disp=self.load_disp)

        self.sp.set_next_handler(self.put_disp).set_next_handler(self.extract_disp).set_next_handler(self.load_disp)
        self.last_source_query: QueryT = None
        self.sp.init()

    def update(self): # after init
        response = collections.defaultdict(dict)
        print("HEAPQUE")
        print(self.heap_que)
        print("BUFFERS")
        print(self.put_disp.buffers)
        if not self.heap_que:
            return False
        que_query: QueryT = heappop(self.heap_que)
        que_input = copy(que_query)
        self.last_source_query = copy(que_query)
        response["inputs"]["n_source"] = que_input.n_source
        response["inputs"]["n_query"] = que_input.n_query
        if que_query.end_time > my_time.time:
            # sleep(que_query.end_time - my_time.time)
            my_time.time = que_query.end_time

        print("NEW STATE------------------------------:\n", que_query)
        self.manager.process_new_event(que_query)

        print("priority packet:", self.extract_disp.priority_packet)

        response["buffers"] = [q.point_to_str() for q in self.put_disp.buffers]
        response["instruments"] = [instr.query.point_to_str() if instr.is_busy else '-' for instr in self.instruments]
        response["cancel"] = self.put_disp.refused_query.point_to_str() if self.put_disp.refused_query else "-"
        # print(response) # for web
        # return response # for web
        return True

    def test_run(self):
        while True:
            if not self.update():
                return

    def run(self, max_n_queries=constants.MAX_N_QUERIES):
        self.sp.MAX_N_QUERIES = max_n_queries
        while True:
            print(self.sp.total_gen_queries)
            if not self.update():
                return

    def refresh(self):
        self.sp.total_gen_queries = 0
        self.put_disp.n_refused = 0
        my_time.time = 0
        self.sp.init()
