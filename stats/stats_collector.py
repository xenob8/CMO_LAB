import collections
# from app import App
import constants
from .stat_data import StatData

f = open('../output.txt', 'w')


class StatsCollector():
    # stats = create_dict()
    t_a = 1.643
    relative_accuracy = 0.1

    def __init__(self, n_sources):
        self.stats = [StatData() for _ in range(n_sources)]

    def add_query(self, n_source):
        self.stats[n_source].n_queries += 1

    def add_cancel(self, n_source):
        self.stats[n_source].n_cancels += 1

    def add_time_in_buffer(self, n_source, time):
        self.stats[n_source].times_in_buffer.append(round(time,3))

    def add_time_in_instr(self, n_source, time):
        self.stats[n_source].times_in_instr.append(round(time,3))


    def print_stats(self):
        print(self.stats)

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
