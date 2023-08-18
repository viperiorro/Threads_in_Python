from threading import Thread
from time import sleep


def make_tea():
    counter = 0
    while True:  # INFINITIVE LOOP
        print(f'Tea from INFINITIVE LOOP: {counter}')
        counter += 1
        sleep(0.5)


# Create daemon thread
# The main thread will not wait for the daemon thread to finish
thread = Thread(target=make_tea, daemon=True)
thread.start()

for tea in range(5):
    print(f'Tea from main thread: {tea}')
    sleep(2)

# The main thread will not wait for the daemon thread to finish
print('FINISH')
