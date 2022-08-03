from threading import Thread
from time import sleep


def make_tea():
    for tea in range(5):
        print(f'Tea from CHILD thread: {tea}')
        sleep(2)


thread = Thread(target=make_tea)
thread.start()
thread.join(timeout=15)

for tea in range(5):
    print(f'Tea from MAIN thread: {tea}')
    sleep(0.1)

print('FINISH')
