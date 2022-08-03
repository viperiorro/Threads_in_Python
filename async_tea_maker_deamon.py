from threading import Thread
from time import sleep


def make_tea():
    for tea in range(500):
        print(f'ChildThread: {tea}')
        sleep(2)


thread = Thread(target=make_tea, daemon=True)
thread.start()

for tea in range(5):
    print(f'Tea from main THREAD: {tea}')
    sleep(1)

print('FINISH')
