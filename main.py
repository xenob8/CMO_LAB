import my_time
from app import App
from stats.stats_collector import stats_collector, StatsCollector
from utils.smo_setuper import count_optimal_query_count
from gui.gui import GUI

opt_queries = count_optimal_query_count()
print("optimal queries:", opt_queries)

app = App(opt_queries)
# stats_collector.reset()
app.run()

stats_collector.compute_stats()
stats_collector.show_sources_table()
stats_collector.show_instruments_table()

# gui = GUI(opt_queries)
# gui.run()


