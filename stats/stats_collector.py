import collections

from tabulate import tabulate

import constants
import my_time
from .instrument_data import InstrumentData
from .stat_data import StatData


class StatsCollector():

    def __init__(self, n_sources=constants.N_SOURCES, n_instr=constants.N_INSTUMENTS):
        self.source_stats = [StatData() for _ in range(n_sources)]
        self.instr_stats = [InstrumentData() for _ in range(n_instr)]

    def add_query(self, n_source):
        self.source_stats[n_source].n_queries += 1

    def add_cancel(self, n_source):
        self.source_stats[n_source].n_cancels += 1

    def add_time_in_buffer(self, n_source, time):
        self.source_stats[n_source].times_in_buffer.append(round(time, 3))

    def add_time_in_instr(self, n_source, time):
        self.source_stats[n_source].times_in_instr.append(round(time, 3))

    def add_instrument_time(self, n_instr, time):
        self.instr_stats[n_instr].work_times.append(round(time, 3))

    def compute_stats(self):
        for stat_data in self.source_stats:
            stat_data.compute()
        for stat_instr in self.instr_stats:
            stat_instr.compute()

    def show_sources_table(self):
        headers = ["Номер источника", "кол-во заявок", "p отк", "Tпреб", "Tбуф", "Tобсл", "Дбуф", "Добсл"]
        table = []
        table.append(headers)
        for i, stat_data in enumerate(self.source_stats):
            table.append([f"Soruce {i}", stat_data.n_queries, stat_data.refuse_prob, stat_data.avg_total_time,
                          stat_data.avg_buffer_time, stat_data.avg_instr_time, stat_data.dispersion_buffer,
                          stat_data.dispersion_instr])
        print(tabulate(table, headers='firstrow', tablefmt='grid'))

    def show_instruments_table(self):
        headers = ["Номер прибора", "коэф использования"]
        table = []
        table.append(headers)
        # total_global_time = sum(instr.total_time for instr in self.instr_stats)
        total_global_time = my_time.time
        print("total time:", total_global_time)
        for i, instr_data in enumerate(self.instr_stats):
            table.append([f'Прибор {i}', round(instr_data.total_time / total_global_time, 3)])
        print(tabulate(table, headers='firstrow', tablefmt='grid'))

    def source_table_dict(self):
        rows = collections.defaultdict(dict)
        for i, stat_data in enumerate(self.source_stats):
            rows[f'{i}'] = [f"Soruce {i}", stat_data.n_queries, stat_data.refuse_prob, stat_data.avg_total_time,
                          stat_data.avg_buffer_time, stat_data.avg_instr_time, stat_data.dispersion_buffer,
                          stat_data.dispersion_instr]
        return rows

    def instruments_table_dict(self):
        rows = collections.defaultdict(dict)
        total_global_time = my_time.time
        print("total time:", total_global_time)
        for i, instr_data in enumerate(self.instr_stats):
            rows[i] = [f'Instrument {i}', round(instr_data.total_time / total_global_time, 3)]
        return rows


    def print_stats(self):
        print(self.source_stats)

    def reset(self):
        self.source_stats = [StatData() for _ in range(len(self.source_stats))]
        self.instr_stats = [InstrumentData() for _ in range(len(self.instr_stats))]


stats_collector = StatsCollector(constants.N_SOURCES)
