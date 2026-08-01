class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, handler):
        self.listeners.setdefault(event_name, []).append(handler)

    def publish(self, event_name, data=None):

        for handler in self.listeners.get(event_name, []):
            handler(data)
