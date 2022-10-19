

from app import App
f = open('output.txt','w')



class StatsCollector():
    def __init__(self, app: App):
        self.n_queries = 0
        self.m_refused_queries = 0
        self.sum_time_queries_running = 0
        self.app = app
        self.relative_accuracy = 0.1
        self.t_a = 1.643

    def count_optimal_query_count(self, init_queries):
        self.app.refresh()
        self.app.run(init_queries)
        n_refused = self.app.put_disp.n_refused
        refused_prob = n_refused / init_queries
        print(f"new refused prob{refused_prob}", file=f)
        print(f"refised:{n_refused}, toltal {init_queries}", file=f)
        n1 = self.count_new_query_count(refuse_prob=refused_prob)
        self.app.refresh()
        self.app.run(init_queries)
        refused_prob_1 = self.app.put_disp.n_refused / init_queries

        print(f"old n {init_queries}, new n {n1}, refused prob {refused_prob}, ref_prob_1 {refused_prob_1}", file=f)
        if abs(refused_prob - refused_prob_1) < 0.1 * refused_prob:
            return init_queries
        else:
            return self.count_optimal_query_count(int(n1))

    def count_new_query_count(self, refuse_prob):
        return (self.t_a ** 2) * (1 - refuse_prob) / (refuse_prob * (self.relative_accuracy ** 2))


collector = StatsCollector(App())
opt_q=  collector.count_optimal_query_count(100)
print(opt_q)
