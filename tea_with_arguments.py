from threading import Thread
from time import sleep


def make_tea(iterations: int, delay: float, thread_id: int):
    for tea in range(iterations):
        print(f'Tea from thread-{thread_id}: {tea}')
        sleep(delay)


thread = Thread(target=make_tea, args=(5, 1.0, 1))
thread2 = Thread(target=make_tea, args=(10, 2.0, 2))
thread.start()
thread2.start()

print('FINISH')
