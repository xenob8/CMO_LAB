import statistics


class StatData:
    def __init__(self):
        self.n_queries = 0
        self.n_cancels = 0
        self.refuse_prob = 0
        self.times_in_buffer = []
        self.times_in_instr = []
        self.avg_buffer_time = 0
        self.avg_instr_time = 0
        self.avg_total_time = 0

    def compute(self):
        self.avg_buffer_time = round(statistics.fmean(self.times_in_buffer), 3)
        self.avg_instr_time = round(statistics.fmean(self.times_in_instr), 3)
        self.avg_total_time = round(self.avg_buffer_time + self.avg_instr_time, 3)
        self.refuse_prob = round(self.n_cancels / self.n_queries, 3)
        self.dispersion_buffer = round(statistics.pvariance(self.times_in_buffer), 3)
        print("max time in buffer", max(self.times_in_buffer)/60)
        self.dispersion_instr = round(statistics.pvariance(self.times_in_instr), 3)

    def __str__(self):
        self.compute()
        return f'queris: {self.n_queries},\n' \
               f'cancels: {self.n_cancels},\n' \
               f'refuse_prob: {self.refuse_prob}\n' \
               f'time_in_buffers : {self.times_in_buffer}\n' \
               f'time_in_instrum : {self.times_in_instr}\n' \
               f'avg_buffer_time : {self.avg_buffer_time}\n' \
               f'avg_instr_time : {self.avg_instr_time}\n' \
               f'avg_total_time : {self.avg_total_time}\n' \
               f'-------------------------\n'

        def __repr__(self):
            return self.__str__()
