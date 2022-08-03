from threading import Thread
from time import sleep


def make_tea():
    for tea in range(5):
        print(f'Thread-1: {tea}')
        sleep(2)


def make_tea2():
    for tea in range(10):
        print(f'Thread-2: {tea}')


thread = Thread(target=make_tea)
thread2 = Thread(target=make_tea2)
thread.start()
thread2.start()

for tea in range(5):
    print(f'Tea from main thread number {tea}')
    sleep(0.25)

print('FINISH')

