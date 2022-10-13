import time
from functools import reduce

from observers.sources_processor import QueryT
from source import Source
from observers import Event
from observers import NotificationService
from heapq import heappop, heappush
from datetime import datetime, timedelta

print(str(datetime.now().strftime()))





# ns = NotificationService()
# ns.subscribe(Event.INSTRUMENT_RELEASE, foo)
# ns.notify(Event.INSTRUMENT_RELEASE)
# print(ns.container)
# newRequest = handleSources(sources)
# BuffDispatcher.handle(request)
# request = chooseRequestDispatcher.handle(buffer) -> #ставится на прибор
# chooseInstrumentDispatcher.handle(request)
