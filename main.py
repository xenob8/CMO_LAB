from app import App
from stats.stats_collector import stats_collector

app = App()
app.run()
stats_collector.compute_stats()
stats_collector.show_sources_table()
stats_collector.show_instruments_table()
print(stats_collector.source_stats)

