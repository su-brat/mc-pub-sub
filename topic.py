class Topic:
    REGISTRY = {}

    def __init__(self, name: str):
        self.name = name
        self.subscribers = set()
        self.REGISTRY[name] = self

    def send_message(self, message):
        for subscriber in self.subscribers:
            subscriber.on_message(message)

    def add_subscriber(self, subscriber):
        self.subscribers.add(subscriber)

    def remove_subscriber(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    @staticmethod
    def get_topic(topic_name: str):
        return Topic.REGISTRY.get(topic_name)

    def remove(self):
        del self.REGISTRY[self.name]
        del self
