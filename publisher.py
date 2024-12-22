class Publisher:
    def __init__(self, name: str, topic):
        self.name = name
        self.topic = topic

    def publish(self, message):
        self.topic.send_message(message)
