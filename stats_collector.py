d = {"n":None,}


class StatsCollector():
    def __init__(self):
        self.n_queries = 0
        self.m_refused_queries = 0
        self.sum_time_queries_running = 0

    def count_refuse(self, n_queries):


