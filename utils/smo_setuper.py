import constants
from app import App

t_a = 1.643
relative_accuracy = 0.1

def count_optimal_query_count(init_queries=constants.MAX_N_QUERIES):  #:App):
    app = App(init_queries)
    app.run()
    n_refused = app.put_disp.n_refused
    refused_prob = n_refused / init_queries
    print(f"refused: {n_refused}, toltal {init_queries}")
    print(f"new refused prob {refused_prob}")
    n1 = __count_new_query_count(refuse_prob=refused_prob)
    print("new n:", n1)
    app = App(int(n1))
    app.run()

    refused_prob_1 = app.put_disp.n_refused / init_queries

    print(f"old n {init_queries}, new n {n1}, refused prob {refused_prob}, ref_prob_1 {refused_prob_1}")
    if abs(refused_prob - refused_prob_1) < 0.1 * refused_prob:
        return init_queries
    else:
        return count_optimal_query_count(int(n1))


def __count_new_query_count(refuse_prob):
    return (t_a ** 2) * (1 - refuse_prob) / (refuse_prob * (relative_accuracy ** 2))
