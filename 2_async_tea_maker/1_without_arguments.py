from threading import Thread
from time import sleep


# Define a function that will be executed in a separate thread
def make_tea():
    for tea in range(5):
        print(f'Thread-1: {tea}')
        sleep(1)


# Create a thread object and pass the function to it
# The function will be executed in a separate thread simultaneously with the main thread
thread = Thread(target=make_tea)

# Start the thread
thread.start()

# The main thread will execute the code below
for tea in range(5):
    print(f'Tea from main thread number {tea}')
    sleep(0.25)

# The main thread will wait for the thread to finish
print('FINISH')

