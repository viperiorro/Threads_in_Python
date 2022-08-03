from threading import Thread
from time import sleep


def make_tea():
    counter = 0
    while True:
        print(f'Tea from INFINITIVE LOOP: {counter}')
        counter += 1
        sleep(0.5)


thread = Thread(target=make_tea, daemon=True)
thread.start()

for tea in range(5):
    print(f'Tea from main thread: {tea}')
    sleep(2)

print('FINISH')
