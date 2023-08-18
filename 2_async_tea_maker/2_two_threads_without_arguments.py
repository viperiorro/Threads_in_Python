from threading import Thread
from time import sleep


# Define a function that will be executed in a separate thread
def make_tea():
    for tea in range(5):
        print(f'Thread-1: {tea}')
        sleep(1)

def make_tea2():
    for tea in range(10):
        print(f'Thread-2: {tea}')


# Create a thread object and pass the function to it
# The function will be executed in a separate thread simultaneously with the main thread
thread = Thread(target=make_tea)
thread2 = Thread(target=make_tea2)

# Start the threads
thread.start()
thread2.start()

# The main thread will execute the code below
for tea in range(5):
    print(f'Tea from main thread number {tea}')
    sleep(0.25)

# The main thread will wait for the thread to finish
print('FINISH')

