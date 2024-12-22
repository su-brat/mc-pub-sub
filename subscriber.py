from topic import Topic
from abc import ABC, abstractmethod


class Subscriber(ABC):
    def __init__(self, name: str):
        self.name = name

    def subscribe(self, topic_name: str):
        topic = Topic.get_topic(topic_name)
        if topic is None:
            raise Exception("Topic not found!")
        topic.add_subscriber(self)

    def unsubscribe(self, topic_name: str):
        topic = Topic.get_topic(topic_name)
        if topic is None:
            raise Exception("Topic not found!")
        topic.remove_subscriber(self)

    @abstractmethod
    def on_message(self, message):
        pass
