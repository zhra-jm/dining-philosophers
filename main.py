import queue
import threading
import time

q = queue.Queue()
for i in range(5):
    q.put(i)


class Dinning_table(threading.Thread):
    fork = [threading.Lock(), threading.Lock(),
            threading.Lock(), threading.Lock(),
            threading.Lock()]

    FORK = {0: [fork[0], fork[1]], 1: [fork[1], fork[2]],
            2: [fork[2], fork[3]], 3: [fork[3], fork[4]],
            4: [fork[4], fork[0]]}

    def __init__(self, q, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)

    @staticmethod
    def eat():
        time.sleep(2)

    def worker(self, philosopher):
        if not self.FORK[philosopher][0].locked():
            if not self.FORK[philosopher][1].locked():
                self.FORK[philosopher][0].acquire()
                self.FORK[philosopher][1].acquire()
                self.eat()
                print(f"{philosopher} ate")
                self.FORK[philosopher][0].release()
                self.FORK[philosopher][1].release()
            else:
                self.q.put(philosopher)

        else:
            self.q.put(philosopher)

    def run(self):
        while True:
            philosopher = self.q.get()
            self.worker(philosopher)
            if self.q.empty():
                break


if __name__ == "__main__":
    d1 = Dinning_table(q)
    d2 = Dinning_table(q)
    d3 = Dinning_table(q)
    d4 = Dinning_table(q)
    d5 = Dinning_table(q)
    d1.start()
    d2.start()
    d3.start()
    d4.start()
    d5.start()
