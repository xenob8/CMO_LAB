import statistics


class InstrumentData:
    def __init__(self):
        self.work_times = []
        self.total_time = 0

    def compute(self):
        self.total_time = round(sum(self.work_times), 3)

    def __str__(self):
        self.compute()
        return f'work times: {self.work_times}\n' \
               f'total time: {self.total_time}'

    def __repr__(self):
        return self.__str__()
