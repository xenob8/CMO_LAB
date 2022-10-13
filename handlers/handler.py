class Handler():
    def set_next_handler(self, handler):
        self.next_step_handler = handler
        return self.next_step_handler



