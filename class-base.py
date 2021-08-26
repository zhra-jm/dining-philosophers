import threading
import time


class Dinning_table(threading.Thread):
    fork = list()
    for i in range(5):
        fork.append(threading.Lock())

    def __init__(self, i, *args, **kwargs):
        self.i = i
        super().__init__(*args, **kwargs)

    @staticmethod
    def eat():
        time.sleep(10)

    def worker(self, philosopher):
        if self.fork[philosopher].acquire():
            if self.fork[philosopher + 1].acquire() if philosopher != 4 else self.fork[0].acquire():
                self.eat()
                print(f"{philosopher} ate")
                self.fork[philosopher].release()
                self.fork[philosopher + 1].release() if philosopher != 4 else self.fork[0].release()

    def run(self):
        self.worker(self.i)


if __name__ == "__main__":
    dining_list = []
    for ph in range(5):
        dining_list.append(Dinning_table(ph))

    for tr in dining_list:
        tr.start()
