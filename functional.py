import threading
import time

fork = list()
for i in range(5):
    fork.append(threading.Lock())


def eat():
    time.sleep(10)


def worker(philosopher):
    if fork[philosopher].acquire():
        if fork[philosopher + 1].acquire() if philosopher != 4 else fork[0].acquire():
            eat()
            print(f"{philosopher} ate")
            fork[philosopher].release()
            fork[philosopher + 1].release() if philosopher != 4 else fork[0].release()


def run():
    tr_list = list()
    for philosopher in range(5):
        t = threading.Thread(target=worker, args=(philosopher,))
        tr_list.append(t)
        t.start()


if __name__ == "__main__":
    run()
