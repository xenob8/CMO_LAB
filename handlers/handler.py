class Handler():
    def set_next_handler(self, handler):
        self.next_handler = handler
        return self.next_handler

    def handle(self):
        pass

    def handle_next(self):
        if not self.next_handler:
            return True
        return self.next_handler.handle()
