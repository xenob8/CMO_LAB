from app import App
from stats.stats_collector import stats_collector

app = App()
app.run()
stats_collector.print_stats()

