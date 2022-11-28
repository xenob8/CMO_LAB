import my_time
from app import App
from stats.stats_collector import singleton
from utils.smo_setuper import count_optimal_query_count
from gui.gui import GUI
from app_config import AppConfig
SMART_DOCTOR_TIME = 5*60
MIDDLE_DOCRTOR_TIME = 6*60
STUDENT_DOCTOR_TIME = 8*60

doctors = [SMART_DOCTOR_TIME, SMART_DOCTOR_TIME, SMART_DOCTOR_TIME, MIDDLE_DOCRTOR_TIME,  STUDENT_DOCTOR_TIME]

config = AppConfig(max_queries=30240, sources_speed=[1/180, 1/360, 1/240], buffer_size=4,
                   instruments_work_time=doctors)

app = App(config)
app.run()

singleton.stats_collector.compute_stats()
singleton.stats_collector.show_sources_table()
singleton.stats_collector.show_instruments_table()


# opt_queries = count_optimal_query_count()
# print("optimal queries:", opt_queries)
# gui = GUI(opt_queries)
# gui.run()
