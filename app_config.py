class AppConfig:
    def __init__(self, max_queries, sources_speed: list, buffer_size, instruments_work_time: list):
        self.instruments_work_time = instruments_work_time
        self.buffer_size = buffer_size
        self.sources_speed = sources_speed
        self.max_queries = max_queries
