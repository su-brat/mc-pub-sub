from message import Message
from publisher import Publisher
from subscriber import Subscriber
from topic import Topic


class PublisherClient(Publisher):
    def __str__(self):
        return f"I publish messages on '{self.topic}'!"


class SubscriberClient(Subscriber):
    def __str__(self):
        return "I am a subscriber!"

    def on_message(self, message):
        print(f"{self.name}: Message received -> {message.get_content()}")


def main():
    topic1 = Topic("swagatika")
    publisher1 = PublisherClient("matrimonial-site", topic1)
    publisher2 = PublisherClient("job-site", topic1)

    topic2 = Topic("subrat")
    publisher3 = PublisherClient("matrimonial-site", topic2)
    publisher4 = PublisherClient("job-site", topic2)

    subscriber1 = SubscriberClient("subscriber-1")
    subscriber1.subscribe("swagatika")
    subscriber2 = SubscriberClient("subscriber-2")
    subscriber2.subscribe("swagatika")
    subscriber3 = SubscriberClient("subscriber-3")
    subscriber3.subscribe("subrat")

    msg1 = Message("Swagatika is no more single!")
    msg2 = Message("Swagatika is killing in job!")
    msg3 = Message("Subrat is single!")
    msg4 = Message("Subrat is hunting for job!")
    msg5 = Message("This is a test message!")

    publisher1.publish(msg1)
    publisher2.publish(msg2)
    publisher3.publish(msg3)
    publisher4.publish(msg4)

    subscriber2.unsubscribe("swagatika")

    publisher2.publish(msg5)


if __name__ == "__main__":
    main()
