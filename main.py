import time
from datetime import datetime
from heapq import *

import constants
from observers.buffer_extract_dispatcher import BufferExtractDispatcher
from observers.buffer_put_dispatcher import BufferPutDispatcher
from observers.instrument import Instrument
from observers.loadInstrumentDispatcher import LoadInstrumentDispatcher
from observers.sources_processor import SourcesProcessor, QueryT
from source import Source

sources = [Source(0.5) for _ in range(0, constants.N_SOURCES)]
instruments = [Instrument(0.5) for _ in range(0, constants.N_SOURCES)]
buffers:list[QueryT] = []


que_sources = []
que_instruments = []
sp = SourcesProcessor(sources=sources, que=que_sources)
put_disp = BufferPutDispatcher(max_size=constants.N_BUFFERS, buffers=buffers)
extract_disp = BufferExtractDispatcher(buffers=buffers, instruments_heap=que_instruments)
load_disp = LoadInstrumentDispatcher(buffer_extract_dispatcher=extract_disp, instruments=instruments, heap_instr=que_instruments)
sp.gather_queries()
# print(que)

def handle_query(que):
    time_ = que.time
    curTime = datetime.now()
    if time_ > datetime.now():
        print("waiting", time_ - curTime)
        time.sleep((time_ - curTime).seconds)
        print(datetime.now(), "wake up")
        sp.gen_new_query(que.n_source)
        if put_disp.add(que):
            print("buffer size = ", len(buffers))
            print("BUFFER ")
            print([(buffer.n_source, buffer.n_query) for buffer in buffers])
            exit_q = extract_disp.get_query()
            if not exit_q:
                print("No places in instruments")
            else:
                print("extracted query:", exit_q)
                load_disp.push_instrument(exit_q)
            print("Pribors:", load_disp.heap_instruments)

        else:
            print("buffer overflow, canceled")


def handle_instrument(que):
    time_ = que.time
    curTime = datetime.now()
    if time_ > datetime.now():
        print("waiting", time_ - curTime)
        time.sleep((time_ - curTime).seconds)
        print(datetime.now(), "wake up")
    print("------------------RELEASE INSTRUMENT -------------")
    instr = next((x for x in instruments if x.end_time == que.time), None)
    if instr:
        instr.is_busy = False
        print("SUCCESS RELEASE:")
    time_ = que.time
    curTime = datetime.now()
    if time_ > datetime.now():
        print("waiting", time_ - curTime)
        time.sleep((time_ - curTime).seconds)
        print(datetime.now(), "wake up")
        exit_q = extract_disp.get_query()
        if not exit_q:
            print("No places in instruments")
        else:
            print("extracted query:", exit_q)
            load_disp.push_instrument(exit_q)
        print("Pribors:", load_disp.heap_instruments)


while que_sources or que_instruments:
    que_query:QueryT = que_sources[0]
    if que_instruments:
        que_insrt = que_instruments[0]
        if que_query < que_insrt:
            que_query = heappop(que_sources)
            handle_query(que_query)
        else:
            que_query = heappop(que_instruments)
            handle_instrument(que_query)
    else:
        que_query = heappop(que_sources)
        handle_query(que_query)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
