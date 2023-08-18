from threading import Thread
from time import sleep


def make_tea(iterations: int, delay: float, thread_id: int):
    for tea in range(iterations):
        print(f'Tea from thread-{thread_id}: {tea}')
        sleep(delay)


thread1 = Thread(target=make_tea, args=(10,), kwargs={"delay": 1.0, "thread_id": 1})
thread1.start()

print('FINISH')
