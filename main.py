import time
import random
import threading

class Drop:
    def __init__(self):
        self._message = None
        self._empty = True
        self._condition = threading.Condition()

    def take(self):
        with self._condition:
            while self._empty:
                self._condition.wait()
            self._empty = True
            self._condition.notify_all()
            return self._message

    def put(self, message):
        with self._condition:
            while not self._empty:
                self._condition.wait()
            self._empty = False
            self._message = message
            self._condition.notify_all()

class Producer(threading.Thread):
    def __init__(self, drop):
        super().__init__()
        self.drop = drop

    def run(self):
        important_info = [
            "Mares eat oats",
            "Does eat oats",
            "Little lambs eat ivy",
            "A kid will eat ivy too"
        ]
        for info in important_info:
            self.drop.put(info)
            time.sleep(random.random() * 2)
        self.drop.put("DONE")

class Consumer(threading.Thread):
    def __init__(self, drop):
        super().__init__()
        self.drop = drop

    def run(self):
        message = self.drop.take()
        while message != "DONE":
            print(f"MESSAGE RECEIVED: {message}")
            time.sleep(random.random() * 2)
            message = self.drop.take()

if __name__ == "__main__":
    drop = Drop()
    producer = Producer(drop)
    consumer = Consumer(drop)
    
    producer.start()
    consumer.start()
    
    producer.join()
    consumer.join()
