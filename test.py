from app import App
from stats import stats_collector

app = App(1030)
app.run()

stats_collector.compute_stats()
stats_collector.show_sources_table()
stats_collector.show_instruments_table()
print(stats_collector.source_table_dict())
# print(stats_collector.instr_stats)
