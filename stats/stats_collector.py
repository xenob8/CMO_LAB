import collections
# from app import App
from tabulate import tabulate

import constants
from .instrument_data import InstrumentData
from .stat_data import StatData

f = open('../output.txt', 'w')


class StatsCollector():
    # stats = create_dict()
    t_a = 1.643
    relative_accuracy = 0.1

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
        total_global_time = sum(instr.total_time for instr in self.instr_stats)
        print("total time:", total_global_time)
        for i, instr_data in enumerate(self.instr_stats):
            table.append([f'Прибор {i}', round(instr_data.total_time / total_global_time, 3)])
        print(tabulate(table, headers='firstrow', tablefmt='grid'))

    def print_stats(self):
        print(self.source_stats)

    @staticmethod
    def count_optimal_query_count(init_queries, app):  #:App):
        app.refresh()
        app.run(init_queries)
        n_refused = app.put_disp.n_refused
        refused_prob = n_refused / init_queries
        print(f"new refused prob{refused_prob}", file=f)
        print(f"refised:{n_refused}, toltal {init_queries}", file=f)
        n1 = StatsCollector.__count_new_query_count(refuse_prob=refused_prob)
        app.refresh()
        app.run(init_queries)
        refused_prob_1 = app.put_disp.n_refused / init_queries

        print(f"old n {init_queries}, new n {n1}, refused prob {refused_prob}, ref_prob_1 {refused_prob_1}", file=f)
        if abs(refused_prob - refused_prob_1) < 0.1 * refused_prob:
            return init_queries
        else:
            return StatsCollector.count_optimal_query_count(int(n1), app)

    @staticmethod
    def __count_new_query_count(refuse_prob):
        return (StatsCollector.t_a ** 2) * (1 - refuse_prob) / (refuse_prob * (StatsCollector.relative_accuracy ** 2))


stats_collector = StatsCollector(constants.N_SOURCES)

# app = App()
# opt_q = StatsCollector.count_optimal_query_count(100, app)
# print(opt_q)
