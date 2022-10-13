from .events import Event


class NotificationService():
    def __init__(self):
        self.container = {event: [] for event in Event}

    def subscribe(self, event, listener):
        self.container[event].append(listener)

    def notify(self, event):
        listeners = self.container.get(event)
        for listener in listeners:
            print(listener)
