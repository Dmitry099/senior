from collections import defaultdict


class Message:
    def __init__(self, payload, topic):
        self.payload = payload
        self.topic = topic


class Subscriber:
    def __init__(self, dispatcher, topic):
        dispatcher.subscribe(self, topic)

    def process(self, message):
        print(f"Message: {message.payload}")


class Publisher:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def publish(self, message):
        self.dispatcher.send(message)


class Dispatcher:
    def __init__(self):
        self.topic_subscribers = defaultdict(set)

    def subscribe(self, subscribe, topic):
        self.topic_subscribers[topic].add(subscribe)

    def unsubscribe(self, subscribe, topic):
        self.topic_subscribers[topic].discard(subscribe)

    def send(self, message):
        for subscriber in self.topic_subscribers[message.topic]:
            subscriber.process(message)


def main():
    topic = "test_topic"
    d = Dispatcher()
    s = Subscriber(d, topic)
    p = Publisher(d)
    message = Message("Interesting payload", topic)
    p.publish(message)


if __name__ == '__main__':
    main()